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
        query = self.request.GET.get('q')
        object_list = Stuff.objects.filter(
            Q(tittle__icontains=query) | Q(position_Z__icontains=query)
        )
        return object_list