from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='job'
urlpatterns = [
    path('',views.send_message,name='contact'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
