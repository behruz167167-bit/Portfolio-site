from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # Oddiy tashrif buyuruvchilar faqat ko'ra oladi (Read-Only).
    # Faqat Django admin paneliga kirgan foydalanuvchi ma'lumot qo'sha oladi yoki o'chira oladi.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]