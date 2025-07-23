from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import *

# Create your views here.
wilayat = [
  {
    "id": 1,
    "IDWilaya": 1,
    "name": "ADRAR",
    "delivery_home": 1400,
    "delivery_office": 970
  },
  {
    "id": 2,
    "IDWilaya": 2,
    "name": "CHLEF",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 3,
    "IDWilaya": 3,
    "name": "LAGHOUAT",
    "delivery_home": 950,
    "delivery_office": 670
  },
  {
    "id": 4,
    "IDWilaya": 4,
    "name": "OUM EL BOUAGHI",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 5,
    "IDWilaya": 5,
    "name": "BATNA",
    "delivery_home": 700,
    "delivery_office": 520
  },
  {
    "id": 6,
    "IDWilaya": 6,
    "name": "BEJAIA",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 7,
    "IDWilaya": 7,
    "name": "BISKRA",
    "delivery_home": 900,
    "delivery_office": 620
  },
  {
    "id": 8,
    "IDWilaya": 8,
    "name": "BECHAR",
    "delivery_home": 1100,
    "delivery_office": 720
  },
  {
    "id": 9,
    "IDWilaya": 9,
    "name": "BLIDA",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 10,
    "IDWilaya": 10,
    "name": "BOUIRA",
    "delivery_home": 700,
    "delivery_office": 520
  },
  {
    "id": 11,
    "IDWilaya": 11,
    "name": "TAMANRASSET",
    "delivery_home": 1500,
    "delivery_office": 1120
  },
  {
    "id": 12,
    "IDWilaya": 12,
    "name": "TEBESSA",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 13,
    "IDWilaya": 13,
    "name": "TLEMCEN",
    "delivery_home": 1000,
    "delivery_office": 720
  },
  {
    "id": 14,
    "IDWilaya": 14,
    "name": "TIARET",
    "delivery_home": 950,
    "delivery_office": 670
  },
  {
    "id": 15,
    "IDWilaya": 15,
    "name": "TIZI OUZOU",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 16,
    "IDWilaya": 16,
    "name": "ALGER",
    "delivery_home": 600,
    "delivery_office": 400
  },
  {
    "id": 17,
    "IDWilaya": 17,
    "name": "DJELFA",
    "delivery_home": 900,
    "delivery_office": 670
  },
  {
    "id": 18,
    "IDWilaya": 18,
    "name": "JIJEL",
    "delivery_home": 700,
    "delivery_office": 520
  },
  {
    "id": 19,
    "IDWilaya": 19,
    "name": "SETIF",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 20,
    "IDWilaya": 20,
    "name": "SAIDA",
    "delivery_home": 950,
    "delivery_office": 670
  },
  {
    "id": 21,
    "IDWilaya": 21,
    "name": "SKIKDA",
    "delivery_home": 700,
    "delivery_office": 520
  },
  {
    "id": 22,
    "IDWilaya": 22,
    "name": "SIDI BEL ABBES",
    "delivery_home": 1000,
    "delivery_office": 720
  },
  {
    "id": 23,
    "IDWilaya": 23,
    "name": "ANNABA",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 24,
    "IDWilaya": 24,
    "name": "GUELMA",
    "delivery_home": 700,
    "delivery_office": 520
  },
  {
    "id": 25,
    "IDWilaya": 25,
    "name": "CONSTANTINE",
    "delivery_home": 600,
    "delivery_office": 400
  },
  {
    "id": 26,
    "IDWilaya": 26,
    "name": "MEDEA",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 27,
    "IDWilaya": 27,
    "name": "MOSTAGANEM",
    "delivery_home": 1000,
    "delivery_office": 720
  },
  {
    "id": 28,
    "IDWilaya": 28,
    "name": "M'SILA",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 29,
    "IDWilaya": 29,
    "name": "MASCARA",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 30,
    "IDWilaya": 30,
    "name": "OUARGLA",
    "delivery_home": 1000,
    "delivery_office": 720
  },
  {
    "id": 31,
    "IDWilaya": 31,
    "name": "ORAN",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 32,
    "IDWilaya": 32,
    "name": "EL BAYADH",
    "delivery_home": 1050,
    "delivery_office": 720
  },
  {
    "id": 33,
    "IDWilaya": 33,
    "name": "ILLIZI",
    "delivery_home": 1500,
    "delivery_office": 1120
  },
  {
    "id": 34,
    "IDWilaya": 34,
    "name": "BORDJ BOU ARRERIDJ",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 35,
    "IDWilaya": 35,
    "name": "BOUMERDES",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 36,
    "IDWilaya": 36,
    "name": "EL TARF",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 37,
    "IDWilaya": 37,
    "name": "TINDOUF",
    "delivery_home": 1400,
    "delivery_office": 0
  },
  {
    "id": 38,
    "IDWilaya": 38,
    "name": "TISSEMSILT",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 39,
    "IDWilaya": 39,
    "name": "EL OUED",
    "delivery_home": 950,
    "delivery_office": 670
  },
  {
    "id": 40,
    "IDWilaya": 40,
    "name": "KHENCHELA",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 41,
    "IDWilaya": 41,
    "name": "SOUK AHRAS",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 42,
    "IDWilaya": 42,
    "name": "TIPAZA",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 43,
    "IDWilaya": 43,
    "name": "MILA",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 44,
    "IDWilaya": 44,
    "name": "AIN DEFLA",
    "delivery_home": 750,
    "delivery_office": 520
  },
  {
    "id": 45,
    "IDWilaya": 45,
    "name": "NAAMA",
    "delivery_home": 950,
    "delivery_office": 670
  },
  {
    "id": 46,
    "IDWilaya": 46,
    "name": "AIN TEMOUCHENT",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 47,
    "IDWilaya": 47,
    "name": "GHARDAIA",
    "delivery_home": 950,
    "delivery_office": 670
  },
  {
    "id": 48,
    "IDWilaya": 48,
    "name": "RELIZANE",
    "delivery_home": 800,
    "delivery_office": 520
  },
  {
    "id": 49,
    "IDWilaya": 49,
    "name": "TIMIMOUN",
    "delivery_home": 1400,
    "delivery_office": 0
  },
  {
    "id": 50,
    "IDWilaya": 50,
    "name": "BORDJ BADJI MOKHTAR",
    "delivery_home": 1400,
    "delivery_office": 0
  },
  {
    "id": 51,
    "IDWilaya": 51,
    "name": "OULED DJELLAL",
    "delivery_home": 900,
    "delivery_office": 620
  },
  {
    "id": 52,
    "IDWilaya": 52,
    "name": "BENI ABBES",
    "delivery_home": 1000,
    "delivery_office": 720
  },
  {
    "id": 53,
    "IDWilaya": 53,
    "name": "IN SALAH",
    "delivery_home": 1600,
    "delivery_office": 0
  },
  {
    "id": 54,
    "IDWilaya": 54,
    "name": "IN GUEZZAM",
    "delivery_home": 1600,
    "delivery_office": 0
  },
  {
    "id": 55,
    "IDWilaya": 55,
    "name": "TOUGGOURT",
    "delivery_home": 950,
    "delivery_office": 670
  },
  {
    "id": 56,
    "IDWilaya": 56,
    "name": "DJANET",
    "delivery_home": 1400,
    "delivery_office": 0
  },
  {
    "id": 57,
    "IDWilaya": 57,
    "name": "M'GHAIR",
    "delivery_home": 950,
    "delivery_office": 0
  },
  {
    "id": 58,
    "IDWilaya": 58,
    "name": "EL MENIAA",
    "delivery_home": 1000,
    "delivery_office": 0
  }
]

def wilayas(request):
    if request.method == 'GET':
        wilayat = WilayaInfo.objects.all()
        serializer = WilayaInfoSerializer(wilayat,many=True)
        return JsonResponse(serializer.data,safe=False)
    


