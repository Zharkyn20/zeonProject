from .views import NewsViewSet


"""This variable used in zeonProject/urls as News' app's urls.
Then registering in Api Root"""
routeList = (
    (r'news', NewsViewSet),
)
