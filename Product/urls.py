from django.conf.urls import url
from django.urls import path, include
from .views import product_list, product_detail,GenericAPIView,ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',ProductViewSet,basename="products")
urlpatterns = [
    url(r'^products/$', product_list),
    url(r'^products/(?P<pk>[0-9]+)$', product_detail),
    path('generic/products/<int:id>/', GenericAPIView.as_view()),
]