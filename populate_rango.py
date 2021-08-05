import os
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
         ,'views':10,} ]
    
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':110,},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/','views':121,},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/','views':122,} ]

    java_pages = [
        {'title':'Official java Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':140,},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/','views':161,},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/','views':162,} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/','views':134,},
        {'title':'Flask',
         'url':'http://flask.pocoo.org','views':100,} ]

    
    
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Java': {'pages': java_pages, 'views': 63, 'likes': 42},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    user_test1=User(username='father',password='pl050030809')    
    user_test2=User(username='son',password='pl050030809')  

    comments = {'Python': {'user': user_test1, 'time':'2021-08-05 09:23:21','content':'xxxvavavxxxx','likes': 10},
                'Django': {'user': user_test1, 'time':'2021-08-03 09:23:21','content':'hahahahah','likes': 101},
                'Python': {'user': user_test1, 'time':'2021-08-04 09:23:21','content':'lalala','likes': 102},
                'Django': {'user': user_test2, 'time':'2021-08-05 09:23:21','content':'asasasa','likes': 103},
                'Python': {'user': user_test1, 'time':'2021-08-06 09:23:21','content':'wobuhi','likes': 104},
                'Django': {'user': user_test2, 'time':'2021-08-07 09:23:21','content':'tttttt','likes': 105},
                'Python': {'user': user_test1, 'time':'2021-08-08 09:23:21','content':'aaaaaa','likes': 107},
            
            }
    





    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

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

def add_comment(name,user,time,content,likes):
    cat = Category.objects.get_or_create(name=name)[0]
    comment = Comment.objects.create()
    comment.user = user
    comment.category = cat
    comment.time = time
    comment.content = content
    comment.likes = likes
    comment.save()
    return comment

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()