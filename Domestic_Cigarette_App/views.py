from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, resolve_url
from Domestic_Cigarette_App.models import Domestic_Cigarette, Domestic_Cigarette_Category, Domestic_Cigarette_Comment
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.
def readCigaretteAll(request) :
  category_query_set = Domestic_Cigarette_Category.objects.all()
  list_query_set = Domestic_Cigarette.objects.all()
    
  context = {'cigarette_category' : category_query_set, 'cigarette_list' : list_query_set}
  return render(request, 'Domestic_Cigarette_App/readCigaretteAll.html', context)
  
  
def readCigaretteCategory(request, category) :
  selected_category = category
  category_query_set = Domestic_Cigarette_Category.objects.all()
  list_query_set = Domestic_Cigarette.objects.filter(Category=category)
  
  context = {'selected_category' : selected_category, 'cigarette_category' : category_query_set, 'cigarette_list' : list_query_set}
  return render(request, 'Domestic_Cigarette_App/readCigaretteCategory.html', context)
  
  
def readCigaretteDetail(request, name) :
  item_query_set = Domestic_Cigarette.objects.get(Name=name)
  
  context = {'selected_item' : item_query_set}
  return render(request, 'Domestic_Cigarette_App/readCigaretteDetail.html', context)
  

@login_required 
def createNewComment(request, item_pk) :
  if request.method == "POST" :
    Nickname_pk = int(request.POST.get('Nickname'))
    
    Object = get_object_or_404(Domestic_Cigarette, pk=item_pk)
    Nickname = get_object_or_404(get_user_model(), pk=Nickname_pk)
    Content = request.POST.get('Content')
    StarPoint = request.POST.get('StarPoint')
  
    Domestic_Cigarette_Comment.objects.create(Object=Object, Nickname=Nickname, Content=Content, StarPoint=StarPoint)
    StarPoint = int(StarPoint)
    Object.StarPointUpdate(StarPoint)
    
  return HttpResponseRedirect(resolve_url(Object))
  
  
@login_required
def deleteComment(request, item_pk) :
  Comment = get_object_or_404(Domestic_Cigarette_Comment, pk=item_pk)
  Object = Comment.Object
  
  if Comment.Nickname.username == request.user.username :
    StarPoint = Comment.StarPoint
    Object.StarPointDelete(StarPoint)
    Comment.delete()
    
  return HttpResponseRedirect(resolve_url(Object))
