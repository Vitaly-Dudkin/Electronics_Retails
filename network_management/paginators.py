from rest_framework.pagination import PageNumberPagination


class NetworkPagination(PageNumberPagination):
    page_size = 5


class ProductPagination(PageNumberPagination):
    page_size = 5


class SupplierPagination(PageNumberPagination):
    page_size = 5
