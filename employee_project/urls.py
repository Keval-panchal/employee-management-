from django.urls import path 
from . import views
urlpatterns = [
    path('',views.Employee_add ),
    path('views/',views.Employee_view),
    path('delete/<int:id>',views.Employee_delete),
     path('update/<int:id>',views.Employee_update)
]