from .views import HelpViewSet


"""This variable used in zeonProject/urls as help app's urls.
Then registering in Api Root"""
routeList = (
    (r'help', HelpViewSet),
)
