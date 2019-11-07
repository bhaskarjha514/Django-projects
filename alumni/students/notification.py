# from django.shortcuts import render
# from . models import Notice , Profile,FollowUser,MyPost,PostComment,PostLike
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import UpdateView, CreateView
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q
# from django.views.generic.base import TemplateView
# from django.http.response import HttpResponseRedirect
# from django.views.generic.edit import DeleteView
# from django.shortcuts import redirect;
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import User

# newnotice = Notice.objects.values_list('subject', flat=True)
# allnotice = Notice.objects.values_list('subject', flat=True)
# length = 0 
# length+=1

# def newnotice(request):




# emails = User.objects.values_list('email' ,flat=True)
#         message = instance.subject
#         i=0
#         branchuser = Profile.objects.values_list('branch',flat=True)
#         for branches in branchuser:
#             if branches==instance.branch:
#                 emailid= emails[i]
#                 #loopof email
#                 send_mail('contact form',
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 [emailid],
#                 fail_silently = False)
#                 i+=1

emails=[10,20,30,40]
branches=["cse","me","civil","cse"]
i=0

for branch in branches:
    if branch=="cse":
        print(emails[i])
    i+=1