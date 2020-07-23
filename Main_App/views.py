from django.shortcuts import render

# Create your views here.
def readMainPage(request) :
  return render(request, 'Main_App/readMainPage.html')
