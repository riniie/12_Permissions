from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
    DjangoObjectPermissions
)
from .models import Student
from .serializers import StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
