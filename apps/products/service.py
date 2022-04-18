from rest_framework.pagination import PageNumberPagination


class PaginationProducts(PageNumberPagination):
    page_size = 8