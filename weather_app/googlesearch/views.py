from django.shortcuts import render
from rest_framework.views import APIView
from .models import WEATHER_RECURRENT
from .serializers import GetAllCourseSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View
from rest_framework import status
import cx_Oracle
# Create your views here.

"""
class GetAllCouse(APIView):   
    def get(self, request):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='covid19db')
        conn = cx_Oracle.connect(user='sa', password='123456', dsn=dsn_tns)
        sql = "select * from thongkeqg"
        lis = []
        with conn.cursor() as cursor:
            tmp = cursor.execute(sql)
            for i in tmp:
                lis.extend(i)
        conn.close()
        mydata = GetAllCourseSerializer(lis, many=True)
        return Response(data=mydata.data, status=status.Http_200_OK)
        # return HttpResponse('xin chao day la class base')
"""
    
def index(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
    conn = cx_Oracle.connect(user='phapnm', password='123', dsn=dsn_tns)
    sql = "select tentp, feel_like, w_descript, cloud, wind_speed from (select * from weather_current order by id desc) where rownum = 1"
    tmp_list = []
    with conn.cursor() as cursor:
        tmp = cursor.execute(sql)
        for i in tmp:
            tmp_list.extend(i)
    conn.close()
    data_list = []
    data_dic = {
        'tentp': tmp_list[0],
        # 'tentp': datacity,
        'feel_like': tmp_list[1],
        'w_descript': tmp_list[2],
        'cloud': tmp_list[3],
        'wind_speed': tmp_list[4],
    }
    data_list.append(data_dic)
    
    context = {'data_list': data_list}
    #mydata = GetAllCourseSerializer(lis, many=True)
    return render(request, 'googlesearch/index.html', context)

# def index(request):
#     # return HttpResponse("Hello Wo")
#     myname = "Tund"
#     sanpham = ["Điện thoại", "Máytính"]
#     context = {"name": myname, "sanpham": sanpham}
#     return render(request, "polls/index.html", context)

# class Home(View):
#     def get(self, request):
#         return HttpResponse('', homepage/index.html)

# class SearchView(TemplateView):
#     template_name = "googlesearch/result.html"

#     def get_context_data(self, **kwargs):

#         context = super(SearchView, self).get_context_data(**kwargs)

#         service = build("customsearch", GOOGLE_SEARCH_API_VERSION,
#                         developerKey=GOOGLE_SEARCH_API_KEY)
#         # add a "try" block to see if googleapiclient throws a 400 error
#         try:
#             results = service.cse().list(
#                 q=self.request.GET.get('q', ''),
#                 start=self.page_to_index(),
#                 num=GOOGLE_SEARCH_RESULTS_PER_PAGE,
#                 cx=GOOGLE_SEARCH_ENGINE_ID,
#             ).execute()

#             results = SearchResults(results)
#             pages = self.calculate_pages()

#         # if googleapiclient raises an error, we need to catch it here
#         except:

#             # run the search again starting with a defined page 1 instead of the "user" defined
#             results = service.cse().list(
#                 q=self.request.GET.get('q', ''),
#                 start=1,
#                 num=GOOGLE_SEARCH_RESULTS_PER_PAGE,
#                 cx=GOOGLE_SEARCH_ENGINE_ID,
#             ).execute()

#             # set some default values used for the context below
#             page = 1

#             # previous, current, next pages
#             pages = [0, 1, 2]

#             results = SearchResults(results)

#         """ Set some defaults """
#         context.update({
#             'items': [],
#             'total_results': 0,
#             'current_page': 0,
#             'prev_page': 0,
#             'next_page': 0,
#             'search_terms': self.request.GET.get('q', ''),
#             'error': results
#         })

#         """ Now parse the results and send back some
#             useful data """

#         context.update({
#             'items': results.items,
#             'total_results': results.total_results,
#             'current_page': pages[1],
#             'prev_page': pages[0],
#             'next_page': pages[2],
#             'search_terms': results.search_terms,
#         })

#         return context

#     def calculate_pages(self):
#         """ Returns a tuple consisting of
#             the previous page, the current page,
#             and the next page """

#         current_page = int(self.request.GET.get('p', 1))
#         return (current_page - 1, current_page, current_page + 1)

#     def page_to_index(self, page=None):
#         """ Converts a page to the start index """

#         if page is None:
#             page = self.request.GET.get('p', 1)

#         return int(page) * int(GOOGLE_SEARCH_RESULTS_PER_PAGE) + 1 - int(GOOGLE_SEARCH_RESULTS_PER_PAGE)


# THONGKEQG = quocgia.objects.all()
# def index(request):
#     return render(request, 'googlesearch/index.html')
