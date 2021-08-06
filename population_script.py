import os

from django.db.models.fields import CommaSeparatedIntegerField
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page,Comment,User

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views':120,},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views':12,},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/'
         ,'views':10,},
        {'title':'Learn Python in 100 Minutes',
         'url':'http://docs.python.org/3/whatsnew/changelog.html'
         ,'views':10,},
        {'title':'Welcome to Github',
         'url':'https://github.com/'
         ,'views':10,} ]
    
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':110,},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/','views':121,},
        {'title':'Introducing Twd',
         'url':'http://www.tangowithdjango.com/#intro','views':122,},
        {'title':'How to Tango with me',
         'url':'http://www.tangowithdjango.com/#authors','views':122,} ]

    java_pages = [
        {'title':'Official java Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':140,},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/','views':161,},
        {'title':'How to write code',
         'url':'http://codetop.cc/#/home','views':162,} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/','views':134,},
        {'title':'Flask',
         'url':'http://flask.pocoo.org','views':100,} ]



     #add user
    user_test1 = User.objects.create(username='luobida',password='pl050030809',email='222@qq.com')
    user_test1.save()
    user_test2 = User.objects.create(username='pikaqiu',password='qq050030809',email='fff@qq.com')
    user_test2.save()
    user_test3 = User.objects.create(username='nird',password='qe050030809',email='dadfadad@qq.com')
    user_test3.save()
    user_test4 = User.objects.create(username='father',password='qe050030809',email='dadfadad@qq.com')
    user_test4.save()
    user_test5 = User.objects.create(username='son',password='faf05003080',email='daadaad@qq.com')
    user_test5.save()
    user_test6 = User.objects.create(username='moon',password='ff50030809',email='eedfadad@qq.com')
    user_test6.save()

    luobida = User.objects.get_or_create(username='luobida')  
    pikaqiu = User.objects.get_or_create(username='pikaqiu') 
    nird = User.objects.get_or_create(username='nird') 
    father = User.objects.get_or_create(username='father') 
    son = User.objects.get_or_create(username='son')
    moon= User.objects.get_or_create(username='moon')



    
    python_comments = [{'user': son[0], 'time':'2021-08-05 09:23:21','content':'python is the best','likes': 10},
                {'user': luobida[0], 'time':'2021-08-05 09:23:22','content':'you rae my father','likes': 101},
               {'user': pikaqiu[0], 'time':'2021-08-05 09:23:23','content':'lalala','likes': 102},
               {'user': moon[0], 'time':'2021-08-06 09:23:24','content':'i love you','likes': 107},
               {'user': nird[0], 'time':'2021-08-07 09:23:25','content':'i love you too','likes': 17},
               {'user': father[0], 'time':'2021-08-09 09:23:28','content':' i am hungry','likes': 127},
                 ]

    django_comments = [{'user': nird[0], 'time':'2021-08-05 09:23:28','content':'java is the best','likes': 10},
                {'user': luobida[0], 'time':'2021-08-05 09:23:29','content':'i am your father','likes': 11},
               {'user': father[0], 'time':'2021-08-05 09:23:31','content':'Code contains helpe','likes': 12},
               {'user': moon[0], 'time':'2021-08-05 09:23:31','content':'Code is readable, clear and commented where appropriate ','likes': 13},
               {'user': pikaqiu[0], 'time':'2021-08-06 09:23:32','content':'Unit tests are included ','likes': 14,},
               {'user': son[0], 'time':'2021-08-07 09:23:34','content':'user authentication, unit testing','likes': 17}  ]

    java_comments = [{'user': nird[0], 'time':'2021-08-05 09:23:35','content':'models, Javascript, AJAX','likes': 1},
                {'user': luobida[0], 'time':'2021-08-05 09:23:36','content':'the app should involve user authentication;','likes': 1},
               {'user': moon[0], 'time':'2021-09-05 09:23:38','content':'asasasa','likes': 3},
               {'user': father[0], 'time':'2021-08-05 09:23:39','content':'Here is a possible breakdown of responsibilities ','likes': 4,},
               {'user': son[0], 'time':'2021-08-05 09:23:40','content':'it should certainly interact with a new model stored in the database;','likes': 5,},
               {'user': pikaqiu[0], 'time':'2021-03-05 09:23:41','content':'Here is a possible breakdown of responsibilities ','likes': 107}  ]

    other_comments = [{'user': nird[0], 'time':'2021-08-05 09:23:42','content':'it should be visually appealing and have an intuitive user interface;','likes': 10},
                {'user': luobida[0], 'time':'2021-08-05 09:23:43','content':'Polished / refined interface, not clunky','likes': 101},
               {'user': father[0], 'time':'2021-06-05 09:23:44','content':'Uses a responsive CSS framework','likes': 102},
               {'user': son[0], 'time':'2021-08-05 09:23:45','content':'URLs are relative i.e. use the {% url ... %} tag','likes': 3},
               {'user': pikaqiu[0], 'time':'2021-04-05 09:23:46','content':'Code contains helper functions/classes (if required)','likes': 104},
               {'user': moon[0], 'time':'2021-08-07 09:23:47','content':'Code is readable, clear and commented where appropriate','likes': 5} ]
               


    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64,'comments':python_comments},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32,'comments':django_comments},
            'Java': {'pages': java_pages, 'views': 63, 'likes': 42,'comments':java_comments},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16,'comments':other_comments,} }


    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for comment in cat_data['comments']:           
            com = add_comment(c,comment['user'],comment['time'],comment['content'],comment['likes']) 
            print(com)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
            print(c,p)
    





#add comment
def add_comment(cat,user,time,content,likes):
    comment = Comment.objects.get_or_create(category = cat,user=user)[0]
    comment.time = time
    comment.content = content
    comment.likes = likes
    comment.save()
    print(content)
    return comment

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
#add user
def add_user(username,pasword,email):
    user_test = User.objects.get_or_create(username=username,password=pasword,email=email)
    return user_test

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()