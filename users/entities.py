from datetime import datetime

class User:
    def __init__(self, uid, email, role='user', id_admin=None, created_at=None):
        self.uid = uid
        self.email = email
        self.role = role
        self.id_admin = id_admin
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'uid': self.uid,
            'email': self.email,
            'role': self.role,
            'id_admin': self.id_admin,
            'created_at': self.created_at,
        }

class LoginAttempt:
    def __init__(self, uid, success, timestamp=None):
        self.uid = uid
        self.success = success
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        return {
            'uid': self.uid,
            'success': self.success,
            'timestamp': self.timestamp,
        }
