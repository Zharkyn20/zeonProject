from .views import FloatingButtonViewSet,\
    CallbackViewSet


"""This variable used in zeonProject/urls as Floating Button app's urls.
Then registering in Api Root"""
routeList = (
    (r'floating_button', FloatingButtonViewSet),
    (r'callback', CallbackViewSet),
)