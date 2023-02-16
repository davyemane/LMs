from rest_framework import serializers
from .models import *


class TraductionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Traduires
        fields = ('audio','motTraduit')

class MotFrSerializer(serializers.ModelSerializer):
    ecriture=serializers.CharField()
    Traduction = TraductionSerializer(read_only= True, many=True) 
    class Meta:
        model= MotFr 
        fields = ["ecriture","Traduction",] 

class ContenuSerializer(serializers.ModelSerializer):
    #champ = serializers.CharField(source="NomChamp.NomChamp", read_only=True, )
    mots = MotFrSerializer(source='id_Mot' ,read_only=True)

    class Meta:
        model= Contenir 
        fields=("mots",)
   # def get_mots(self,obj):
   #     return{'mot_francais':obj.id_Mot.ecriture, 'id':obj.id_Mot.pk}





class ChampSerializer(serializers.ModelSerializer):
    Niv = serializers.CharField(source="Nivform.libelleNiveauFormation", read_only=True)
    champ = ContenuSerializer(read_only=True, many=True)
    class Meta:
        model= ChampLexicale
        fields= ["Niv","champ", "NomChamp", "Nivform",]


class NiveauSerializer(serializers.ModelSerializer):
    niveau = ChampSerializer(read_only=True, many=True)
    class Meta:
        model= NiveauFormation
        fields="__all__"