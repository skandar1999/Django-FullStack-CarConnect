from django.urls import path
from .views import blog_view, home_view, contact_view, list_view, listing_detail
from uuid import UUID

urlpatterns = [
    path('', home_view, name='landing'), 
    path('contact/', contact_view, name='contact'), 
    path('blog/', blog_view, name='blog'),  
    path('list/', list_view, name='list'), 
    path('listing/<uuid:listing_id>/', listing_detail, name='listing_detail'), 
    
]
