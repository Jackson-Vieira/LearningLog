
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

     # URLs users
    path('users/', include('users.urls', namespace='users')),

    # URLs learning_logs
    path('', include('learning_logs.urls', namespace='learning_logs')),

   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
	document_root=settings.MEDIA_ROOT,)