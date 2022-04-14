from .views import OfferViewSet


"""This variable used in zeonProject/urls as offer app's urls.
Then registering in Api Root"""
routeList = (
    (r'offer', OfferViewSet),
)
