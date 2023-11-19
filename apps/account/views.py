from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.account.permissions import IsOwnUserOrReadOnly
from apps.account.serializers import RegisterSerializer, LoginSerializer, AccountUpdateSerializer
from apps.account.models import Account


class AccountRegisterView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/register/
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        username = serializer.data.get('username')
        tokens = Account.objects.get(username=username).tokens
        user_data['tokens'] = tokens
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/login/
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)


class AccountRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    # http://127.0.0.1:8000/account/retrieve-update/<id>/
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()
    permission_classes = (IsOwnUserOrReadOnly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        query = self.get_object()
        if query:
            serializer = self.get_serializer(query)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'message': 'query did not exist'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response({'success': False, 'message': 'credentials is invalid'}, status=status.HTTP_404_NOT_FOUND)


class AccountListView(generics.ListAPIView):
    # http://127.0.0.1:8000/account/list/
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')

        q_condition = Q()
        if q:
            q_condition = Q(full_name__icontains=q) | Q(username__icontains=q)

        queryset = qs.filter(q_condition)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            serializer = self.get_serializer(queryset, many=True)
            count = queryset.count()
            return Response({'success': True, 'count': count, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'data': 'queryset does not match'}, status=status.HTTP_404_NOT_FOUND)