
from django.contrib import admin
from django.urls import path
from portfolioapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('components/', views.components, name = "component"),
    path('service/', views.service, name = "my_services"),
    path('contact/', views.contact, name = "contact_me"),
    path('price/', views.pricing, name="my_pricing"),
    path('test/', views.testmonial, name="testmonials"),
    path('work/', views.work, name="my_work"),
    path('blog/', views.blog, name="my_blogs"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
