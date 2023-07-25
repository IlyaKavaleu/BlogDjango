from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('sections/', views.sections, name='sections'),
    path('sections/<int:section_id>/', views.section, name='section'),
    path('new_section/', views.new_section, name='new_section'),
    path('new_model/<int:section_id>/', views.new_model, name='new_model'),
    path('edit_section/<int:section_id>/', views.edit_section, name='edit_section'),
    path('edit_model/<int:model_id>/', views.edit_model, name='edit_model'),
    path('delete_section/<int:section_id>/', views.delete_section, name='delete_section'),
    path('delete_model/<int:model_id>/', views.delete_model, name='delete_model'),
    path('section/<int:model_id>/', views.model, name='model'),
]
