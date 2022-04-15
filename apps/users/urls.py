from .views import UserViewSet, FavoriteViewSet


"""This variable used in zeonProject/urls as user app's urls.
Then registering in Api Root"""
routeList = (
    (r'user', UserViewSet),
    (r'favorites', FavoriteViewSet),
)