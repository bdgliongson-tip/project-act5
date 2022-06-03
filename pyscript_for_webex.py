import requests
import json


def main():
    notif = input("enter message: ")
    input_message = notif
    access_token = 'NzA3NGY4MTctZTY4MC00NzI0LTgzMTItODFkZWExNDU0OWYwNThlN2M5YmYtZTIx_P0A1_af949325-f1e2-44dc-a297-78a9bdf6f617'
    room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZjEyMzliZjAtZGYzYi0xMWVjLTk1OGEtZjkwZjIxZDllZWY1'
    message = input_message
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params = {'roomId': room_id, 'markdown': message}
    res = requests.post(url, headers=headers, json=params)
    print(res.json())


if __name__ == '__main__':
    main()
