""" API v1 URLs. """
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from edx_rbac_demo.apps.api.v1 import views


app_name = 'v1'
urlpatterns = []

router = DefaultRouter()  # pylint: disable=invalid-name
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns += router.urls
