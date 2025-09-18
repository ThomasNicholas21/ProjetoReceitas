from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class DefaultPaginationOffset(LimitOffsetPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class DefaultPaginationPageNumber(PageNumberPagination):
    page_size = 5
    max_page_size = 10
