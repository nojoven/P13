from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from core.models import User


"""
@receiver(post_save, sender=User)
def email_after_user_registration(sender, instance, created, **kwargs):
    if created:
        # EmailAlert.objects.create(user=instance)
        pass

@receiver(post_save, sender=User)
def save_email_alert(sender, instance, **kwargs):
    #instance.emailalert.save()
    pass
    
@receiver(post_delete, sender=User)
def email_after_user_deletion(sender, instance, deleted, **kwargs):
    if deleted:
        # EmailAlert.objects.create(user=instance)
        pass

@receiver(post_delete, sender=User)
def deletion_email_alert(sender, instance, **kwargs):
    #instance.emailalert.save()
    pass

@receiver(post_delete, sender=User)
def email_after_account_deactivation(sender, instance, deactivated, **kwargs):
    if deactivated:
        # EmailAlert.objects.create(user=instance)
        pass

@receiver(post_save, sender=User)
def deactivation_email_alert(sender, instance, **kwargs):
    #instance.emailalert.save()
    pass

@receiver(post_save, sender=User)
def email_after_account_reactivation(sender, instance, reactivated, **kwargs):
    if reactivated:
        # EmailAlert.objects.create(user=instance)
        pass

@receiver(post_save, sender=User)
def reactivation_email_alert(sender, instance, **kwargs):
    #instance.emailalert.save()
    pass

"""