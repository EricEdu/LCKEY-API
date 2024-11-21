from LCKEY.firebase import db, firestore
from users.entities import User, LoginAttempt

class UserRepository:
    def create_user(self, user_data):
        try:
            user = User(
                uid=user_data['uid'], 
                email=user_data['email'], 
                role=user_data['role'],
                id_admin=user_data['id_admin'],
                created_at=user_data.get('created_at')
            )
            user_ref = db.collection('users').document(user.uid)
            user_ref.set(user.to_dict())
            return {"success": True, "message": "User created successfully"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_user(self, uid):
        try:
            user_ref = db.collection('users').document(uid).get()
            if user_ref.exists:
                return user_ref.to_dict()
            else:
                return None
        except Exception as e:
            return {"error": str(e)}

    def log_login_attempt(self, uid, success):
        try:
            attempt = LoginAttempt(uid=uid, success=success)
            attempts_ref = db.collection('login_attempts').document(uid)
            attempts_ref.update({
                "attempts": firestore.ArrayUnion([attempt.to_dict()])
            })
            return {"success": True}
        except Exception as e:
            return {"error": str(e)}
        
    def get_users_by_admin_id(self, id_admin):
        try:
            users_ref = db.collection('users')  # Acessa a coleção de usuários
            query = users_ref.where('id_admin', '==', id_admin).get()  # Aplica a consulta pelo admin_id
            users_list = []

            for user in query:
                user_data = user.to_dict()  # Converte os dados do usuário para dict
                users_list.append(user_data)  # Adiciona à lista de usuários

            if users_list:
                return {"users": users_list}  # Retorna a lista de usuários
            else:
                return {"message": "Nenhum usuário vinculado a este administrador."}  # Caso não haja resultados
        except Exception as e:
            return {"error": str(e)}  # Retorna qualquer erro que ocorrer

