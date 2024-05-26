from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import cashier, employee

# Create your views here.

def all_cashiers(request):
    #return (HttpResponse("test"))
    if request.method == 'GET':
        cashiers = cashier.objects.all()
        cashier_list = list(cashiers.values())
        return JsonResponse(cashier_list, safe = False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status = 405)

def add_cashier(request):
    if request.method == 'POST':
        return JsonResponse({"success": "successful operation"}, status = 200)
    else:
        return JsonResponse({"error": "Method not allowed"}, status = 405)
