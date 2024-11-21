from django.http import JsonResponse
from .services import insertedEntryAndExit, getAllUserCode
import json

def insertEntryAndExit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        entryCode = data.get('code')  # Certifique-se de que 'code' está sendo enviado na requisição
        # Chamando a função com ambos os argumentos
        response = insertedEntryAndExit(entryCode)  
        
        if "error" in response:
            return JsonResponse({"error": response["error"]}, status=400)
        return JsonResponse(response, status=200)  
    return JsonResponse({"error": "Method not allowed"}, status=405)  # Retorna erro caso o método não seja POST

def getAllCodes(request):
    if request.method == 'GET':
        response = getAllUserCode()
        
        if "error" in response:
            return JsonResponse({"error": response["error"]}, status=400)
        return JsonResponse(response, status=200)
    return JsonResponse({"error": "Method not allowed"}, status=405)  # Retorna erro caso o método não seja GET
