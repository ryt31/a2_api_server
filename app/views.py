from rest_framework import viewsets
from .models import UserInfo
from .serializer import UserInfoSerializer


# Create your views here.
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
