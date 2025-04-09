from django.urls import path
from registration import views

urlpatterns = [
    path('user/get', views.get_user, name='get_user'),
    path('user/create', views.create_user, name='create_user'),
    path('user/update', views.update_user, name='update_user'),
    path('user/delete', views.delete_user, name='delete_user'),
    path('user/getAll', views.get_all_users, name='get_all_users'),
]

# from django.contrib import admin
# from django.urls import path
# from registration import views  # change this if your app name is different

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.display, name='display'),
#     path('insert/', views.insert_view, name='insert'),
#     path('delete/<int:id>/', views.delete_view, name='delete'),
#     path('update/<int:id>/', views.update_view, name='update'),
# ]

