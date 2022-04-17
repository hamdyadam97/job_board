from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import api
app_name='job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_detail'),
    path('api/jobs',api.job_list_api,name='job_list_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),
    path('api/v2/jobs',api.JobListApi.as_view(),name='Job_List_Api'),
    path('api/v2/jobs/<int:id>',api.JobDetailApi.as_view(),name='Job_Detail_Api'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
