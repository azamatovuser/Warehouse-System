from rest_framework.views import APIView
from rest_framework.response import Response
from apps.product.models import Spare, Device
from rest_framework import generics, permissions

from apps.product.serializers import DeviceListSerializer, DeviceCreateSerializer, SpareCreateSerializer


class SpareListAPIView(APIView):
    def get(self, request):
        spares = Spare.objects.values('name').distinct()

        spare_list = []
        for spare in spares:
            spare_name = spare['name']
            spare_count = Spare.objects.filter(name=spare_name).count()
            spare_list.append(f"{spare_name} - {spare_count}")

        spare_list.sort()

        return Response(spare_list)


class DeviceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceListSerializer
    permission_classes = (permissions.AllowAny, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeviceListSerializer
        elif self.request.method == 'POST':
            return DeviceCreateSerializer


class DeviceDetailAPIView(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceListSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DeviceDeleteAPIView(generics.DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceListSerializer
    permission_classes = (permissions.IsAuthenticated, )


class SpareCreateAPIView(generics.CreateAPIView):
    queryset = Spare.objects.all()
    serializer_class = SpareCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class SpareDetailAPIView(generics.RetrieveAPIView):
    queryset = Spare.objects.all()
    serializer_class = SpareCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )


class SpareDeleteAPIView(generics.DestroyAPIView):
    queryset = Spare.objects.all()
    serializer_class = SpareCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )
