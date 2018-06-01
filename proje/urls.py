from django.conf.urls import url, include
# routers çağırdık, url işlemlerini yürütücek.
from rest_framework import routers
# wp benim uygulamamım adıdır.
# views içindeki iki adet fonksiyonu çağırıdık.
from .views import UserViewSet,GroupViewSet
router = routers.DefaultRouter()
# /user/ ve /groups/ adlı iki url oluşturduk.
# Bu urller çalışınca, belirtilmiş fonksiyonlar çalışacak.
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
# API Ana sayfası Sayfası
url(r'^', include(router.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]