from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

# إنشاء View لعمل تسجيل مستخدم جديد
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
