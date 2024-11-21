from datetime import datetime

class Entry:
    def __init__(self, entryCode, entryTipe, entryMenssagem, userid, usermail, status, created_at=None):
        self.entryCode = entryCode
        self.entryTipe = entryTipe
        self.entryMenssagem = entryMenssagem
        self.userid = userid
        self.usermail = usermail
        self.status = status
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'entryCode' : self.entryCode,
            'entryTipe' : self.entryTipe,
            'entryMenssagem' : self.entryMenssagem,
            'userid' : self.userid,
            'usermail' : self.usermail,
            'status' : self.status,
            'created_at' : self.created_at
        }

# class LoginAttempt:
#     def __init__(self, uid, success, timestamp=None):
#         self.uid = uid
#         self.success = success
#         self.timestamp = timestamp or datetime.now()

    # def to_dict(self):
    #     return {
    #         'uid': self.uid,
    #         'success': self.success,
    #         'timestamp': self.timestamp,
    #     }