
from django.http import JsonResponse
from django.shortcuts import render
import json
from . models import CourseRegistration
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# post method
@csrf_exempt
def CourseDetails(request):
  try:
    if request.method == 'POST':
      data = json.loads(request.body)
      details = CourseRegistration.objects.create(
            name =data["name"],
            email =data["email"],
            course= data["course"],
            phone =data["phone"],
          
            )
      print(details.course)
      return JsonResponse({"status":"success","message": "Registration Successful"},status =201)
    else:
      return JsonResponse({"status":"fail","msg":"Other than Post any Method Is not allowed"})
  except Exception as e:
        print(e)
        return JsonResponse({"Error":"something went wrong"},status=500)
  
#Read by means Get
def CheckingDetails(request):
   try:
    if request.method == 'GET':
     result= list(CourseRegistration.objects.values()) #getting all the records from table
     print(result)
     if len(result) == 0:
      msg = "No Records Found"
     else:
      msg = "Data Retrived SuccessFully"
          
      return JsonResponse({"status":"success","message": msg ,"data":result,"total no of records":len(result)},status =201)
    else:
      return JsonResponse({"status":"fail","msg":"Other than Post any Method Is not allowed"})
   except Exception as e:
        print(e)
        return JsonResponse({"Error":"something went wrong"},status=500)
   
  





      


