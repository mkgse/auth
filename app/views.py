from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import User

# Create your views here.
def login_form(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
    form = LoginForm(request=request, data=request.POST)
    if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user =  authenticate(username=uname,password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Congratulations!! You have Succsessfuly Loged In')
        return HttpResponseRedirect('/dashboard')
  else:
      form = LoginForm()
  return render(request,'app/login.html',{'form':form })
 else:
      return HttpResponseRedirect('/dashboard')
 

def signup(request):
    if request.method == "POST":
     fm = SignUpForm(request.POST)
     if fm.is_valid():
       messages.success(request, 'Congratulations!! You have Succsessfuly Registerd')
                
       user = fm.save()
       fm = SignUpForm()
       return HttpResponseRedirect('/login')
    else:
     fm = SignUpForm()
    return render(request,"app/signup.html",{'form':fm})

def dashbaord(request):
    if request.user.is_authenticated:
       if request.method=='POST':
          pass
       else:
         user = request.user
         print(user)
         form = User.objects.filter(username=user)
    return render(request,'app/dashboard.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

