import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import account
from django.views.decorators.csrf import csrf_exempt

def cashier_unfreeze(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        modify_account = account.objects.get(account_id = data.get("accountID"))
        modify_account.is_frozen = False
        modify_account.save()
        return JsonResponse({"success": "successful operation"}, status = 200)
    elif request.method == 'OPTIONS':
        return JsonResponse({"success": "OPTION operation"}, status = 200)
    else: return JsonResponse({"error": "Method not allowed"}, status = 405)

def cashier_freeze(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        modify_account = account.objects.get(account_id = data.get("accountID"))
        modify_account.is_frozen = True
        modify_account.save()
        return JsonResponse({"success": "successful operation"}, status = 200)
    elif request.method == 'OPTIONS':
        return JsonResponse({"success": "OPTION operation"}, status = 200)
    else: return JsonResponse({"error": "Method not allowed"}, status = 405)

def cashier_reportloss(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        modify_account = account.objects.get(account_id = data.get("accountID"))
        modify_account.is_lost = True
        modify_account.save()
        return JsonResponse({"success": "successful operation"}, status = 200)
    elif request.method == 'OPTIONS':
        return JsonResponse({"success": "OPTION operation"}, status = 200)
    else: return JsonResponse({"error": "Method not allowed"}, status = 405)

def cashier_reissue(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        delete_account = account.objects.get(account_id = data.get("accountID"))
        delete_account.delete()
        return JsonResponse({"success": "successful operation"}, status = 200)
    elif request.method == 'OPTIONS':
        return JsonResponse({"success": "OPTION operation"}, status = 200)
    else: return JsonResponse({"error": "Method not allowed"}, status = 405)