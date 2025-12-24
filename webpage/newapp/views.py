from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . models import   MovieDetails
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def MovieTickets(request):
    try:
        if request.method == "POST":
            data =json.loads(request.body)
            details =  MovieDetails.objects.create(
                moviename =data["moviename"],
                moviescreen =data["screen"],
                bookingid = data["bookingid"],
                theatrename =data["theatrename"],
                user_email = data["email"],
                showtype = data["showtype"],
                price = data["price"]
            )
            print(details.transactionid)
            return JsonResponse({"status":"success","message":"movie_ticket is placed","transaction_id": str(details.transactionid)},status =201)

        else:
            return JsonResponse({"Error":"only post allowed"},status=400)
    except Exception as e:
        print(e)
        return JsonResponse({"Error":"something went wrong"},status=500)
    
def MovienewTickets(request):
     return HttpResponse("MovieTickets works!")
