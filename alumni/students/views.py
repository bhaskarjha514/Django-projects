from django.shortcuts import render
from . models import Notice , Profile,FollowUser,MyPost,PostComment,PostLike
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect;
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


# def home(request):
#     return render(request,'students/index.html')
class HomeView(TemplateView):
    template_name = "students/index.html"


class LoginView(TemplateView):
    template_name = "registration/login.html"

class AboutView(TemplateView):
    template_name = "students/about.html"   

def follow(req, pk):
    user = Profile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user, followed_by = req.user.profile)
    return HttpResponseRedirect(redirect_to="/students/profiles")
    
# class ProfileView(TemplateView):
#     template_name = "students/profile.html"

class NoticeListView(ListView):
    model = Notice
    
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(subject__icontains = si)|Q(msg__icontains = si)).order_by("-id")
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull=True)).filter(Q(subject__icontains = si)|Q(msg__icontains = si))   .order_by("-id")
        
def about(request):
    # users = User.objects.all().values_list('email')
    emails = User.objects.values_list('email', flat=True)
    for email in emails:
        if request.method == 'POST':
            message = request.POST['message']
            send_mail('contact form',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False)
    return render(request, 'students/about.html')
        
        
@method_decorator(login_required, name="dispatch")
class NoticeDetailListView(DetailView):
    model = Notice

@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["name","user","age","branch","skill","phone_no","pic","description","status","gender","address","current_job"]

@method_decorator(login_required, name="dispatch")
class MyPostCreate(CreateView):
    model = MyPost
    fields = ["subject","msg","pic"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.profile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name="dispatch")
class MyPostListView(ListView):
    model = MyPost
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MyPost.objects.filter(Q(uploaded_by=self.request.user.profile)).filter(Q(subject__icontains = si)|Q(msg__icontains = si)).order_by("-id")
        
@method_decorator(login_required, name="dispatch")
class MyPostDetailView(DetailView):
    model = MyPost

@method_decorator(login_required, name="dispatch")
class MyPostDeleteView(DeleteView):
    model = MyPost

class ProfileListView(ListView):
    model = Profile
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Profile.objects.filter(Q(name__icontains = si)|Q(phone_no__icontains = si)).order_by("-id")

@method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView):
    model = Profile