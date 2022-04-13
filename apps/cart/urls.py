from .views import CartViewSet


"""This variable used in zeonProject/urls as cart app's urls.
Then registering in Api Root"""
routeList = (
    (r'cart', CartViewSet),
)