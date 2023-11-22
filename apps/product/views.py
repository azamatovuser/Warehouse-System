from rest_framework.views import APIView
from rest_framework.response import Response
from apps.product.models import Spare


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
