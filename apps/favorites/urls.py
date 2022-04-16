from .views import FavoriteViewSet


"""This variable used in zeonProject/urls as user app's urls.
Then registering in Api Root"""
routeList = (
    (r'favorites', FavoriteViewSet),
)
