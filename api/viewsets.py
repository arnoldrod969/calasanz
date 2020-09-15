from rest_framework import viewsets, permissions
from .models import Nature, Region, Pays, Document
from .serializers import *


class NatureViewset(viewsets.ModelViewSet):
    queryset = Nature.objects.all()
    serializer_class = NatureSerializer


class RegionViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class PaysViewset(viewsets.ModelViewSet):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

