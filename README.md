# notifycoin
코인 알리미


## CURL TEST
curl -i -H 'Content-type: application/json' -H 'Authorization: key=[__SERVER_KEY__]' -XPOST https://fcm.googleapis.com/fcm/send -d '{
  "to":"/topics/500won",
  "notification": {
    "title" : "hello!!",
    "message" : "world!!",
  },
  "priority": "high"
}'