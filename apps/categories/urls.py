from .views import CategoryViewSet


"""
This variable is used in zeonProject/urls as category app's urls.
Then registering in Api Root
"""
routeList = (
    (r'categories', CategoryViewSet),
)