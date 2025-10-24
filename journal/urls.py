from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('journal/', views.daily_journal, name='daily_journal_today'),
    path('journal/<str:date_str>/', views.daily_journal, name='daily_journal'),
    path('manage/', views.manage_dodonts, name='manage_dodonts'),
    path('api/toggle-entry/', views.toggle_entry, name='toggle_entry'),
    path('api/add-dodont/', views.add_dodont, name='add_dodont'),
    path('api/delete-dodont/<int:dodont_id>/', views.delete_dodont, name='delete_dodont'),
    path('api/update-dodont/<int:dodont_id>/', views.update_dodont, name='update_dodont'),
    path('api/reorder-dodonts/', views.reorder_dodonts, name='reorder_dodonts'),
]

