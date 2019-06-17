from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def count(requset):
    text = requset.GET['text']
    result={}
    for i in text:
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    result = sorted(result.items(),key=lambda x:x[1], reverse=True)
    return render(requset, 'count.html',{'count_result':result})