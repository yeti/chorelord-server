from chores.models import Users
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'group_name', 'start_date', 'interval')

    def create(self, validated_data):
        return Users.objects.create(**validated_data)