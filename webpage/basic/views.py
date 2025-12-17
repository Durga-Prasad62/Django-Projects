from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import math

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
     return render(request,'about.html')
def contact(request):
     return render(request,'contact.html')
def service(request):
     return render(request,'services.html')
def sample(request):
     return HttpResponse("<h1>welcome to the html</h1>")

def sample1(request):
     info= {"data":{"name":"raju","Age":16,"location":"hyderabad"}}
     return JsonResponse(info)
# dynamic Response as per the input in the req
def sample2(request):
     print(request)
     qp1 = request.GET.get("name")
     qp2 = request.GET.get("city")
     return  HttpResponse(f"hello {qp1} is from {qp2}")

def sample3(request):
     product_name = request.GET.get("prod_name","laptop")
     product_quantity = int(request.GET.get("prod_quantity",2))
     product_price = int(request.GET.get("prod_price",154456))
     return JsonResponse({'product name':product_name, 'product_quantity': product_quantity ,'product price':product_price,'total_price':product_price*product_quantity})




#filtered data 
def filter_views(request):
     student_names=[{'name':'prasad','city':'hyderabad'},{'name':'uma','city':'bangalore'},{'name':'sriram','city':'hyderabad'}]
     city = request.GET.get("city","hyderabad")
     info =[]
     for x in student_names:
          if x['city']==city:
               info.append(student_names)
     return JsonResponse({"data":info})




#pagination
def manual_pagination(request):
     limit = int(request.GET.get("limit",4))
     page = int(request.GET.get("page",1))
     data =list(range(1,21))
     total_items= len(data)
     total_pages = (total_items+limit-1)//limit
     start = (page-1)*limit
     end = start+limit
     pagination_data = data[start:end]

     if page < 1 or page > total_pages:
        return JsonResponse({"error": "Invalid page number"}, status=400)

     return JsonResponse({
        "limit": limit,
        "total_pages": total_pages,
        "current_page": page,
        "data":  pagination_data
    })

# DIFFERENT  APPROACH
def Pagination_data(request):
     items=["orange","apple","banana","kiwi","pome-granate","papaya","dragon fruit","grapes","custard-apple","pine-apple","mango","Strawberry","Watermelon","Cherry","Blackberry","Blueberry"]
     limit = int(request.GET.get("limit",4))
     page = int(request.GET.get("page",1))
     start = (page - 1) * limit
     end = start + limit
     total_pages = math.ceil(len(items) / limit)
     pagination_data=(items[start:end])
     if page < 1 or page > total_pages:
      return JsonResponse({"error": "Invalid page number"}, status=400)
     return JsonResponse({
          "limit": limit,
          "total_pages": total_pages,
          "current_page": page,
          "data":  pagination_data
    })






