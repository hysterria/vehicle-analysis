from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vehicles.urls')),
    path('calculator/', include('calculator.urls')),
    path('vehicle_simulation/', include('vehicle_simulation.urls', namespace='vehicle_simulation')),
    path('admin/', admin.site.urls),

]
