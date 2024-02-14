"""
URL configuration for mtag_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "MTAG Admin"
# Add the below line
admin.site.index_title = "MTAG  App"
from mtag_admin import settings
def trigger_error(request):
   division_by_zero = 1 / 0
   
urlpatterns = [
    path('admin/', include('massadmin.urls')),
    path('sentry-debug/', trigger_error),
    path("admin/", admin.site.urls),
    path("api/activities/", include("activities.urls")),
    path("api/servicemanagement/", include("servicemanagement.urls")),
    path("api/finance/", include("finance.urls")),
    path("api/ministries/", include("ministries.urls")),
    path("api/homepage/", include("homepage.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # imp for what you want to achieve.
