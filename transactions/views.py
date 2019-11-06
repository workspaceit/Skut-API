from rest_framework import viewsets
from transactions.models import Transaction
from transactions.trnasection_serializer import TransactionSerializer
from rest_framework import permissions


class TransactionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (TransactionPermission, )
