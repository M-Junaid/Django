from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Blog

# Triggered before saving a blog
@receiver(pre_save, sender=Blog)
def blog_pre_save(sender, instance, **kwargs):
    # Perform actions before saving the blog instance
    print(f"About to save blog: {instance.title}")


# Triggered after saving a blog
@receiver(post_save, sender=Blog)
def after_blog_save(sender, instance, created, **kwargs):
    if created:
        print(f"New blog created: {instance.title}")
    else:
        print(f"Blog updated: {instance.title}")
