from .models import Resident
from rest_framework import viewsets
from .serializers import ResidentSerializer
from .decos import check_list


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    @check_list
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
