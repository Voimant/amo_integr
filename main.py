import json
from pprint import pprint
from amocrm.v2 import tokens
import requests
from config import TOKEN, REF_TOKEN

# BASE_URL = f'https://temabanyaclub.amocrm.ru/api/v4/leads'
#
# params = {'page': 1,
#           'limit': 5,
#           }

headers = {'Authorization': 'Bearer ' + TOKEN}
# response = requests.get(BASE_URL, params=params, headers=headers)
BASE_URL_2 = f'https://temabanyaclub.amocrm.ru/api/v4/leads'

def get_fields_leed():
    BASE_URL = 'https://temabanyaclub.amocrm.ru/api/v4/leads/custom_fields'
    headers = {'Authorization': 'Bearer ' + TOKEN}
    response = requests.get(BASE_URL, headers=headers)
    return response


def get_upgrade_token():
    with open('refresh_token.txt', 'r') as f:
        old_ref = f.read()
    BASE_URL_3 = f'https://temabanyaclub.amocrm.ru/oauth2/access_token'
    params = {
      "client_id": "abf93b9f-de0d-4b39-a8ce-cd83cb3facdb",
      "client_secret": "LvqHP6Pq25BCzqXxQC8Yg8kXspD1m7I0RmL3eGcjq1FcReEF9B3B6eKY7rsCYoEI",
      "grant_type": "refresh_token",
      "refresh_token": str(old_ref),
      "redirect_uri": "https://t.me/test_voimant_2_bot"
    }
    response = requests.post(BASE_URL_3, data=params)
    pprint(response.json())
    ref_token = response.json()['refresh_token']
    access_token = response.json()['access_token']
    pprint(response.json())

    with open('access_token.txt', 'w') as f:
        f.write(access_token)

    with open('refresh_token.txt', 'w') as f:
        f.write(ref_token)
    return 'Tокены успешно обновлены'

def post_lead(fio, city, date):
    get_upgrade_token()
    with open('access_token.txt', 'r') as f:
        token = f.read()
    BASE_URL_2 = f'https://temabanyaclub.amocrm.ru/api/v4/leads'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
    payload = [
        {'name': fio,
         'custom_fields_values': [
             {'field_id': 697657,
              'values': [{'value': fio}]}, # ФИО
             # {'field_id': 697659,
             #  'values': [{'value': phone}]},   #Номер телефона
             {'field_id': 208451,
              'values': [{'value': city}]}, # Город
             # {'field_id': 697645,
             #  'values': [{'value': programs}]}, # Programma
             {'field_id': 697647,
              'values': [{'value': date}]},  # data697649
             # {'field_id': 697649,
             #  'values': [{'value': time}]}, #time
             # {'field_id': 697651,
             #  'values': [{'value': many}]}, # how many
             # {'field_id': 697653,
             #  'values': [{'value': child}]} # child
         ]
         }
               ]
    response = requests.post(BASE_URL_2, headers=headers, json=payload)
    if response.status_code == 200:
        return 'Сделка создана'
    else:
        return response.json()





if __name__ == "__main__":

    #pprint(get_fields_leed().json())

    # get_upgrade_token()
    print(post_lead('oleg', '89223244617', 'perm', ))

    # tokens.default_token_manager(
    #     client_id="abf93b9f-de0d-4b39-a8ce-cd83cb3facdb",
    #     client_secret="LvqHP6Pq25BCzqXxQC8Yg8kXspD1m7I0RmL3eGcjq1FcReEF9B3B6eKY7rsCYoEI",
    #     subdomain="temabanyaclub",
    #     redirect_url="https://t.me/test_voimant_2_bot",
    #     storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    # )
    # tokens.default_token_manager.init(code="def50200947fa0295c8a3850124f47a9e87610c1422627713cbf9e02779ba4a796c449bc5e791962fbeab7440e37cc1c228fae18228bcee6a18dea5a57317dba800d02aa9b983a61fc877b44d7a293ac4bd2ae9baa78007c5568eb5838e399a5e1fd70ca596326409b9817e5248368106885dd3540b421428d66190e6715714cccb7c8f08ed232313d77990226b521f7482f3a8572def8c003bfeb3e2ec1eee3af58c4b07816dd4daa854a2eb2ed4ea1d3692d7f6d6e0e1835f95974d41ce027307fbfe544bcd07665fc3c3d999a8c9d6921237dd3a119e529bc2b23ce9f4ac85b5faac7f7e8ea5d09d6950f03bb250c4c78dc46275c907055b9841b3738134e6967b28b4ca96c3da98ef60543bd7b31389d4a6250be8557b5957284caf02642709a37f9a9e5872387a0c03ad174e51030708237a35d05a003c2759fdcd96db8d4c5237b25ae40ab7072ad60e90c3ce13bc2bc96f129b5e9fed69b7383e81f7731041facb4c773292e17bb50edc8aaa7ff6ef2684ae6b4e4c22f4fb7520b388603ebafa78eef91ddd6bded2f5b7195b86b05171b6d8410ccaa3bb36916fe77bd060bab10fe199d6549c80cc06e2ac62b580c6ddfa54b6ee575114f74242ff33d6f4e591d2a4a9a3fe42cf25f4b7f611365b9ad06c59135e56d543a33b246710bd8ddd030761e55c044b4d2728ace4cf3", skip_error=False)