from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import math
from django.views.decorators.csrf import csrf_exempt
import json
from basic.models import Productmodel, UserProfile


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
     res= {"limit": limit,
          "total_pages": total_pages,
          "current_page": page,
          "data":  pagination_data}

     return JsonResponse ({"data": res}, status=200)





def new_pagination_data(request):
     items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
     limit = int(request.GET.get("limit",4))
     page = int(request.GET.get("page",1))
     start = (page-1)*limit
     end = start + limit 
     res = items[start:end]
     total_pages =  math.ceil (len(items)/limit)
     res= {"limit": limit,
          "total_pages": total_pages,
          "current_page": page,
          "data":  res}
     return JsonResponse ({"data": res}, status=200)

@csrf_exempt 
def Createuser(request):
     if request.method =='POST':
          data = json.loads( request.body)
          print(data)
     return JsonResponse({"status":"success"})
@csrf_exempt
def CreateProduct(request):
     if request.method == 'POST':
          data = json.loads(request.body)
          print(data)
     return JsonResponse({"status":"Success"})

@csrf_exempt
def CreateProfile(request):
     try:
          if request.method == 'POST':
               data = json.loads(request.body)
               name = data.get("name")
               age = data.get("age")
               city = data.get("city")
               UserProfile.objects.create(name =name,age = age,city=city)
               return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
     except Exception as e:
           return JsonResponse({"statuscode":501,"message":"internalservererror"})
     


@csrf_exempt
def ProductProfile(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            pro_name = data.get("pro_name")
            pro_price = data.get("pro_price")
            pro_quantity = data.get("pro_quantity")

            # Validation
            if not pro_name or not pro_price or not pro_quantity:
                return JsonResponse({"error": "All fields are required"}, status=400)

            # Convert to numeric types
            try:
                pro_price = float(pro_price)
                pro_quantity = int(pro_quantity)
            except ValueError:
                return JsonResponse({"error": "pro_price must be a number and pro_quantity must be an integer"}, status=400)

            pro_total = pro_price * pro_quantity

            product = Productmodel.objects.create(
                pro_name=pro_name,
                pro_price=pro_price,
                pro_quantity=pro_quantity,
                pro_total=pro_total
            )
            return JsonResponse({
                "status": "success",
                "data": {
                    "id": product.id,
                    "pro_name": pro_name,
                    "pro_price": pro_price,
                    "pro_quantity": pro_quantity,
                    "pro_total": pro_total
                },
                "statuscode": 201
            }, status=201)

        return JsonResponse({"message": "Please send POST request"}, status=400)

    except Exception as e:
        return JsonResponse({"statuscode": 501, "message": "internalservererror", "error": str(e)}, status=501)
    
def  Carlist(request):
     car_model = request.GET.get("car_model", "maruthi")
     car_price = int(request.GET.get("car_price", 100000))
     car_color = request.GET.get("car_color", "red")
     if car_price>8000000:
          meme = "rich bro miru"
     elif car_price<=8000000 and  car_price>6000000:
          meme = "haha car"
     elif car_price<=6000000 and car_price>=4000000:
          meme ="miru manchi range"
     else:
          meme = " car konnarooch"
     return JsonResponse({"carcolor":car_color, "carprice": meme,"carmodel":car_model})
     














