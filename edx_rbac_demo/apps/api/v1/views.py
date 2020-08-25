# Create your views here.
from edx_rbac.decorators import permission_required as permission_required_
from edx_rbac.mixins import PermissionRequiredMixin
from edx_rest_framework_extensions.auth.jwt.authentication import (
    JwtAuthentication,
)
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from edx_rbac_demo.apps.core import constants
from edx_rbac_demo.apps.core.models import User


def get_user_by_pk(pk):
    return User.objects.get(pk=pk)


class BaseViewSet(PermissionRequiredMixin):
    """
    Base class for all view sets.
    """
    # Adding this means you'll have to have valid edX JWT cookies
    # loaded in your browser (if you make requests via the browser).
    # You have to make requests with the 'use-jwt-cookie' header to make this so.
    authentication_classes = [JwtAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff'
        ]


class UserViewSet(BaseViewSet, viewsets.ModelViewSet):
    """
    View set for getting/setting data about users.
    /api/v1/users/<pk>/
    """
    queryset = User.objects.all().order_by('email')
    permission_required = constants.ENTERPRISE_USER_READ_PERMISSION
    serializer_class = UserSerializer

    def get_permission_object(self):
        """
        Retrieves the apporpriate user object to use during edx-rbac's permission checks.

        This object is passed to the rule predicate(s).
        """
        # returns the User object with a primary key of the ``pk`` provided
        # in this request
        return self.get_object()

    @permission_required_(
        constants.ENTERPRISE_USER_WRITE_PERMISSION,
        fn=lambda request, pk: get_user_by_pk(pk)
    )
    @action(detail=True, methods=['get'])
    def get_password(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user)
        data = serializer.data
        data['password'] = 'taco'
        return Response(data, status=status.HTTP_200_OK)
