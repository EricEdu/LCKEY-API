
from .repositories import EntryRepository
from firebase_admin import auth, firestore

entry_repository = EntryRepository()

def insertedEntryAndExit(entryCode):
    try:
        passwords = entry_repository.getAllCodes()
        if entryCode in passwords['senhas']:
            status = {"status": "true"}
        else: 
            status = {"status": "false"}
        entryTipe = entry_repository.get_entry(entryCode)
        user = entry_repository.getUserByEntryCode(entryCode)

        # Validando se o tipo de entrada foi encontrado
        if user is None:
            msg = "CODIGO COLOCADO ESTA ERRADO OU NÃO EXISTE EM NOSSA BASE"
            return status

        else:
            # Caso a entrada seja inválida
            if status['status'] == "false":
                msg = "ENTRADA NEGADA REVISE COM SEU ADMINISTRADOR OU TENTE NOVAMENTE"
            else:
                if(entryTipe == "entrada"):
                    msg = "ENTRADA OCORRIDA COM SUCESSO"  # Mensagem de sucesso se a entrada for válida
                else:
                    msg = "SAIDA OCORRIDA COM SUCESSO"

        # Criando os dados para a entrada ou saída
        entry_data = {
            "userid": user['id'] if user['id'] else None,
            "entryCode": entryCode,
            # "isEntry": isEntry,
            "entryTipe": entryTipe,
            "entryMenssagem": msg,  # Usando a variável msg diretamente
            "status": True,
            "created_at": firestore.SERVER_TIMESTAMP,
            "usermail": user['email'] if user['email'] else None
        }

        # Chama o repositório para criar a entrada/saída
        entry_repository.createEntryAndExit(entry_data)
        return status
    except Exception as e:
        return {"error": str(e)}

    
def getAllUserCode():
    try:
        response = entry_repository.getAllCodes()
        return response
    except Exception as e:
        return {"error": str(e)}