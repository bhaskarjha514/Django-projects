from django.shortcuts import render
from students.models import Notice
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def home(request):
    return render(request,'students/index.html')
    
def about(request):
    return render(request,'students/about.html')

class NoticeListView(ListView):
    model = Notice

class NoticeDetailListView(DetailView):
    model = Notice



# Create your views here.
