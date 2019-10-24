from django.shortcuts import render
from . models import Notice ,Albums, Profile,FollowUser,MyPost,PostComment,PostLike,pictures
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import View
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
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.http import Http404

# def home(request):
#     return render(request,'students/index.html')
class HomeView(TemplateView):
    template_name = "students/index.html"

# ***************************************************************************** Profile *********************************************************************
class ProfileListView(ListView):
    model = Profile
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Profile.objects.filter(Q(name__icontains = si)|Q(phone_no__icontains = si)).order_by("-id")

@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["name","user","age","branch","skill","phone_no","pic","description","status","gender","address","current_job"] 

# @method_decorator(login_required, name="dispatch")
# class ProfileDetailView(DetailView):
#     model = Profile

def follow(req, pk):
    user = Profile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user, followed_by = req.user.profile)
    return HttpResponseRedirect(redirect_to="/students/profiles")

# ************************************************************************  End Profile *********************************************************************

# *************************************************************************** Post *********************************************************************

@method_decorator(login_required, name="dispatch")
class MyPostUpdateView(UpdateView):
    model = MyPost
    fields = ["pic","subject","msg"] 

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

# ***********************************************************************  End Post *********************************************************************

#  *********************************************************************** Gallery ********************************************************************

def memories(request):
    all_albums = Albums.objects.all()
    profile = Profile.objects.all()
    context = {'all_albums':all_albums,'profile':profile}
    return render(request,'students/memories.html',context)

def albumdetail(request,pk):
    try:
        albumpic = pictures.objects.get(pk=pk)
        context = {
            'pics':albumpic.pic
        }
    except pictures.DoesNotExist:
        raise Http404("Pictures doesnot exist")
    return render(request, 'students/albumdetail.html',context)

#************************************************************************ End Gallery***************************************************************************** 

#  ************************************************************************** Events **********************************************************************
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

@method_decorator(login_required, name="dispatch")
class NoticeDetailListView(DetailView):
    model = Notice

# ***************************************************************************** End Events *********************************************************************
def about(request):
    # if request.method == 'POST':
    #         message = request.POST['message']
    #         send_mail('contact form',
    #         message,
    #         request.user.email,
    #         ['admindatabase.123@gmail.com'],
    #         fail_silently = False)
    return render(request, 'students/about.html')
class LoginView(TemplateView):
    template_name = "registration/login.html"

class AboutView(TemplateView):
    template_name = "students/about.html"   

# def albumdetail(request,pk):
#     try:
#         albumpic = pictures.objects.get(pk=pk)
#         context = {
#             'pics':albumpic.pic
#         }
#     except pictures.DoesNotExist:
#         raise Http404("Pictures doesnot exist")
#     return render(request, 'students/albumdetail.html',context)
        
def profiledetailview(request,pk):
    mypost = MyPost.objects.all()
    profile = Profile.objects.get(pk=pk) 
    userpost = []
    for post in mypost:
        if str(profile.user) == str(post.uploaded_by):
            userpost.append(post)
    context = {
        'mypost':userpost,
        'profilepic':profile.pic,
        'profilename':profile.name,
        'profileusername':profile.user
        }
    return render(request,'students/profiledetail.html',context)









