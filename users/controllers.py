from django.http import JsonResponse
from .services import get_users_by_admin_id, login_user, register_user, verify_token
import json

def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        isadmin = data.get('isAdmin')
        id_admin = data.get('id_admin')
        response = register_user(email, password, isadmin, id_admin)
        if "error" in response:
            return JsonResponse({"error": response["error"]}, status=400)
        return JsonResponse(response, status=201)

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        response = login_user(email, password)
        if "error" in response:
            return JsonResponse({"error": response["error"]}, status=400)
        return JsonResponse(response, status=200)

def verify(request):
    if request.method == 'POST':
        token = request.headers.get('Authorization').split(' ')[1]  # Obtendo o Bearer token
        response = verify_token(token)
        if not response['valid']:
            return JsonResponse({"error": response["error"]}, status=401)
        return JsonResponse({"uid": response["uid"]}, status=200)

def getUsersByAdmin(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization').split(' ')[1] 
        idAdmin = verify_token(token)
        response = get_users_by_admin_id(idAdmin['uid'])
    if "error" in response:
        return JsonResponse({"error": response["error"]}, status=400)
    return JsonResponse(response, status=200)
