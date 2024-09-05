#--------------------# CREATE THE VIEWS #--------------------#
#USER INTERFACE TO BE SEEN

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from django.db.models import F
from rest_framework import filters, viewsets
from rest_framework.response import Response
from .models import SegEstrada
from .serializers import SegEstradaSerializer
from .perms import AdminOrAnon

#CREATE A FILTERING CLASS FOR USER SEARCH

class SegEstradaFilter(FilterSet):
    #Note: ID and Speed already part of the model, need to define the variable name for traffic intensity
    intensity = CharFilter(method='filter_intensity', label="Intensity") 

    class Meta:
        model = SegEstrada
        fields = ['id', 'speed', 'intensity']

    def filter_intensity(self, queryset, name, value):
        #Any type of writing I want, can be define in here (to be more user friendly)
        intensity_mapping = {
            'low': 'low',
            'l': 'low',
            'baixa': 'low',
            'medium': 'medium',
            'm': 'medium',
            'media': 'medium',
            'high': 'high',
            'h': 'high',
            'elevada': 'high'
        }

        #Make all the writing in lowercase so no confusion occurs
        normalized_value = intensity_mapping.get(value.lower())

        #And then filter by the speed
        if normalized_value == 'low':
            return queryset.filter(speed__gt=50)
        elif normalized_value == 'medium':
            return queryset.filter(speed__lte=50, speed__gt=20)
        elif normalized_value == 'high':
            return queryset.filter(speed__lte=20)
        else:
            #Empty set for invalid input
            return queryset.none()  

#CREATE THE CLASS FOR THE MODEL
class SegEstradaViewSet(viewsets.ModelViewSet):
    queryset = SegEstrada.objects.all()
    serializer_class = SegEstradaSerializer

    #Permissions followed by perms.py
    permission_classes = [AdminOrAnon]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = SegEstradaFilter

    def list(self, request, *args, **kwargs):
        #Start filtering
        queryset = self.filter_queryset(self.get_queryset())

        #User input any of such filters? Checking that
        used_filters = any(
            request.query_params.get(param) for param in ['id', 'speed', 'intensity']
        )
        
        ##Increment the view count of a road segment if searched and if is Anon
        if request.user.is_anonymous and used_filters:
            ids = queryset.values_list('id', flat=True)
            SegEstrada.objects.filter(id__in=ids).update(views_count=F('views_count') + 1)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

#--------------------# INITIAL PAGE, LOCALHOST:8000 #--------------------#

def initial_page(request):
    return render(request, 'initial_page.html')

#--------------------# ATTEMPT TO CREATE AN INTERACTIVE MAP #--------------------#

from django.shortcuts import render

def map_view(request):
    #Get the search request from the user
    segment_id = request.GET.get('id')
    speed = request.GET.get('speed')
    intensity = request.GET.get('intensity')

    #Make sure we have a empty dataset before searching, not to overload the map
    segments = []

    #Based onthe user search, retrive the data needed. Define the filters:
    filters = {}
    if segment_id:
        filters['id'] = segment_id
    if speed:
        filters['speed'] = speed
    if intensity:
        #Intensity -> Speed
        intensity_mapping = {
            'low': 50,
            'medium': (20, 50),
            'high': 20
        }
        #Just a convertion of Speed values to intensity "string" and classification
        if intensity in intensity_mapping:
            if intensity == 'medium':
                filters['speed__lte'] = 50
                filters['speed__gt'] = 20
            else:
                filters['speed__lte'] = intensity_mapping[intensity] if intensity == 'high' else None
                filters['speed__gt'] = intensity_mapping[intensity] if intensity == 'low' else None

    #Filter based on search
    if filters:
        queryset = SegEstrada.objects.filter(**filters)
        serializer = SegEstradaSerializer(queryset, many=True)
        segments = serializer.data

    #Upload the data to the .html file corresponding
    return render(request, 'segment_map.html', {'segments': segments, 'filters': {'id': segment_id, 'speed': speed, 'intensity': intensity}})
