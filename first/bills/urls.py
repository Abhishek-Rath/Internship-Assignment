from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'invoice', views.InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('detail/<str:pk>/', views.itemDetail, name = 'detail'),
    # path("", views.itemList, name = "items"),
    path('generate_invoice/', views.generate_invoice),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('create', views.create, name ='create'),
    # path('update/<str:pk>', views.itemUpdate, name ='update'),
]