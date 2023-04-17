from rest_framework import generics, authentication, permissions
from member.serializers import MemberSerializer, TokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CreateMemberView(generics.CreateAPIView):
    serializer_class = MemberSerializer


class MemberAuthToken(ObtainAuthToken):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


# Used for read or update endpoints to represent a single model instance.
class MemberProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = MemberSerializer
    # May be used to specify the list of authentication classes that will apply to the schema endpoint. 
    # Defaults to settings.DEFAULT_AUTHENTICATION_CLASSES
    authentication_classes = [authentication.TokenAuthentication]

    # May be used to specify the list of permission classes that will apply to the schema endpoint.
    # Defaults to settings.DEFAULT_PERMISSION_CLASSES
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Returns an object instance that should be used for detail views.
        # Defaults to using the lookup_field parameter to filter the base queryset.
        return self.request.user
