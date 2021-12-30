from rest_framework import serializers
from home.models import Createportfolio

class templateserializer(serializers.ModelSerializer):
    class Meta:
        model = Createportfolio
        fields = "__all__"