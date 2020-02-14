from .models import Resident
from .validators import add_title
from rest_framework import serializers
from .resident import Resident as ResidentClass


class ResidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = "__all__"

    def validate(self, attrs):
        res = ResidentClass(attrs)
        attrs = res.add_title()
        print("After Class Validation", attrs)
        del res
        return attrs
