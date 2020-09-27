from rest_framework import serializers
from .models import Stuff
class SearchResultsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('id','tittle','description','position_X','position_Y','position_Z','quantity')
    tittle = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    position_X = serializers.IntegerField()
    position_Y = serializers.IntegerField()
    position_Z = serializers.IntegerField()
    quantity = serializers.IntegerField()