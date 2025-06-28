# Sample automation script to find square of number 5 and render it in 127.0.0.1:8000/app1/
# Hard code project name, no input
# Hard code app name
# Open settings.py and do find replace
# Open urls.py and do find replace
# Open views.py and do find replace
# Create templates/app1/index.html
# Create app1/urls.py
# run python manage.py runserver
import subprocess
import os
from subprocess import CalledProcessError

list1 = ["automationTester", "app1"]
try:
    subprocess.run(f'django-admin startproject {list1[0]}', shell=True, stdout=subprocess.DEVNULL, check=True)
except subprocess.CalledProcessError:
    print("something happened with the program")
os.chdir(list1[0])
try:
    subprocess.run(f'django-admin startapp {list1[1]}', shell=True, stdout=subprocess.DEVNULL, check=True)
except subprocess.CalledProcessError:
    print("something happened with the program")
os.chdir("automationTester")
f1 = open('settings.py', 'r+')
settings = f1.read()
modified_settings = settings.replace("'django.contrib.staticfiles',", f"'django.contrib.staticfiles',\n\t'{list1[1]}',")
f1.seek(0)
f1.write(modified_settings)
f1.close()
f1 = open('urls.py', 'r+')
urls = f1.read()
modified_urls = urls.replace("from django.urls import path", "from django.urls import path, include").replace("admin.site.urls),", f"admin.site.urls),\n\tpath('{list1[1]}/', include('{list1[1]}.urls')),")
f1.seek(0)
f1.write(modified_urls)
f1.close()
os.chdir('..')
os.chdir('app1')
f1 = open('views.py', 'a')
factorialFunction = """def home(request):
    num=5
    result=1
    for i in range(1, num+1, 1):
        result*=i
    return render(request,'app1/index.html', {'param1':num,'param2':result})"""
f1.write(factorialFunction)
f1.close()
try:
    subprocess.run('mkdir templates', shell=True, stdout=subprocess.DEVNULL, check=True)
    os.chdir('templates')
    subprocess.run(f'mkdir {list1[1]}', shell=True, stdout=subprocess.DEVNULL, check=True)
    os.chdir('app1')
except CalledProcessError:
    print("something happened with the program")
f1 = open('index.html', 'w')
htmlFile = """<!DOCTYPE html>
<html lang=en>
<head>
    <meta charset="UTF-8">
    <title>Rahul's automatic factorial generator</title>
</head>
<body>
    <h1>Automatic Factorial Script</h1>
    <p>The factorial of {{param1}} is {{param2}}</p>
</body>
</html>"""
f1.write(htmlFile)
f1.close()
os.chdir('../../')
f1 = open('urls.py', 'w')
urls ="""from django.urls import path
from app1.views import home
urlpatterns = [path('', home),]"""
f1.write(urls)
f1.close()
os.chdir('..')
subprocess.run("python manage.py runserver", shell=True)