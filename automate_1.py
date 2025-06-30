# Step 0.5
import subprocess
import os
import sys

# Steps 1 and 2
list1 = sys.argv
del list1[0]
try:
    subprocess.run(f'django-admin startproject {list1[0]}', shell=True, stdout=subprocess.DEVNULL, check=True)
except subprocess.CalledProcessError:
    print("something happened with the program")
os.chdir(list1[0])
try:
    subprocess.run(f'django-admin startapp {list1[1]}', shell=True, stdout=subprocess.DEVNULL, check=True)
except subprocess.CalledProcessError:
    print("something happened with the program")

# Step 3
os.chdir(list1[0])
f1 = open('settings.py', 'r+')
old_settings = f1.read()
new_settings = old_settings.replace("'django.contrib.staticfiles',", f"'django.contrib.staticfiles',\n\t'{list1[1]}',")
f1.seek(0)
f1.write(new_settings)
f1.close()

# Step 4
f1 = open('urls.py', 'r+')
old_urls = f1.read()
new_urls = old_urls.replace("from django.urls import path", "from django.urls import path, include").replace("admin.site.urls),", f"admin.site.urls),\n\tpath('{list1[1]}/', include('{list1[1]}.urls')),")
f1.seek(0)
f1.write(new_urls)
f1.close()

# Step 5
os.chdir('..')
os.chdir(list1[1])
f1 = open('views.py', 'a')
factorialFunction = """def home(request):
    num=5
    result=1
    for i in range(1, num+1, 1):
        result*=i
    return render(request,'app1/index.html', {'param1':num,'param2':result})"""
f1.write(factorialFunction)
f1.close()

# Step 6
os.chdir('../..')
f1 = open('htmlFile.txt', "r")
htmlFile = f1.read()
f1.close()

# Step 7
os.chdir('django3/app1')
try:
    subprocess.run('mkdir templates', shell=True, stdout=subprocess.DEVNULL, check=True)
    os.chdir('templates')
    subprocess.run(f'mkdir {list1[1]}', shell=True, stdout=subprocess.DEVNULL, check=True)
    os.chdir(list1[1])
except subprocess.CalledProcessError:
    print("something happened with the program")
f1 = open('index.html', 'w')
f1.write(htmlFile)
f1.close()

# Step 8
os.chdir('../../')
f1 = open('urls.py', 'w')
urls ="""from django.urls import path
from app1.views import home
urlpatterns = [path('', home),]"""
f1.write(urls)
f1.close()

# Step 9
os.chdir('..')
subprocess.run("python manage.py runserver", shell=True)