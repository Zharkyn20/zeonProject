from rest_framework.pagination import PageNumberPagination


class PaginationCategories(PageNumberPagination):
    page_size = 8
