"""poll_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('search', poll_views.search_for, name='search'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('update_question/<poll_id>/', poll_views.update_question, name='update-question'),
    path('login/', include("django.contrib.auth.urls")),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('questions/', poll_views.questions, name='questions'),
    path('delete_question/<poll_id>/', poll_views.delete_question, name='delete-question'),
    path('members/profile/', poll_views.profile, name='profile'),




    
]