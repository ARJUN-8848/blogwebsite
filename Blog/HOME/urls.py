from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import force_logout_and_login

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<slug:slug>/", views.blog_detail, name='blog_detail'),  # Updated to include 'blog/'
    path("category/<slug:slug>/", views.category, name="category"),
    path('<slug:slug>/add_comment/',views.add_comment,name='add_comment'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name='contact'),
    path('login/', force_logout_and_login, name='force_login'),  # Force logout and redirect to login
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
