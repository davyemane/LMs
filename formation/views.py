from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions, authentication
from formation.vocabSerializer import ChampSerializer, NiveauSerializer, ContenuSerializer, MotFrSerializer, TraductionSerializer, ContenusSerializer
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





class ChampLexicaleViews(viewsets.ModelViewSet):
    queryset = ChampLexicale.objects.all().order_by('Nivform')
    serializer_class = ChampSerializer
    authentication_classes= [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ContenuListviews(generics.ListAPIView):
    queryset= Contenir.objects.all().order_by('NomChamp')
    serializer_class=ContenuSerializer
    authentication_classes= [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ContenuDetailViews(generics.RetrieveAPIView):
    queryset= Contenir.objects.all().order_by('NomChamp')
    serializer_class= ContenuSerializer
    lookup_field= 'id_Contenir'
    authentication_classes= [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ContenuCreatViews(generics.ListCreateAPIView):
    queryset= Contenir.objects.all().order_by('NomChamp')
    serializer_class= ContenusSerializer
    authentication_classes= [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class Niveauviews(viewsets.ModelViewSet):
    queryset= NiveauFormation.objects.all()
    serializer_class=NiveauSerializer
    authentication_classes= [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class Motfrviews(viewsets.ModelViewSet):
    queryset= MotFr.objects.all()
    serializer_class=MotFrSerializer
    authentication_classes= [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

 
class Traduireviews(viewsets.ModelViewSet):
    queryset= Traduires.objects.all()
    serializer_class=TraductionSerializer
    authentication_classes= [authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
