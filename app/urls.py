from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view

# from cars.views import cars_view, new_car_view, CarsView, NewCarView,


urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    # Assuming logout_view is defined in accounts/views.py
    path('logout/', logout_view, name='logout'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    # path('new_car/', NewCarView.as_view(), name='new_car'),
    # path('cars/', CarsView.as_view(), name='cars_list'),
    # path('cars/', cars_view, name='cars_list'),
    # path('new_car/', new_car_view, name='new_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
