from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('accounts/Sign-Up/', views.UserRegistration, name='signup'),
    path('accounts/profile/<id>/',views.profile,name = 'profile'),
    path('accounts/profile-update/',views.edit_profile,name = 'editprofile'), 
    path('newproject', views.add_project, name='addProject'),
    path('projects/<id>/',views.projects,name = 'projects'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('rate/<id>/',views.ratings,name = 'rate'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)