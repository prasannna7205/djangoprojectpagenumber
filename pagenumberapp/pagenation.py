from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class Mypaginations(PageNumberPagination):
    page_size=3
    page_query_param="mypage"
    last_page_strings=('endpage')
