from rest_framework.pagination import PageNumberPagination


class PaginationCategoryProducts(PageNumberPagination):
    page_size = 12
