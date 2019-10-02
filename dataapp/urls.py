from django.urls import path
from . import views

app_name = 'dataapp'

urlpatterns = [
    path('', views.database_upload, name='database_upload'),
    # path('db/vis/', views.database_visual, name='database_visual'),
    path('crud/', views.UploadList.as_view(), name='upload_list'),
    path('crud/view/<int:pk>', views.UploadView.as_view(), name='upload_view'),
    path('crud/new', views.UploadCreate.as_view(), name='upload_new'),
    path('crud/edit/<int:pk>', views.UploadUpdate.as_view(), name='upload_edit'),
    path('crud/delete/<int:pk>', views.UploadDelete.as_view(), name='upload_delete'),
]