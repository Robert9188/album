from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from api.models import Photo
from api.models import Album
from api.models import User
from api.serializers import UserSerializer
from api.serializers import AlbumSerializer
from api.serializers import PhotoSerializer
from django.contrib.auth.models import User
from api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
 

@api_view(['GET'])
def api_root(request, format=None):
    
    return Response({
        'albums': reverse('album-list', request=request, format=format),
        'photos': reverse('photo-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format)
    })


class PhotoList(generics.ListCreateAPIView):
    
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        if album.photos.exists():
            return Response({'status': 'You cannot delete an Album that has Photos!'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            album.delete()


class UserList(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
