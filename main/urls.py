from django.urls import path
from .views import blog_view, main_view,contact_view

urlpatterns = [
    path('', main_view, name='landing'),
    path('contact/', contact_view, name='contact'),
    path('blog/', blog_view, name='blog'),

]
 