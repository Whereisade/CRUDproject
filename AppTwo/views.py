from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request):
        authors = self.get_queryset()
        serializer = self.get_serializer(authors, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            author = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response(
                {'error': 'Author not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):
        try:
            author = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Author.DoesNotExist:
            return Response(
                {'error': 'Author not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        try:
            author = self.get_queryset().get(pk=pk)
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response(
                {'error': 'Author not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )