from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from sample.models import Person
from sample.serializers import PersonSerializers

class PersonViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

    def create(self, request):
        if self.request.method == 'POST':
            name = request.data.get('name')
            age = request.data.get('age')
            address = request.data.get('address')

            Person.objects.create(
                name=name,
                age=age,
                address=address
            )
            return Response('SUCCESS', status=status.HTTP_200_OK)
        else:
            return Response('FAILED', status=status.HTTP_400_BAD_REQUEST)

    def list(self, requset):
        query = self.get_queryset()
        serializer = self.get_serializer(query, many=True)
        if query.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



