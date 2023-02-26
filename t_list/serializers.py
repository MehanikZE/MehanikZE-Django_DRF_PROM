from rest_framework import serializers
from t_list.models import Ezhednevnik


class ZadachiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ezhednevnik
        read_only_fields = ["id", "time_nach"]
        fields = read_only_fields + ["zadachi", "status", "active_switch"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
