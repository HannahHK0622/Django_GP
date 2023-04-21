"""GroupProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from AssetMgr.views import *

router = routers.DefaultRouter()
router.register('users', Userviewset)
router.register('cargo', CargoViewset)
router.register('inbound', InboundViewset)
router.register('outbound', OutboundViewset)
router.register('order', OrderViewset)
router.register('products', ProductsViewset)
router.register('pellet', PelletViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('AssetMgr.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

