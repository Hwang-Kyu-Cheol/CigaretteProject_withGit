import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signUp(request) :
  if request.method == "POST" :
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    
    user = User.objects.create_user(username=username, email=email, password=password1)
    return HttpResponseRedirect(reverse('Member_App:SUF'))
    
  return render(request, 'Member_App/signUp.html')
  

def idCheck(request) :
  input_id = request.GET.get('input_id')
  try :
    user = User.objects.get(username=input_id)
  except :
    user = None
  
  if user is None :
    response = "success"
  else :
    response = "fail"
  
  context = {'response' : response}
  return JsonResponse(context)
  

def signUpFinish(request) :
  return render(request, 'Member_App/signUpFinish.html')
  

def logIn(request) :
  redirect_url = request.GET.get('next')
  if(redirect_url is None or "Member" in redirect_url) :
    redirect_url = '/'
    
  if request.is_ajax() :
    input_username = request.POST.get('username')
    input_password = request.POST.get('password')
    user = auth.authenticate(request, username=input_username, password=input_password)
    
    if user is not None :
      response = "success"
      auth.login(request, user)
    else :
      response = "fail"
    
    context = {'response' : response, 'redirect_url' : redirect_url}
    return JsonResponse(context)
  
  context = {'redirect_url' : redirect_url}      
  return render(request, 'Member_App/logIn.html', context)
  

def logOut(request) :
  redirect_url = request.GET.get('next')
  if(redirect_url is None or "Member" in redirect_url) :
    redirect_url = '/'
    
  if request.user.is_authenticated :
    auth.logout(request)
    return HttpResponseRedirect(redirect_url)
    
  return HttpResponseRedirect(reverse('Main_App:RMP'))
