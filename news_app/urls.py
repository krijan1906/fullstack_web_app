from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.Register,name='register'),
    path('',views.Login,name='login'),
    path('news/',views.Inputs,name='news'),
    path('home/',views.Front,name='front'),
    path('delete/<int:Id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update,name='update'),
    

    
]
if settings.DEBUG:
    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)