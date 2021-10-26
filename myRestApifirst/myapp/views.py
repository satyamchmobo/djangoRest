from django.shortcuts import render
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    # request_args=request.json()
    # print(request.json)
    numberOne = int (request.GET.get('numberOne'))
    numberTwo = int(request.GET.get('numberTwo'))
   
    
    roundupCal= numberTwo - (numberOne%numberTwo)
    totalValue = numberOne + roundupCal
    
    response = json.dumps({"totalValue":totalValue})
    return HttpResponse(response, content_type="application/json")
