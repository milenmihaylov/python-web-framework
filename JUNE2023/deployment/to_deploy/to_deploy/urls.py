from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('to_deploy.app.urls')),
]


"""
#For deployment:
1. Package application in Docker image
2. Push docker image into Docker hub
3. Pull docker image on the server
4. Start application sing the new image on the server
"""
