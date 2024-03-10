from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('formrec/', views.formrec, name='formrec'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>', views.update, name="update"),
    path('upate/uprec/<int:id>', views.uprec, name='uprec'),
    path('cota/', views.cota, name='cota'),
    path('cota/add', views.add, name='add'),   
]
