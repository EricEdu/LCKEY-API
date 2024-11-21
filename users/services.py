# users/services.py
import requests
from .repositories import UserRepository
from firebase_admin import auth, firestore

user_repository = UserRepository()

def register_user(email, password, isAdmin, id_admin=None):
    try:

        if id_admin:
            admin_user = user_repository.get_user(id_admin)

            if not admin_user or admin_user.get("role") != "admin":
                return {"error": "O ID fornecido não pertence a um administrador válido."}

        user = auth.create_user(email=email, password=password)
        role = "user"
        if(isAdmin and id_admin is None):
            role = "admin"
        user_data = {
            "uid": user.uid,
            "email": user.email,
            "role": role,
            "id_admin": id_admin if role == "user" else None,
            "created_at": firestore.SERVER_TIMESTAMP
        }

        response = user_repository.create_user(user_data)

        auth.set_custom_user_claims(user.uid, {
            'role': role,
            'admin_id': id_admin if role == "user" else None
        })

        return response
    except Exception as e:
        return {"error": str(e)}

def login_user(email, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDABWetSaM3JHkTeF8noZ_lhkvd32PNunI"
    
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        uid = data['localId']
        id_token = data['idToken']
        
        # Logar tentativa de login com sucesso
        user_repository.log_login_attempt(uid, success=True)

        return {"token": id_token, "uid": uid, "email": email}
    else:
        return {"error": response.json().get('error', {}).get('message', 'Unknown error')}

def get_users_by_admin_id(idAdmin):
    try:
        response = user_repository.get_users_by_admin_id(idAdmin)
        return response
    except Exception as e:
        return {"error": str(e)}
    

def verify_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return {"valid": True, "uid": decoded_token['uid']}
    except Exception as e:
        return {"valid": False, "error": str(e)}
