check whether django package installed: python -c "import django; print(django.get_version())"
install django: pip install Django
to generate basic project structure run: django-admin startproject mysite_name
to generate basic app structure run: python manage.py startapp app_name
to start server run: python manage.py runserver [ip:port]

to make migration script run: python manage.py makemigrations app_name
to apply migration script run: python manage.py migrate # django will track what migrations should be applied and run them
to see the SQL that will be applied by migration run: python manage.py sqlmigrate app_name migration number

admin : 123qweadmin