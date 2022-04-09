from .views import ProductListViewSet


"""This variable used in zeonProject/urls as product app's urls.
Then registering in Api Root"""
routeList = (
    (r'products', ProductListViewSet),
)