from django.shortcuts import render,get_object_or_404
from . models import Category,Events
# Create your views here.


def event_list(request):
    events = Events.objects.all()
    categories = Category.objects.all()
    return render(request,'events_list.html',{'events':events,'categories':categories})
    
def category_events(request,id):
    category = get_object_or_404(Category,id=id)
    events = Events.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request,'events_list.html',{'events':events,'categories':categories,'selected_category':category})
