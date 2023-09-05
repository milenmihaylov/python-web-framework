from os.path import join

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('templates_advanced.todos.urls')),
	path('pets/', include('resources.urls')),
	path('cbv/', include('cbv.urls')),
] + static(settings.MEDIA_URL, document_root=join(settings.MEDIA_ROOT))
# + static(settings.MEDIA_URL, document_root=join(settings.MEDIA_ROOT, 'public'))
