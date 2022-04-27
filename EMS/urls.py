from django.urls import path
from .views import *
urlpatterns = [
    path('',Home,name='Home'),
    # path('page1', page1,name='page1'),
    path('Create',Create,name='Create'),
    path('Edit_Employee/<int:myid>',Edit_Employee,name='Edit_Employee'),
    path('delete_view/<int:myid>',delete_view,name='delete_view'),
    path('leave/<int:id>',leave,name='leave'),
    path('Employee_List',Employee_List,name='Employee_List'),
   
    
]