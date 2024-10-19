from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserLocation
from .serializers import UserLocationSerializer
from rest_framework.decorators import authentication_classes, action
from django.db.models import OuterRef, Subquery
from ..company.models import Company


class UserLocationModelViewSet(viewsets.ModelViewSet):
    latest_location = UserLocation.objects.filter(
        user = OuterRef("user")
    ).order_by("-timestamp")

    queryset = UserLocation.objects.filter(
        id = Subquery(latest_location.values("id")[:1])
    )

    serializer_class = UserLocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, company=Company.objects.filter(id=self.request.data['company']).first())


    # def list(self, request, *args, **kwargs):
    #     queryset =


 # "timestamp": "2024-10-18T02:28:02.344154Z",
# "timestamp": "2024-10-19T03:08:27.557709Z",