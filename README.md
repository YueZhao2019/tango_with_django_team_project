
`Python` `js` `Django` 

## **Version** 
>  django==2.1.5  
>  Python==3.7.5  
>  
## **Step 0** ：Activate the environment
>  ./conda activate rango

## **Step 1** ：Install
>  pip install django-tinymce  
>  pip install social-auth-app-django  
>  pip install coverage  
>  pip install -U django-registration-redux==2.2  

## **Step 2** ：Make database migrations and fill in the data
>  python manage.py makemigrations  
>  python manage.py migrate  
>  python populate_rango.py  


## **Step 3** ：Creating a Superuser
>  python manage.py createsuperuser  

## **Step 4** ：Run
>  python manage.py runserver  


Open the browser: http://127.0.0.1:8000/
