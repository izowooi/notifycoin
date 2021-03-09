import requests

headers = {
            'Content-type': 'application/json',
                'Authorization': 'key=[__SERVER_KEY__]',
                }

data = '{ "to":"/topics/500won", "notification": { "title" : "hello!!", "message" : "world!!", }, "priority": "high" }'

response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, data=data)