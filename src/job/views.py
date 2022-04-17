from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import job, Apply
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
from .filters import JobFilter
# Create your views here.

def job_list(request):
    job_list = job.objects.all()
    my_filter = JobFilter(request.GET,queryset=job_list)
    job_list = my_filter.qs
    paginator = Paginator(job_list,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj,'my_filter':my_filter}
    return render(request,'job/jobs.html',context)


def job_detail(request,slug):
    job_detail = job.objects.get(slug=slug)
    if request.method =='POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()

    else:
        form = ApplyForm()
    context ={'job_detail':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)

@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit= False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse("jobs:add_job"))
    else:
        form = JobForm()
    context = {"form":form}
    return render(request,"job/add_job.html",context)
