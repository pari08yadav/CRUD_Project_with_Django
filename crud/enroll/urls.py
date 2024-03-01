from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.add_show, name="show"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('update/<int:id>/', views.update_data, name="update"),
]