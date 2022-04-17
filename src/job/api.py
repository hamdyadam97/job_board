from rest_framework import generics

from .models import job
from .serializers import JobSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

## views

@api_view(['GET'])
def job_list_api(request):
    all_job = job.objects.all()
    data = JobSerializers(all_job,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = job.objects.get(id=id)
    data = JobSerializers(job_detail).data
    return Response({'data':data})


class JobListApi(generics.ListAPIView):
    queryset =  job.objects.all()
    serializer_class = JobSerializers


class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializers
    lookup_field = 'id'


