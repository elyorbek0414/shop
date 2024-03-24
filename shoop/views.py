from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mahsulot, Buyurtma, Chegirma
from .serializers import MahsulotSerializer, BuyurtmaSerializer


class MahsulotListCreate(APIView):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.all()
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MahsulotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MahsulotRetrieveUpdateDestroy(APIView):
    def get_object(self, poc):
        try:
            return Mahsulot.objects.get(poc=poc)
        except Mahsulot.DoesNotExist:
            raise Http404

    def get(self, request, poc):
        mahsulot = self.get_object(poc)
        serializer = MahsulotSerializer(mahsulot)
        return Response(serializer.data)

    def put(self, request, poc):
        mahsulot = self.get_object(poc)
        serializer = MahsulotSerializer(mahsulot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, poc):
        mahsulot = self.get_object(poc)
        mahsulot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChegirmaListCreate(APIView):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.filter(chegirma_foizi__isnull=False)
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)


class BuyurtmaListCreate(APIView):
    def post(self, request):
        data = request.data
        mahsulot_id = data.get('mahsulot')
        miqdori = data.get('miqdori')

        if mahsulot_id:
            try:
                mahsulot = Mahsulot.objects.get(poc=mahsulot_id)
            except Mahsulot.DoesNotExist:
                return Response({"error": "Mahsulot not found"}, status=status.HTTP_404_NOT_FOUND)

            chegirma_foizi = mahsulot.chegirma_foizi
            chegirma_muddati = mahsulot.chegirma_muddati
        else:
            chegirma_foizi = data.get('chegirma_foizi', None)
            chegirma_muddati = data.get('chegirma_muddati', None)

        summa = mahsulot.narxi * miqdori

        chegirma = None
        if chegirma_foizi is not None and chegirma_muddati is not None:
            try:
                chegirma = Chegirma.objects.get(mahsulot=mahsulot, chegirma_foizi=chegirma_foizi, chegirma_muddati=chegirma_muddati)
            except Chegirma.DoesNotExist:
                pass

        if chegirma:
            chegirma_miqdori = chegirma.chegirma_foizi * summa / 100
            summa -= chegirma_miqdori

        buyurtma = Buyurtma.objects.create(
            mahsulot=mahsulot,
            miqdori=miqdori,
            chegirma_foizi=chegirma_foizi,
            chegirma_muddati=chegirma_muddati,
            summa=summa,
            qabul_sana=data.get('get_data')
        )

        serializer = BuyurtmaSerializer(buyurtma)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BuyurtmaDetail(APIView):
    def get_object(self, poc):
        try:
            return Buyurtma.objects.get(poc=poc)
        except Buyurtma.DoesNotExist:
            raise Http404

    def get(self, request, poc):
        buyurtma = self.get_object(poc)
        serializer = BuyurtmaSerializer(buyurtma)
        return Response(serializer.data)

    def put(self, request, poc):
        buyurtma = self.get_object(poc)
        serializer = BuyurtmaSerializer(buyurtma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, poc):
        buyurtma = self.get_object(poc)
        buyurtma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
