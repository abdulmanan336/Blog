from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('blog',views.blog,name='blog'),
    path('search',views.search,name='search'),
    path('subscribe',views.subscribe,name='subscribe'),
    path('comment/<id>',views.comment,name='comment'),
    path('post/<id>',views.post,name='post'),
    path('author/<id>',views.author,name='author'),
    path('author/<id>',views.author,name='author'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
