
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_app.urls')),
    path('pets', include('pets.urls')),
    path('new/', include('todos.urls'))
]
