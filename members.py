import os
import json
import requests


def is_member(telegram_id):
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjAxMTJlMzkxNDA1MDQ0YTZmNjRiYTRhZDk1MTQyZGJiZjM1MjljZDc4YmY2M2E3ZjA2MDQwODQ4YWFiMmUyY2E0ZmY4MTJkMjZlYmViNWYyIn0.eyJhdWQiOiJiMDNkYjAyNy0yODExLTQ1ZjctOGFkMC03MzQxMTc1ODJmN2UiLCJqdGkiOiIwMTEyZTM5MTQwNTA0NGE2ZjY0YmE0YWQ5NTE0MmRiYmYzNTI5Y2Q3OGJmNjNhN2YwNjA0MDg0OGFhYjJlMmNhNGZmODEyZDI2ZWJlYjVmMiIsImlhdCI6MTY0NzkzMzYxNywibmJmIjoxNjQ3OTMzNjE3LCJleHAiOjE5NjMyOTM2MTcuODIwNTQzLCJzdWIiOiIxNzU4Iiwic2NvcGUiOlsiYXV0aGVudGljYXRlZCIsInJlc3RfYXBpX2NoZWNrX2FjY2VzcyJdfQ.CsoH3kSUDCW5pp5kvvKH6eETptabZs9NDTnuC_DJwSBfFcjJsCnmLoAKeCK_yLVPAghtGDs3-hWuW5pTg3gOgg8pTuon5-jSx-VPGiTYBlKzod3r7urc5899cxW-WWxKvNEuNSc3M1ScIImOD6e8x3M2yNxniw2Ciu6qHohHs0Zu9w_RjIbD9Ux0bAg44xB9mYAP3IkP4HDqDds587dmvhZvQaI9VQXNupxVP6R7ZQ7S4Y-nOy9E1zpERAL2TnF15C30_CJzzKMxCAvgX30SbQP5EN6HObU6a6lBmkSOcDky0fKEVnHroPQL-HPK5WZHHCK-RsKgYwNy5fPj9Ap38A'
    # with open('printers/access-token', 'r', encoding='utf-8') as token_file:
    #     token = token_file.read()

    url = 'https://physics.itmo.ru/ru/rest/export/json/users-telegram-id-roles'
    params = {'_format': 'json', 'telegram_id_value': telegram_id}
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, params=params, headers=headers)
    resp = json.loads(response.text)

    #print(resp)..

    if resp != [] and resp[0]['roles_target_id'] == 'member':
        return True

    return False