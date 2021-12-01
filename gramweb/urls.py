"""Imports URLS"""
from django.contrib import admin
from django.urls import path
from gramweb import views as local_views
from posts import views as posts_views
from users import views as users_views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('hello',local_views.hello,name="hello_word"),
    path('admin/', admin.site.urls ,name="admi"),

    path('posts/',posts_views.list_posts ,name='posts'),

    path('users/login/',users_views.login_view,name='login'),
    path('users/logout/',users_views.logout_view,name='logout'),
    path('users/signup/',users_views.signup_view,name='signup'),
    path('users/me/profile',users_views.update_profile,name='update_profile'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
