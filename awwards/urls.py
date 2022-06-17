from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('accounts/Sign-Up/', views.UserRegistration, name='signup'),
    path('accounts/profile/<id>/',views.profile,name = 'profile'),
    path('accounts/profile-update/',views.edit_profile,name = 'editprofile'), 
    path('new/project', views.add_project, name='addProject'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)