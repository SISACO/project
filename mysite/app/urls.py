from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
  
  path('',views.index,name='home'),
  
  path('member/',views.member,name='member'), 
  
  path('activities/',views.activities,name='activities'), 
  
  path('alumni/', views.alumni_list, name='alumni_list'),
  
  path('alumni/<str:department>/', views.alumni_list_department, name='alumni_list_department'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)