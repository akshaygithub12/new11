from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hellow woweopw")


def akshay(request):
    return HttpResponse("hello dsakdkdajas")



def vishal(request):
    return HttpResponse("hello dsakdkdajas")


def newname(request,name):
    return render(request,"home\greet.html",{"name":name})

def index(request):
    return render(request,"home\index.html")
texts=["sdasdasdsa sadas sd asd asdsad asdas d","Sdasdsadsad sad asd asdas sa das","DSadsad asdsa sadsa"]
       def section(request,num):
           if 1<=num<=3:
               return HttpResponse(texts[num-1])
            else:
                raise http404("no such a page")
            
 


