# Django

## 1. 시작하기

[`Django_girls`](https://docs.djangoproject.com/ko/2.1/intro/)



1. 프로젝트 시작하기

   ```bash
   $ pip install django(쟝고)
   $ django-admin startproject 프로젝트이름
   ```

   아래와 같이 프로젝트 구조가 만들어진다.

   ```bash
   ├── db.sqlite3
   ├── django_intro
   │   ├── __init__.py
   │   ├── __pycache__
   │   │   ├── __init__.cpython-36.pyc
   │   │   ├── settings.cpython-36.pyc
   │   │   ├── urls.cpython-36.pyc
   │   │   └── wsgi.cpython-36.pyc
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py
   ```

   지금부터 pwd는 '-workspace/django-intro 이다.'



1. 서버 실행하기

   - `settings.py`

     ```bash
     ALLOWED_HOSTS = ['*']
     # c9에서는 host - 0.0.0.0, port - 8080만 활용할 수 있기 때문에 위와 같이 설정한다.
     ```

   ```bash
   ~/workspace/django_intro $ python manage.py runserver 0.0.0.0:8080
   ```

   ```
   vi .gitignore
   복붙
   ```

   ```bash
   gitignore.io
   ```

   앞으로 모든 장고 명령어는 프로젝트를 만들 때를 제외하고 `python manage.py`를 활용한다. 따라서 반드시 `pwd`와 `ls`를 통해 현재 bash(터미널) 위치를 확인하자!!

```
python manage.py startapp 이름.py
```



## 2. hello, Django

> Django 프로젝트는 여러가지 app의 집합이다.
>
> 각각의 app은 MTV 패턴으로 구성되어 있다.
>
> M (Model) : 어플리케이션의 핵심 로직의 동작을 수행한다. 
>
> T (Template) : 사용자에게 결과물을 보여준다.
>
> V (view) :  모델과 템플릿의 동작을 제어한다. (모델의 상태를 변경하거나 값을 가져오고, 템플릿에 값을 전달하기 등)
>
> **일반적으로 MVC패턴으로 더 많이 사용된다.**



### 기본로직

앞으로 우리는 1. 요청 url 설정(`urls.py`) 2. 처리 할 view 설정(`view.py`) 3. 결과 보여줄 template설정(`templates/`)으로 작성할 것이다.

1. url 설정

   ```python
   # django_intro/urls.py
   from django.contrib import admin
   from django.urls import path
   # home 폴더 내에 있는 views.py를 불러온다.
   from home import views
   
   urlpatterns = [
       path('admin/', admin.site.urls), 
       # 요청이 home/으로 오면, views의 index 함수를 실행시킨다.
       path('home/', views.index), 
   ]
   ```



1. view 설정

   ```python
   # home/views.py
   from django.shortcuts import render, HttpResponse
   
   # Create your views here.
   def index(request):
       print(request)
       print(type(request))
       print(request.META)
       return HttpResponse('hello, django!!')
   ```

   - 주의할 점은 선언된 함수에서 `request`를 인자로 받아야 한다.
     - request는 사용자(클라이언트)의 요청 정보와 서버에 대한 정보가 담겨있다.
     - Django 내부에서 해당 함수를 호출하면서 정보를 넘겨주기 때문에 반드시 명시해줘야한다.



## 3. Template (MTV - T)

> Django에서 활용되는 Template는 DTL(Django Template Language)이다.
>
> jinja2와 문법이 유사하다.

1. 요청 url 설정

   ```python
   path('home/dinner/', views.dinner)
   ```

2. view 설정

   ```python
   def dinner(request):
       box = ['치킨', '밥', '피자']
       dinners = random.choice(box)
       return render(request, 'dinner.html', {'dinners': dinners})
   ```

   - Template을 리턴하려면, `render`를 사용하여야 한다.
     - `request`(필수)
     - `template 파일 이름`(필수)
     - `template 변수`(선택) : 반드시 `dictionary`타입으로 구성해야 한다.



1. Template 설정

   ```bash
   $ mkdir home/templates
   $ touch home/templates/dinner.html
   ```

   ```html
   <!-- home/templates/dinner.html -->
   <h1> {{ dinner }} </h1>
   ```

![image_from_ios](https://user-images.githubusercontent.com/44271206/52547094-1ea11500-2e08-11e9-8997-f73a528a7562.jpg)



## 4. Variable Routing

1. url 설정

   ```python
   path('home/you/<name>', views.you),
   path('home/cube/<int:num>', views.cube)
   ```

   

2. view 파일 설정

   ```python
   def you(request, name):
   	return render(request, 'you.html', {'name':name})
   ```

   

3. 템플릿 파일 설정

   ```django
   <h1> {{ name }}, 안녕..? </h1>
   ```



## 5. Form data

1. `ping`

   1. 요청 url 설정

      ```python
      path('home/ping/', views.ping)
      ```

   2. view 설정

      ```python
      def ping(request):
          return render(request, 'ping.html')
      ```

   3. template 설정

      ```django
      <form action='/home/pong/'>
          <input name='message' type='text'>
          <input type='submit'>
      </form>
      ```

2. `pong`

   1. 요청 url 설정

      ```python
      path('home/pong/', views.pong)
      ```

   2. view 설정

      ```python
      def pong(request):
      	message = request.GET.get('message')
      	return render(request, 'pong.html', {'message':message})
      ```

   3. template 설정

      ```django
      <h1>{{message}}</h1>
      ```

3. POST 요청 처리

   1. 요청 url 설정

      ```django
      <form action="/home/pong/" method="POST">
      	{% csrf_token %}
      	 	  
      </form>
      ```

   2. view 설정

      ```python
      def pong(request):
          message = request.POST.get('message')
      ```

   - `csrf_token` 은 보안을 위해 django에서 기본적으로 설정되어 있는 것이다.
     - CSRF 공격: Cross Site Request Forgery
     - form을 통해 POST요청을 보낸다는 것은 데이터베이스에 반영되는 경우가 대부분인데, 해당 요청을 우리가 만든 정해진 form에서 보내는지 검증하는 것.
     - 실제로 input type hidden으로 특정한 hash값이 담겨 있는 것을 볼 수 있다.
     - `settings.py`에 `MIDDLEWARE`설정에 보면 csrf 관련된 내용이 설정된 것을 볼 수 있다.



## 6. static file 관리

> 정적 파일(images, css, js)을 서버 저장이 되어 있을 때, 이를 각각의 템플릿에 불러오는 방법

### 디렉토리 구조

디렉토리 구조는 `home/static/home/`으로 구성된다. 

이 디렉토리 설정은 `setting.py`의 가장 하단에 `STATIC_URL`에 맞춰서 해야한다. (기본 `/static/`)

1. 파일 생성

   `home/static/home/images/1.jp`

   `home/static/home/stylesheets/style.css`

2. 템플릿 활용

   ```django
   {% extends 'base.html' %}
   {% load static %}
   {% block css %}
   <link rel="stylesheets" type="text/css" href="{% static 'home/stylesheets/style.css' %}">
   {% endblock %}
   {% block body %}
   <imag src="{% static 'home/images/1.jpg' %}">
   {% endblock %}
   ```



## 7. URL 설정 분리

> 지금과 같은 코드를 짜는 경우에, `django_intro/urls.py`에 모든 url정보가 담기게 된다.
>
> 일반적으로 Django 어플리케이션에서 url을 설정하는 방법은 app 별로 `urls.py`를 구성하는 것이다.



1. `django_intro/urls.py`

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('home/', include('home.urls')),
   ]
   ```

   - `include`를 통해 `app/urls.py`에 설정된 url을 포함한다.

2. `home/urls.py`

   ```python
   from django.urls import path
   # view는 home/views.py
   from . import views
   urlpatterns = [
       path('', views.index)
   ]
   ```

   - `home/views.py`파일에서 `index`를 호출하는 url은 `https://<host>/`이 아니라, 

     `https://<host>/home/`이다.

   

## 8. Template 폴더 설정

### 디렉토리 구조

   디렉토리 구조는 `home/templates/home/`으로 구성된다.

   디렉토리 설정은 `settings.py`의 `TEMPLATES`에 다음과 같이 되어 있다.

```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
```

- `DIRS`: template를 커스텀하여 경로를 설정할 수 있다.

  - 경로 설정

    ```python
    os.path.join(BASE_DIR, 'django_intro', 'templates')
    #=> PROJECT/django_intro/templates/ 
    ```

- `APP_DIRS` : `INSTALLED_APPS`에 설정된 app의 디렉토리에 있는 `templates`를 템플릿으로 활용한다. (TRUE)



1. 활용 예시

   ```python
   # home/views.py
   def index(request):
       return render(request, 'home/index.html')
   ```

   ```python
   home
   ├── __init__.py
   ├── admin.py
   ├── apps.py
   ├── migrations
   ├── models.py
   ├── templates
   │   └── home
   │       └── index.html
   ├── tests.py
   ├── urls.py
   └── views.py
   ```

   

   