from rest_framework import serializers

from sample.models import Person


class PersonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('name', 'age', 'address')

