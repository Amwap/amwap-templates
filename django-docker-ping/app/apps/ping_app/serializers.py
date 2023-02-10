from rest_framework import serializers
from apps.ping_app.models import Ping


class IncomePingSerializer(serializers.Serializer):
    count = serializers.IntegerField(max_value=10, min_value=0)

    def validate(self, attrs:dict[str, any]) -> any:
        attrs = super().validate(attrs)
        return attrs


class PingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ping
        fields = [
                'host'
                'created_at'
            ]

