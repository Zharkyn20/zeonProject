from rest_framework.pagination import PageNumberPagination


class PaginationMainPage(PageNumberPagination):
    page_size = 8


class PaginationCategories(PageNumberPagination):
    page_size = 4
