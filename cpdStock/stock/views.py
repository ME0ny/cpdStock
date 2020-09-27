from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from django.db.models import Q
from .models import Stuff
from .serializers import SearchResultsViewSerializer

# Create your views here.

'''class SearchResultsView(ListView):
    model = Stuff
    template_name = 'search_results.html'
    def get_queryset(self): # новый
        query = self.request.GET
        if(len(query)>0):
            queryM={}
            queryM['X']=int(query['X'])
            queryM['Y']=int(query['Y'])
            queryM['Z']=int(query['Z'])
            if(query['q']!='' and queryM['X']==0):
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
        return None
'''

class SearchResultsView(ListModelMixin, GenericAPIView):
    serializer_class = SearchResultsViewSerializer
    model = Stuff

    def get_queryset(self): # новый
        query = self.request.GET
        if(len(query)>0):
            queryM={}
            try:
                queryM['X']=int(query['X'])
                queryM['Y']=int(query['Y'])
                queryM['Z']=int(query['Z'])
                if(query['q']!='' and queryM['X']==0):
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
            except Exception as e:
                print(e)
                object_list = Stuff.objects.all()
            return object_list
        return None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)