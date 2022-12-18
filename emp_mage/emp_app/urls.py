from django.urls import path,include
from emp_app import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('add_emp', views.add_emp,name='add_emp'),
    path('rem_emp', views.rem_emp,name='rem_emp'),
    path('remove_emp/<int:emp_id>/', views.rem_emp,name='rem_emp'),
    path('flt_emp', views.flt_emp,name='flt_emp'),
    
]
