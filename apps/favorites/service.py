from rest_framework.pagination import PageNumberPagination


class PaginationFavorites(PageNumberPagination):
    page_size = 12
