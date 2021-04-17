from django.shortcuts import render
from .models import Project
# Create your views here.


def home_page(request):
    data = list(Project.objects.all().values())
    return render(request, 'root/home_page.html', {'data': data,'page_title':'Mashood - Portfolio'})


def fetch(request, projectname):
    data = Project.objects.get(url=projectname)

    data = [
        data.title,
        data.text1,data.image1,
        data.text2,data.image2,
        data.text3,data.image3,
        data.text4,data.image4,
        data.text5,data.image5,
        data.text6,data.image6,
        data.text7,data.image7,
        data.text8,data.image8 
    ]

    print(data)

    # all_data = list(Project.objects.all().values())
    return render(request, 'root/fetch.html', {'data': data})
