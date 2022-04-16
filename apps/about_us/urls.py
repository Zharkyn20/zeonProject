from .views import AboutUsViewSet


"""This variable used in zeonProject/urls as About Us's app's urls.
Then registering in Api Root"""
routeList = (
    (r'about_us', AboutUsViewSet),
)
