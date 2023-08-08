from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

# For Contact
class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
# For Service
class Service(models.Model):
    ser_name = models.CharField(max_length=200,default='')
    ser_desc = models.CharField(max_length=1000,default='')
    ser_logo = models.FileField(upload_to="images", validators=[FileExtensionValidator(['pdf','svg','doc'])],default='')

    def __str__(self):
        return self.ser_name
    
# For Pricing and plans
class Pricing(models.Model):
    type = models.CharField(max_length=100)
    feature1 = models.CharField(max_length=100)
    feature2 = models.CharField(max_length=100)
    feature3 = models.CharField(max_length=100)
    feature4 = models.CharField(max_length=100)
    feature5 = models.CharField(max_length=100)
    feature6 = models.CharField(max_length=100)
    price = models.IntegerField()
    pic = models.FileField(upload_to="images",validators=[FileExtensionValidator(['pdf',"doc","svg"])])

    def __str__(self):
        return self.type

# For Testimonials
class Testmonial(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    avatar = models.FileField(upload_to="images", validators=[FileExtensionValidator(['pdf','svg','doc',"jpg"])])

    def __str__(self):
        return self.name
    
# For works section
class Work(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.FileField(upload_to="images", validators=[FileExtensionValidator(['pdf','svg','doc',"jpg"])])

    def __str__(self):
        return self.title
    
# For Blog Sections
class Blog(models.Model):
    header = models.CharField(max_length=200)
    like = models.IntegerField()
    comment = models.IntegerField()
    body = models.CharField(max_length=500)
    nav = models.CharField(max_length=100)
    photo = models.FileField(upload_to="images", validators=[FileExtensionValidator(['pdf','svg','doc',"jpg"])])

    def __str__(self):
        return self.header