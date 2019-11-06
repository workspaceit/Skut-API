"""skut_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

from skut_api.scripts import seed_data
from users.urls import user_urls
from stands.urls import stand_urls
from scooter_categories.urls import scooter_category_urs
from scooter_models.urls import scooter_model_urs
from scooters.urls import scooter_urs
from locks.urls import lock_urs
from rides.urls import ride_urls
from notices.urls import notice_url
from settings.urls import setting_url
from transactions.urls import transaction_url
from notifications.urls import router as notification_route

from . import views

urlpatterns = [
    path('', views.index),
    path('api/oauth', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/users/', include(user_urls)),
    path('api/areas/', include('areas.urls')),
    path('api/stands/', include(stand_urls)),
    path('api/scooter-categories/', include(scooter_category_urs)),
    path('api/scooter-models/', include(scooter_model_urs)),
    path('api/scooters/', include(scooter_urs)),
    path('api/locks/', include(lock_urs)),
    path('api/notifications/', include(notification_route.urls)),
    path('api/rides/', include(ride_urls)),
    path('api/notices/', include(notice_url)),
    path('api/settings/', include(setting_url)),
    path('api/transactions/', include(transaction_url)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)

seed_data()
