from django.shortcuts import render
from django.http import HttpResponse
import operator
from .models import chapter
from .models import topic
from .models import sub_topic

def index(request):
    return render(request,'study/index.html')
def business(request):
    # a=request.POST.get('answer')
    # b=request.POST.get('question')
    # quest=qa.objects.all()
    chapters=chapter.objects.all()
    topics=topic.objects.all()
    sub_topics=sub_topic.objects.all()
    chapters_no={}
    for i in chapters:
        a=i.id
        n=''
        for i in a:
            try:
                i=int(i)
                n=n+str(i)
            except Exception as e:
                i=str(i)
        chapters_no[a]=int(n)
    chapters_no=sorted(chapters_no.items(),key=operator.itemgetter(1))
    chapters_no_sorted={}
    for i,j in chapters_no :
            chapters_no_sorted[i]=j
    # print(chapters_no)
    # print(chapters_no_sorted)
    d={'chapters':chapters,'topics':topics,'sub_topics':sub_topics,'chapters_no':chapters_no_sorted}
    # form = qa(question=b,ans=a)
    # form.save()
    #={'Qust':quest}
    return render(request,'study/business.html',d)

def economic(request):
    # a=request.POST.get('answer')
    # b=request.POST.get('question')
    # quest=qa.objects.all()
    chapters=chapter.objects.all()
    topics=topic.objects.all()
    sub_topics=sub_topic.objects.all()
    chapters_no={}
    for i in chapters:
        a=i.id
        n=''
        for i in a:
            try:
                i=int(i)
                n=n+str(i)
            except Exception as e:
                i=str(i)
        chapters_no[a]=int(n)
    chapters_no=sorted(chapters_no.items(),key=operator.itemgetter(1))
    chapters_no_sorted={}
    for i,j in chapters_no :
            chapters_no_sorted[i]=j
    #pri(chapters_no)
    #print(chapters_no_sorted)
    d={'chapters':chapters,'topics':topics,'sub_topics':sub_topics,'chapters_no':chapters_no_sorted}
    # form = qa(question=b,ans=a)
    # form.save()
    #={'Qust':quest}
    return render(request,'study/economic.html',d)

def account(request):
    # a=request.POST.get('answer')
    # b=request.POST.get('question')
    # quest=qa.objects.all()
    chapters=chapter.objects.all()
    topics=topic.objects.all()
    sub_topics=sub_topic.objects.all()
    chapters_no={}
    for i in chapters:
        a=i.id
        n=''
        for i in a:
            try:
                i=int(i)
                n=n+str(i)
            except Exception as e:
                i=str(i)
        chapters_no[a]=int(n)
    chapters_no=sorted(chapters_no.items(),key=operator.itemgetter(1))
    chapters_no_sorted={}
    for i,j in chapters_no :
            chapters_no_sorted[i]=j
    #print(chapters_no)
    #print(chapters_no_sorted)
    d={'chapters':chapters,'topics':topics,'sub_topics':sub_topics,'chapters_no':chapters_no_sorted}
    return render(request,'study/account.html',d)
def cs(request):
    # a=request.POST.get('answer')
    # b=request.POST.get('question')
    # quest=qa.objects.all()
    chapters=chapter.objects.all()
    topics=topic.objects.all()
    sub_topics=sub_topic.objects.all()
    chapters_no={}
    for i in chapters:
        a=i.id
        n=''
        for i in a:
            try:
                i=int(i)
                n=n+str(i)
            except Exception as e:
                i=str(i)
        chapters_no[a]=int(n)
    chapters_no=sorted(chapters_no.items(),key=operator.itemgetter(1))
    chapters_no_sorted={}
    for i,j in chapters_no :
            chapters_no_sorted[i]=j
    #print(chapters_no)
    #print(chapters_no_sorted)
    d={'chapters':chapters,'topics':topics,'sub_topics':sub_topics,'chapters_no':chapters_no_sorted}
    # form = qa(question=b,ans=a)
    # form.save()
    #={'Qust':quest}
    return render(request,'study/cs.html',d)

# Create your views here.
def secret(request):
    a=request.GET.get('message')
    b={'text':a}
    # b=request.POST.get('question')
    # quest=qa.objects.all()
    # form = qa(question=b,ans=a)
    # form.save()
    #={'Qust':quest}
    print(a)
    return render(request,'study/secret.html',b)
def todo(request):
    return render(request,'study/mytodo.html')
