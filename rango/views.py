from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rango.models import Category, Comment
from rango.models import Page
from rango.forms import CategoryForm, CommentForm, PageForm, UserForm, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.core.paginator import Paginator
def index(request):
    # Refer to the TwD book for more information on how this updated view works.
    category_list = Category.objects.order_by('-likes')
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    visitor_cookie_handler(request)

    response = render(request, 'rango/index.html', context=context_dict)
    return response


def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    #分页
    category = Category.objects.get(slug=category_name_slug)
    all_comments = Comment.objects.filter(category=category).order_by('-likes')
    #每页4个
    paginator = Paginator(all_comments,4)
    page_commenrs = request.GET.get('page')
    comments = paginator.get_page(page_commenrs)

    try:
        #category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        #comments = Comment.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['comments'] = comments
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
        context_dict['comments'] = None

    return render(request, 'rango/category.html', context=context_dict)


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/rango/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(
                    reverse('rango:show_category',
                            kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'rango/register.html',
                  context={
                      'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered
                  })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


@login_required
def add_comment(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None

    if category is None:
        return redirect('/rango/')

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            if category:
                comment = form.save(commit=False)
                comment.category = category
                comment.user = request.user
                comment.views = 0
                comment.save()

                return redirect(
                    reverse('rango:show_category',
                            kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_comment.html', context=context_dict)
    
@login_required
@csrf_exempt
@require_POST
def delete_comment(request):
    
    #登录用户可以删除任意一条评论
    # 根据 id 获取需要删除的文章
    comment_id = request.POST['comment_id']
    print(comment_id)
    try:
        comment = Comment.objects.get(id=comment_id)
        c_id = Comment.objects.filter(id=comment_id).values_list('category_id', flat=True)[0]
        c_name = Category.objects.filter(id=c_id).values_list('name', flat=True)[0]
        print(c_name)
        # 调用.delete()方法删除评论
        comment.delete()
        # 完成删除后返回当前类别页面
        return HttpResponse("1")
    except:
        return HttpResponse("2")  

#Like for category
@login_required
@csrf_exempt
@require_POST
def like_category(request):
    category_id = request.POST['category_id']
    try:
        #The category is determined by the Id
        category = Category.objects.get(id=int(category_id))
        category.likes = category.likes + 1
        category.save()
        return HttpResponse("1")
        #If the likes fail
    except Category.DoesNotExist:
        return HttpResponse("2")
    except ValueError:
        return HttpResponse("2")
    


#Like for commnent
@login_required
@csrf_exempt
@require_POST
def like_comment(request):
    print("点赞评论")
    comment_id = request.POST['comment_id']
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.likes += 1
        comment.save()
        # successful
        return HttpResponse("1")
    except:
        return HttpResponse("2")