from django.urls import path
from . views import home, about, contact, blog_grid, blog_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog_grid, name='blog'),
    path('blogd/', blog_detail, name='blog_detail'),
]
