from LCKEY.firebase import db, firestore
from entry.entities import Entry

class EntryRepository:
    def createEntryAndExit(self, entry_data):
        try:
            entry = Entry(
                userid=entry_data['userid'],
                entryCode=entry_data['entryCode'],
                entryTipe=entry_data['entryTipe'],
                entryMenssagem=entry_data['entryMenssagem'],
                status=entry_data['status'],
                created_at=entry_data.get('created_at'),
                usermail=entry_data['usermail']
            )
            entry_ref = db.collection('entry')
            entry_ref.add(entry.to_dict())
            return {"success": True, "message": "Entry created successfully"}
        except Exception as e:
            return {"error": str(e)}

    def get_entry(self, entryCode):
        try:
            # Recupera a coleção 'entry' e faz a consulta pelo 'entryCode'
            entry_ref = db.collection('entry')
            query = entry_ref.where('entryCode', '==', entryCode).get()

            if query:  # Verifica se a consulta retornou algum documento
                # Converte o primeiro documento encontrado para um dicionário
                entry_data = query[0].to_dict()  # Usando o primeiro documento encontrado

                # Obtemos o valor de count
                count = len(query)

                # Se o count não existir, assume-se que a entrada é "entrada"
                if count is None:
                    return 'entrada'
                else:
                    # Verifica se o count é um número inteiro
                    if not isinstance(count, int):
                        return {"error": "count must be an integer"}

                    # Verifica se count é ímpar ou par e define a ação
                    if count % 2 == 0:
                        # Se o count for par, consideramos 'entrada'
                        return 'entrada'
                    else:
                        # Se o count for ímpar, consideramos 'saida'
                        return 'saida'
            else:
                # Se não houver documentos, assume que a entrada é 'entrada'
                return 'entrada'

        except Exception as e:
            return {"error": str(e)}




    def getUserByEntryCode(self, entryCode):
        try:
            users_ref = db.collection('users')
            query = users_ref.where('entryCode', '==', entryCode).get()

            # Verifica se a consulta retornou documentos
            if query:
                # Retorna o pri meiro documento encontrado como um dicionário
                return {"id": query[0]._data['uid'], "email": query[0]._data['email']} # Retorna um dicionário com id do documento e dados
            else:
                entry_ref = db.collection('entry')
                query = entry_ref.where('entryCode', '==', entryCode).get()
                if query: # Acessa a coleção de usuários
                    query = users_ref.where('uid', '==', query[0]._data['userid']).get()
                    return {"id": query[0]._data['uid'], "email": query[0]._data['email']}
                
            return None  # Retorna None se nenhum documento for encontrado
        except Exception as e:
            return {"error": str(e)}


    def getAllCodes(self):
        try:
            entry_ref = db.collection('users')
            query = entry_ref.get()  # Obtendo todos os documentos na coleção 'users'
            entry_list = []

        # Iterando sobre os documentos retornados pela consulta
            for doc in query:
                entry_data = doc.to_dict()  # Obtendo os dados do documento
                if 'entryCode' in entry_data:  # Verificando se o campo entryCode existe
                    entry_list.append(entry_data['entryCode'])  # Adicionando o entryCode à lista

            return {"senhas": entry_list}  # Retorna a lista com todos os entryCodes

        except Exception as e:
            print(f"Erro ao obter os entryCodes: {e}")
        except Exception as e:
            return {"error": str(e)}

