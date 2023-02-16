from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse

class LangueSerializers(serializers.ModelSerializer):
    urlDetails = serializers.HyperlinkedIdentityField(view_name="formation-detail", lookup_field = "pk")
    urlDell = serializers.HyperlinkedIdentityField(view_name="formation-dell", lookup_field = "pk")
    urlUpdate = serializers.HyperlinkedIdentityField(view_name="formation-update", lookup_field = "pk")

    class Meta:
        model = Langue
        fields = ('id_langue','libelleLangue','urlDetails', 'urlDell','urlUpdate')

class TraductionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Traduires
        fields= ('motTraduit',)


