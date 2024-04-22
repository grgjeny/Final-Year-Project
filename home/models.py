from django.db import models
from django.utils import timezone
import shutil
import os
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_delete

class ProductsType(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    image = models.ImageField(upload_to='products/photos/', null=False)
    upload_path = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk: 
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            self.upload_path = f'products/{self.name}_{timestamp}/'
            upload_path = f'products/{self.name}_{timestamp}/'
            self.image.field.upload_to = upload_path
        super().save(*args, **kwargs)

@receiver(post_delete, sender=ProductsType)
def delete_ProductsType_directory(sender, instance, **kwargs):
    upload_path = 'media/' + instance.upload_path
    try:
        shutil.rmtree(upload_path)
        print(f"Folder {upload_path} successfully deleted.")
    except OSError as e:
        print(f"Error: {upload_path} : {e.strerror}")

class Products(models.Model):
    ProductsType = models.ForeignKey(ProductsType, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, blank=False, unique=True)
    Price = models.FloatField(null=False)
    image = models.ImageField(upload_to="products/images/", null=False)
    description = models.TextField(null=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.Name
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Products.objects.get(pk=self.pk)
            if old_image.image != self.image or old_image.ProductsType != self.ProductsType:
                self.image.field.upload_to = self.ProductsType.upload_path
                if os.path.exists(old_image.image.path):
                    new_image_path = self.ProductsType.upload_path(os.path.basename(old_image.image.path))
                    shutil.move(old_image.image.path, new_image_path)
        else:
            self.image.field.upload_to = self.ProductsType.upload_path
        super().save(*args, **kwargs)

def wrapper(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext) 
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('events/to/photos/', filename)    

def newswrapper(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext) 
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('news/to/photos/', filename)    

class Events(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    location = models.CharField(max_length=50, blank=False)
    Description = models.TextField(blank=False)
    image = models.ImageField(upload_to=wrapper, null=False)
    Event_Start_Date = models.DateField(default=timezone.now)
    Event_End_Date = models.DateField(default=timezone.now)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.name

class newsBlog(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(max_length=200, null=False)
    image = models.ImageField(upload_to=newswrapper, blank=False)
    date = models.DateField(default=timezone.now, editable=False)

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    message = models.TextField(max_length=250)
    subject = models.TextField(max_length=250)
    created_at = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question
