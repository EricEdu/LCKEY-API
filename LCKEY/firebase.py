import firebase_admin
from firebase_admin import credentials, firestore, auth

def initialize_firebase():
    cred = credentials.Certificate('O:/PROJETOS_MELLOAIT/APILOCKKEY/LCKEY/service_account/firebase.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = initialize_firebase()
# import firebase_admin
# from firebase_admin import auth, credentials

# # Inicializando o Firebase Admin SDK (caso ainda não tenha sido inicializado)
# cred = credentials.Certificate("caminho/para/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# def set_user_role(uid, role):
#     # Verificando se a role é válida
#     if role not in ['admin', 'common']:
#         return {"error": "Invalid role"}

#     # Definindo a role como uma 'custom claim'
#     try:
#         auth.set_custom_user_claims(uid, {'role': role})
#         return {"success": f"Role '{role}' assigned to user {uid}"}
#     except Exception as e:
#         return {"error": str(e)}

# # Exemplo de uso
# response = set_user_role('user_uid', 'admin')
# print(response)

