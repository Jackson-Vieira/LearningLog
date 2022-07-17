
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs learning_logs
    path('', include('learning_logs.urls', namespace='learning_logs')),
]
