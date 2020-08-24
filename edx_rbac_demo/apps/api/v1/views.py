# Create your views here.
from edx_rbac.mixins import PermissionRequiredMixin
from edx_rest_framework_extensions.auth.jwt.authentication import (
    JwtAuthentication,
)
from rest_framework import permissions, viewsets, serializers

from edx_rbac_demo.apps.core.models import User


class BaseViewSet(PermissionRequiredMixin, viewsets.ViewSet):
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
            'id', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff'
        ]


class UserViewSet(BaseViewSet, viewsets.ModelViewSet):
    """
    View set for getting/setting data about users.
    """
    queryset = User.objects.all().order_by('email')
    permission_required = 'demo.has_learner_access'
    serializer_class = UserSerializer

    def get_permission_object(self):
        """
        Retrieves the apporpriate object to use during edx-rbac's permission checks.

        This object is passed to the rule predicate(s).
        """
        #import pdb; pdb.set_trace()
        return self.get_object()
