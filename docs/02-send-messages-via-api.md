# Sending Messages

This demonstrates how to find your chat id and how to use curl to send a message from your bot to yourself.

## Examples

To get your chat id, go to your bot and send your bot any message.

Then make a request to telegram's api to [getupdates](https://core.telegram.org/bots/api#getupdates) method:

```bash
curl -s "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getUpdates?limit=1"  | jq .
{
  "ok": true,
  "result": [
    {
      "update_id": xxxxxxxx,
      "message": {
        "message_id": 489,
        "from": {
          "id": 14xxxxxxxxxx,
          "is_bot": false,
          "first_name": "Ruan",
          "last_name": "xxxx",
          "username": "xxxxxxxxxxxxxx",
          "language_code": "en"
        },
        "chat": {
          "id": 14xxxxxxxxxx,
          "first_name": "Ruan",
          "last_name": "xxxx",
          "username": "xxxxxxxxxxxxxx",
          "type": "private"
        },
        "date": 1655379616,
        "text": "a"
      }
    }
  ]
}
```

Now that we have the chat id, we can make a request to the [sendmessage](https://core.telegram.org/bots/api#sendmessage) method:

```bash
$ curl -s -XPOST -H 'Content-Type: application/json' https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage \
  -d '{"chat_id": "14xxxxxxxxxx", "text": "This is a test from curl", "disable_notification": false}' | jq .
  
{
  "ok": true,
  "result": {
    "message_id": 496,
    "from": {
      "id": 6xxxxxxxxxx,
      "is_bot": true,
      "first_name": "xxxxxxxxx",
      "username": "xxxxxxxx_bot"
    },
    "chat": {
      "id": 14xxxxxxxxxx,
      "first_name": "Ruan",
      "last_name": "xxxxxxx",
      "username": "xxxxxxxxxxxx",
      "type": "private"
    },
    "date": 1655380321,
    "text": "This is a test from curl"
  }
}
```

To edit the message we can use the [editMessageText](https://core.telegram.org/bots/api#editmessagetext) method:

```bash
$ curl -s -XPOST -H 'Content-Type: application/json' https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/editMessageText \
  -d '{"chat_id": "14xxxxxxxxxx", "message_id": 496, "text": "This is a edited test from curl", "disable_notification": false}' | jq .
{
  "ok": true,
  "result": {
    "message_id": 496,
    "from": {
      "id": 6xxxxxxxxxx,
      "is_bot": true,
      "first_name": "xxxxxxxxxx",
      "username": "6xxxxxxxxxx_bot"
    },
    "chat": {
      "id": 14xxxxxxxxxx,
      "first_name": "Ruan",
      "last_name": "xxxxx",
      "username": "xxxxxxxxxxxxxx",
      "type": "private"
    },
    "date": 1655380321,
    "edit_date": 1655380614,
    "text": "This is a edited test from curl"
  }
}
```
