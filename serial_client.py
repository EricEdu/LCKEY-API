import requests
import json
import serial as pyserial

try:
    arduino = pyserial.Serial('COM6', 9600, timeout=1)  # Adicionando timeout para evitar travamentos
    print("Conexão com Arduino estabelecida.")
except pyserial.SerialException as e:
    print(f"Erro ao conectar com a porta COM: {e}")
    exit()

# URL da API Django
api_url = 'http://127.0.0.1:8000/api/entry/insertentryandexit/'  # Ajuste conforme o endpoint da sua API

while True:
    if arduino.in_waiting > 0:
        # Lê os dados enviados pelo Arduino
        
        data = arduino.readline().decode('utf-8').strip()
        print(f"Dados recebidos: {data}")

            # Envia os dados para a API como JSON
        try:
            json_data = json.loads(data)
            req = {"code": int(json_data)}
            # Envia para a API Django
            response = requests.post(api_url, json=req)
            txtreturn = json.loads(response.text)
            print(f"Resposta da API: {response.status_code}, {txtreturn['status']}")
            arduino.write(txtreturn['status'].encode('utf-8'))
        except json.JSONDecodeError:
            print("Erro ao decodificar os dados recebidos do Arduino")
        except requests.RequestException as e:
            print(f"Erro ao enviar requisição para a API: {e}")
