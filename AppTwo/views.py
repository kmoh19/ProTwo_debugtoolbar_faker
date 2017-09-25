from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from .forms import User_form

# Create your views here.
def index(request):
    
    my_dic={'result':'Help Page'}
    
    return render(request,'AppTwo/index.html',context=my_dic)

def users(request):
    userlist=User.objects.order_by('last_name')
    my_dic={'result':userlist}
    return render(request,'AppTwo/users.html',context=my_dic)

def user_form_view(request):
    
    userform= User_form()
    
    if request.method=='POST':
        userform= User_form(request.POST)
    
        if userform.is_valid():
            userform.save(commit=True) #what does commit do?
            return HttpResponse('success')   #u can return a success page here?!!!
    
    my_dic={'form':userform}
    return render(request,'AppTwo/UserDetails.html',context=my_dic)
    