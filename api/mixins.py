from rest_framework import permissions

from .permissions import IsProductEditorPermission

class ProductEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsProductEditorPermission]