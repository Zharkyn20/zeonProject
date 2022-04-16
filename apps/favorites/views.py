from rest_framework import viewsets
from .serializers import UserFavoritesSerializer,\
    UserFavoritesPostSerializer
from .models import Favorite
from .service import PaginationFavorites


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    Get all user's favorite products.
    """
    queryset = Favorite.objects.all()
    serializer_classes = {
        'create': UserFavoritesPostSerializer
    }
    default_serializer_class = UserFavoritesSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    pagination_class = PaginationFavorites
