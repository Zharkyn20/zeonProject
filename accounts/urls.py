from .views import CustomUserViewSet


"""This variable used in zeonProject/urls as Account's app's urls.
Then registering in Api Root"""
routeList = (
    (r'customers', CustomUserViewSet),
)
