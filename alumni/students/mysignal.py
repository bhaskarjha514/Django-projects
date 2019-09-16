from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . models import Notice
from students.models import Profile
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg ):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Notice)
def sendmail(sender, instance, created, **kwarg ):
    if created:
        emails = User.objects.values_list('email', flat=True)
        message = instance.msg
        for email in emails:
            send_mail(instance.subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False)

#@receiver(post_save, sender=Notice)
#def sendmail(sender, instance, created, **kwarg ):
   # if created:
        #emails = User.objects.values_list('email', flat=True)
       # branches = Profile.objects.values_list('branch', flat=True)
        #message = instance.msg
        #i=0
        #some=instance.branch
        #for branch in branches:
            #if branch == some:
               # emailid= emails[i]
                #send_mail(instance.subject,
              #  message,
               # settings.EMAIL_HOST_USER,
               # [emailid],
                #fail_silently = False)
           # i+=1    
        # Profile.objects.create(user=instance)
        
