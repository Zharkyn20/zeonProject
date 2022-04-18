from .views import FooterViewSet


"""This variable used in zeonProject/urls as Footer app's urls.
Then registering in Api Root"""
routeList = (
    (r'footer', FooterViewSet),
)