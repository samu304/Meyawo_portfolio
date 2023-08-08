from django.contrib import admin

# Register your models here.
admin.site.site_header = "My Portfolio"

# username: Samundra
# password: samu@123


from .models import Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display= ["name","email","message"]

from .models import Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display =["ser_name","ser_desc","ser_logo"]

from .models import Pricing
@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display =['type','feature1','feature2','feature3','feature4','feature5','feature6','price','pic']

from .models import Testmonial
@admin.register(Testmonial)
class TestmonialAdmin(admin.ModelAdmin):
    list_display = ['name',"comment","avatar"]

from .models import Work
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ["title","category","img"]

from .models import Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display =['header','like','comment','body','nav','photo']