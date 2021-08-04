from django.contrib.auth.models import User
from django.template.defaultfilters import title
from django.test import TestCase
from rango.models import Category, Page,UserProfile,Comment
from django.urls import reverse
from django.db import models

def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category

def add_page(category,title,url,views =0):
    page = Page.objects.create(category=category,title=title,url=url)
    page.views = views
    page.save()
    return page

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no categories exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])
    
    def test_index_view_with_categories(self):
        """
        Checks whether categories are displayed correctly when present.
        """
        add_category('Python', 1, 1)
        add_category('C++', 1, 1)
        add_category('Erlang', 1, 1)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")
        self.assertContains(response, "C++")
        self.assertContains(response, "Erlang")
        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)


    def test_index_view_with_pages(self):
        """
        Checks whether pages are displayed correctly when present.
        """
        python = add_category('Python', 1, 1)
        
        add_page(python,'Test1','http://127.0.0.1:8000/rango/category/sdsd/',1)
        add_page(python,'Test3','http://127.0.0.1:8000/rango/category/',1)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test1")
        self.assertContains(response, "http://127.0.0.1:8000/rango/category/sdsd/")
        self.assertContains(response, "Test3")
        self.assertContains(response, "http://127.0.0.1:8000/rango/category/")
        
        num_pages = len(response.context['pages'])
        self.assertEquals(num_pages, 2)

class ModelsTests(TestCase):
    def test_ensure_modles_are_correct(self):
        
        #Test Category Models
        category = Category(name='Python',views=1,likes=2)
        category.save()
        self.assertEqual((category.likes== 2), True)
        self.assertEqual((category.views== 1 ), True)

        #Test Category Models
        page = Page(category = category,title = 'Test1',url = 'http://127.0.0.1:8000/rango/category/sdsd/',views = 1)
        self.assertEqual((page.views== 1), True)
        self.assertEqual((page.title == 'Test1'), True)
        self.assertEqual((page.url == 'http://127.0.0.1:8000/rango/category/sdsd/'), True)
        self.assertEqual((page.category == category), True)

        #Test UserProfile Models
        user_test1=User(username='simon',password='pl050030809')
        userProfile=UserProfile(user=user_test1,website='http://127.0.0.1:8000/rango/category/sdsd/#')
        self.assertEqual((userProfile.user== user_test1), True)
        self.assertEqual((userProfile.website== "http://127.0.0.1:8000/rango/category/sdsd/#"), True)

        #Test Comment Models
        user_test2=User(username='father',password='pl050030809')
        time_test='2021-08-04-06:56:22'
        content_test="xxxxxxxx"
        comment = Comment(user=user_test2,category=category,time=time_test,content=content_test)
        self.assertEqual((comment.user== user_test2), True)
        self.assertEqual((comment.time== '2021-08-04-06:56:22'), True)
        self.assertEqual((comment.content== "xxxxxxxx"), True)