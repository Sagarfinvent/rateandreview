
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.add_comment, name="addandshow"),
]
