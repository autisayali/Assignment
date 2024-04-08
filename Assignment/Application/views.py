from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Entry
from .models import Task
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User



def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user = authenticate(uname=uname, password=password)
        if user is not None:
            
            login(request, user)
           
            return redirect('create')
        else:
          
            messages.error(request, 'Invalid username or password.')

   
    return render(request, 'login.html')

def signup(request):

    if request.method=='POST':
       uname=request.POST.get('uname')
       email=request.POST['email']
       password=request.POST['password']    
    

       entry=Entry(uname=uname,email=email,password=password).save()
       
       return render(request,'login.html') 
    
    return render(request,'signup.html')
def create(request):
    return render(request,'create.html')

def send(request):
    if request.method=='POST':
        ID=request.POST['ID']
        Status=request.POST['Status']
        Division=request.POST['Division']
        Category=request.POST['Category']
        Priority=request.POST['Priority']
        Department=request.POST['Department']
        
        
        print(ID,Status,Division,Category,Priority,Department)

        Task(ID=ID,Status=Status,Division=Division,Category=Category,Priority=Priority,Department=Department).save()
      
    
    data=Task.objects.all()
    return render(request,'show.html',{'data':data})

def get(request):
    ID=request.POST['ID']
    Status=request.POST['Status']
    Division=request.POST['Division']
    Category=request.POST['Category']
    Priority=request.POST['Priority']
    Department=request.POST['Department']
        
    Task(ID=ID,Status=Status,Division=Division,Category=Category,Priority=Priority,Department=Department).objects.save()
    return render(request,'show.html')

def show(request):
   
    data=Task.objects.all()
    
    print(data)
    return render(request,'show.html',{'data': data})

def edit(request):
    ID = request.GET['ID']
    Status="Not Available"
    for data in Task.objects.filter(ID=ID):
        ID=data.ID
        Status=data.Status
        
    return render(request,"edit.html",{'ID':ID,'Status':Status})
 




def RecordEdited(request):
    if request.method == 'POST':
        
        ID=request.POST['ID']
        
        Status=request.POST['Status']
       
        Task.objects.filter(ID=ID).update(Status=Status)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

def delete_task(request):
    ID = request.GET['ID']
    Task.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")

def stat(request): 
    data = Task.objects.filter(Status='Running').values()
  
    context = {
        'data': data,
    }   
    return render(request,"stat.html",{'data':data})

# views.py

from django.shortcuts import render
from Application.models import Task,Entry

def dashboard(request):
    
    departments=['It','Comp','Mech','Auto']
    
    closed_tickets = Task.objects.filter(Status='Closed').count()
    
    
   
    
    total=Task.objects.count()
    clscnt=Task.objects.filter(Status='Closed').count()
    rncnt=Task.objects.filter(Status='Running').count()
    

    context = {
        'departments': departments,
        'total':total,
        'rncnt':rncnt,
        'clscnt':clscnt,
        
    }
    return render(request, 'dashboard.html',context)

    

def navbar(request):
    return render(request,'navbar.html')




