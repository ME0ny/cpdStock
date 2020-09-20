from django.shortcuts import render
from .models import Stuff
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Stuff
    template_name = 'search_results.html'
    def get_queryset(self): # новый
        query = self.request.GET
        queryM={}
        queryM['X']=int(query['X'])
        queryM['Y']=int(query['Y'])
        queryM['Z']=int(query['Z'])
        if(query['q']!=''):
            object_list = Stuff.objects.filter(
                Q(tittle__icontains=query['q']))
        elif(query['q']=='' and queryM['X']!=0 and queryM['Y']==0):
            object_list = Stuff.objects.filter(
                Q(position_X__icontains=queryM['X']))
        elif(query['q']=='' and queryM['X']!=0 and queryM['Y']!=0 and queryM['Z']==0):
            object_list = Stuff.objects.filter(
                Q(position_X__icontains=queryM['X'] & Q(position_Y__icontains=queryM['Y'])))
        elif(query['q']=='' and queryM['X']!=0 and queryM['Y']!=0 and queryM['Z']!=0):
            object_list = Stuff.objects.filter(
                Q(position_X__icontains=queryM['X'] & Q(position_Y__icontains=queryM['Y']) & Q(position_Z__icontains=queryM['Z'])))
        else:
            object_list = Stuff.objects.all()
        return object_list