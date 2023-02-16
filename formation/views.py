from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import mixins
from formation.vocabSerializer import ChampSerializer, NiveauSerializer, ContenuSerializer, MotFrSerializer, TraductionSerializer
from.serializer import*
from .models import *

#afficher toute les langue
class ListLangue(generics.ListAPIView):
    queryset = Langue.objects.all()
    serializer_class= LangueSerializers

#afficher les details sur une langue
class DetailLangue(generics.RetrieveAPIView):
    queryset = Langue.objects.all()
    serializer_class= LangueSerializers

#supprimer une langue
class DellLangue(generics.DestroyAPIView):
    queryset = Langue.objects.all()
    serializer_class= LangueSerializers

#ajouter une langue
class CreateLangue (generics.ListCreateAPIView):
    queryset= Langue.objects.all()
    serializer_class= LangueSerializers

#modifier une langue
class UpdateLangueView(generics.UpdateAPIView):
    queryset = Langue.objects.all()
    serializer_class= LangueSerializers
    lookup_field = 'pk'




class ChampListApiView(APIView):
    def get(self, request, *args, **kwargs):
        champ = ChampLexicale.objects.filter('Niveau')
        serializer = ChampSerializer(champ(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request,*args, **kwargs):

        data = {
            "NomChamp":request.data.get('NomChamp'),
            "Niveau":request.Niveau.id_Niveau
        }
        serializer = ChampSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChampLexicaleViews(viewsets.ModelViewSet):
    queryset = ChampLexicale.objects.all().order_by('Nivform')
    serializer_class = ChampSerializer
 


class ContenuListviews(generics.ListAPIView):
    queryset= Contenir.objects.filter(NomChamp=1).order_by('NomChamp')
    serializer_class=ContenuSerializer

class ContenuDetailViews(generics.RetrieveAPIView):
    queryset= Contenir.objects.all()
    serializer_class= ContenuSerializer
    lookup_field= 'id_Contenir'

class Niveauviews(viewsets.ModelViewSet):
    queryset= NiveauFormation.objects.all()
    serializer_class=NiveauSerializer
    
class Motfrviews(viewsets.ModelViewSet):
    queryset= MotFr.objects.all()
    serializer_class=MotFrSerializer

 
class Traduireviews(viewsets.ModelViewSet):
    queryset= Traduires.objects.all()
    serializer_class=TraductionSerializer

