from rest_framework import viewsets
from .models import Information
from .serializer import InformationSerializer


# Create your views here.
class InformationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
