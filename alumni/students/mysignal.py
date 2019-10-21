from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . models import Notice,Memories, Profile
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg ):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=Notice)
# def save_profile(sender, instance, created, **kwarg ):
#     if created:
#         Memories.objects.create(image=instance)

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

        # for email in emails:
        #     send_mail(instance.subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [email],
        #     fail_silently = False)
        
# branchuser = Profile.objects.values_list('branch',flat=True)
        # message = instance.subject
        # msgbranch = instance.branch
        # for branches in branchuser:
        #     if branches == msgbranch:
        #         emailid= emails[i]
        #         send_mail('contact form',
        #         message,
        #         settings.EMAIL_HOST_USER,
        #         [emailid],
        #         fail_silently = False)
        #         i+=1
        
        # Profile.objects.create(user=instance)
        
# emails = User.objects.values_list('email', flat=True)
#         message = instance.subject
#         for email in emails:
#             send_mail('contact form',
#             message,
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently = False)

#   emails = User.objects.values_list('email', flat=True)
#         message = instance.msg
#         for email in emails:
#             send_mail(instance.subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently = False)
        