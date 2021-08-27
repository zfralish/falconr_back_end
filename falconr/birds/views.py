from rest_framework import viewsets
from rest_framework import permissions
from .models import Bird
from .serializers import BirdSerializer


class BirdViewSet(viewsets.ModelViewSet):

    queryset = Bird.objects.all()
    serializer_class = BirdSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.birds.all()
