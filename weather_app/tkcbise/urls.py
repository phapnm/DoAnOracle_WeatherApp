from django.contrib import admin
from django.urls import path, include
from googlesearch import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('course/', include('googlesearch.urls'))
]
