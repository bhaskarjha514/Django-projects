from django.shortcuts import render
from students.models import Notice
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'students/index.html')
    
def about(request):
    return render(request,'students/about.html')

class NoticeListView(ListView):
    model = Notice

@method_decorator(login_required, name="dispatch")
class NoticeDetailListView(DetailView):
    model = Notice



# Create your views here.
