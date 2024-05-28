"""
URL configuration for amnesia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/bloqs/', views.BloqCreateViewSet.as_view(), name='bloqs'),
    path('api/bloqs/<uuid:bloqId>', views.BloqRetrieveUpdateViewSet.as_view(), name='bloqs_update'),
    path('api/lockers/', views.LockerCreateViewSet.as_view(), name='lockers'),
    path('api/lockers/<uuid:lockerId>', views.LockerRetrieveUpdateViewSet.as_view(), name='lockers_update'),
    path('api/rents/', views.RentCreateViewSet.as_view(), name='rents'),
    path('api/rents/<uuid:rentId>', views.RentRetrieveUpdateViewSet.as_view(), name='rents_update'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
