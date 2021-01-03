from django.shortcuts import render, HttpResponse
from .models import Job
import requests

# Create your views here.

from bs4 import BeautifulSoup
import json


def get_jobs(request):
    

    url="https://opportunities.mindtree.com/ccubeAPI/getListOfAllJobs/14977/S"
    r=requests.get(url)
    htmlcontent=r.content
    soup=BeautifulSoup(htmlcontent,'html5lib')
    all_jobs=json.loads(soup.text)

    for j in all_jobs:


        jb=Job(j['id'],j['jobTitle'],j['location'])
        jb.save()


    
    return render(request,'mindtree_jobs.html',{'jobs':Job.objects.all()})


