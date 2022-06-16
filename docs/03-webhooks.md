# Webhooks

## Docs

- https://core.telegram.org/bots/api#setwebhook

## Examples

Run a web service that accepts post requests:

```
$ docker run -itd --name webhook -p 5000:5000 ruanbekker/webhook
$ ngrok http 5000
```

Set webhook:

```
$ curl -H "Content-Type: application/json" -XPOST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebhook -d '{"url": "https://x-x-x-x-x.ngrok.io"}'
{"ok":true,"result":true,"description":"Webhook was set"}
```

View webhook:

```
$ curl -s https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getWebhookInfo | jq .
{
  "ok": true,
  "result": {
    "url": "https://x-x-x-x-x.ngrok.io",
    "has_custom_certificate": false,
    "pending_update_count": 0,
    "max_connections": 40,
    "ip_address": "x.x.x.x"
  }
}
```

Send a message to your bot, then view the webhook server logs:

```
$ docker logs -f webhook
172.17.0.1 - - [16/Jun/2022 11:21:50] "POST / HTTP/1.1" 200 -
{
  'update_id': 621204569, 
  'message': {
    'message_id': 488, 
    'from': {
      'id': xxxxxxxx, 
      'is_bot': False, 
      'first_name': 'Ruan', 
      'last_name': 'xxxx', 
      'username': 'xxxxxxxxxxxxxxxx', 
      'language_code': 'en'
    }, 
    'chat': {
      'id': xxxxxxxx, 
      'first_name': 'Ruan', 
      'last_name': 'xxxx', 
      'username': 'xxxxxxxxxxxxxxxx', 
      'type': 'private'
    }, 
    'date': 1655379141, 
    'text': 'hello'
  }
}
```

Delete webhook:

```
$ curl -s https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/deleteWebhook
{"ok":true,"result":true,"description":"Webhook was deleted"}
```
