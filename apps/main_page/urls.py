from .views import SliderViewSet, BestSellerViewSet, \
    NoveltiesViewSet, CategoriesViewSet, MoreCategoriesViewSet, \
    OurAdvantagesViewSet


"""This variable used in zeonProject/urls as Main Page app's urls.
Then registering in Api Root"""
routeList = (
    (r'main_page/slider', SliderViewSet),
    (r'main_page/best_seller', BestSellerViewSet),
    (r'main_page/novelties', NoveltiesViewSet),
    (r'main_page/categories', CategoriesViewSet),
    (r'main_page/more_categories', MoreCategoriesViewSet),
    (r'our_advantages', OurAdvantagesViewSet),

)
