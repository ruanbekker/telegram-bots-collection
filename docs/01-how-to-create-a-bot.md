## How to create a Telegram Bot

Open a chat with BotFather:

<img width="807" alt="image" src="https://user-images.githubusercontent.com/567298/120043871-0cfdce80-c00d-11eb-8675-664f38cce37e.png">

Send a message with `/newbot`:

<img width="550" alt="image" src="https://user-images.githubusercontent.com/567298/120043938-256de900-c00d-11eb-8362-bd24407dc954.png">

etc: `MyAlarm`

<img width="550" alt="image" src="https://user-images.githubusercontent.com/567298/120043994-3e769a00-c00d-11eb-83ee-4a39173aa815.png">

etc: `MyAlarmBot`:

<img width="1096" alt="image" src="https://user-images.githubusercontent.com/567298/120044147-91e8e800-c00d-11eb-9f85-39b2542462eb.png">

Your Telegram Bot is now reachable on t.me/MyAlarm_Bot (dummy name ie. non-existent) and from the token that was received, I will use that for demonstration purposes as $TELEGRAM_BOT_TOKEN .

Open:
https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates?offset=0

Send message to bot, then refresh link, or use curl:

```
curl -s https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates | jq -r '.result[].message.chat.id'
14xxxxx99
```

A full response will look like this:

```json
{
  "ok":true,
  "result":[
    {
      "update_id":xxxxxxx50,
      "message":{
        "message_id":3,
        "from":{
          "id":xxxxxxx99,
          "is_bot":false,
          "first_name":"xxxxxxxxx",
          "last_name":"xxxxxx",
          "username":"xxxxxxxxxxxxx",
          "language_code":"en"
        },
        "chat":{
          "id":14xxxxx99,
          "first_name":"xxxxxxx", 
          last_name":"xxxxxxxx",
          "username":"xxxxxxxxxxxxx",
          "type":"private"
        },
        "date":16xxxxxx26,
        "text":"hi"
      }
    }
  ]
}
```

Send a notification to Telegram with curl:

```bash
curl -XPOST -H 'Content-Type: application/json' -d '{"chat_id": "14xxxxx99", "text": "This is a test from curl", "disable_notification": false}' https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage
{
  "ok":true,
  "result":{
    "message_id":7,
    "from":{
      "id":15xxxxxx77,
      "is_bot":true,
      "first_name":"MyAlarmBot",
      "username":"MyAlarm_Bot"
    },
    "chat":{
      "id":142714999,
      "first_name":"xxxxxxx",
      "last_name":"xxxxxxxxx",
      "username":"xxxxxxxxxxxxx",
      "type":"private"
    },
    "date":162xxxxxx3,
    "text":"This is a test from curl"
  }
}
```

<img width="1087" alt="image" src="https://user-images.githubusercontent.com/567298/120155035-c10b7f00-c1f0-11eb-946e-9d19c8d06984.png">


To add your bot to a group, select your bot, then add to group.

Then use the `/getUpdates` method to get the group id:

```
curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates | jq .
{
  "ok": true,
  "result": [
    {
     ...,
      "update_id": xxxxxxxxx,
      "my_chat_member": {
        "chat": {
          "id": -xxxxxxxxx,
          "title": "GroupName",
          "type": "group",
          "all_members_are_administrators": true
        },
        ...
      }
    }
  ]
}
```

Group ID's are always with `-` in the beginning

Resources:
- https://docs.influxdata.com/kapacitor/v1.5/event_handlers/telegram/
- https://github.com/n8n-io/n8n/tree/master/docker/compose/withPostgres
- https://gist.github.com/dideler/85de4d64f66c1966788c1b2304b9caf1
