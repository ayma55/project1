
# Create your views here.
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shrtcuts import get_current_site
from django.urls import reverse
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).accss_token

        current_site = get_current_site(request)
        relativeLink = reverse('email-verify')

        email_boady = 'Hi' + user.username+'Use link below to verify your email \n'
        absurl = 'http\\' + current_site + relativeLink + "?token=" + str(token)
        data = {'email_boady':email_boady, 'email_subject':'verify you email' }
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

        class VerifyEmail(generics.GenericAPIView):
            def get(self):
                pass
