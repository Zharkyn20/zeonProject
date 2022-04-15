from rest_framework.pagination import PageNumberPagination


class PaginationNews(PageNumberPagination):
    page_size = 8
