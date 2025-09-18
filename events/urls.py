from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.event_list,name='event_list'),
    path('category/<int:id>',views.category_events,name='category_events'),
    
]
