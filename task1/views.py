from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

task=['sdaasd','asdasd','asdasdas']

class NewTaskForm(forms.Form):
    task = forms.CharField(label="new task")
    priority= forms.IntegerField(label="Prior", min_value=1,max_value=11)
def index(request):
    return render(request,'index/task1.html',{"task":task})


def add(request):
    if request.method=="post":
        form=NewTaskForm(request.post)
        if form.is_valid():
            task=form.cleaned_data["task"]
            task.append(task)
        else:
            return render(request,"index/add.html",{
                "form":form})
    return render(request,"index/add.html",
                  {"form":NewTaskForm()})
