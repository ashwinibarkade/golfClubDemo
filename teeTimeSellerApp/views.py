from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

def rest_getListOfAlgorithms(request):
    response = HttpResponse(json.dumps({"algoList":["bookCourt","makePayment"]}))
    response['Access-Control-Allow-Origin'] = '*';
    return response;
