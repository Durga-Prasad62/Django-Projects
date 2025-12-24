
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
      return JsonResponse({"Other than Post any Method Is not allowed"})
  except Exception as e:
        print(e)
        return JsonResponse({"Error":"something went wrong"},status=500)




      


