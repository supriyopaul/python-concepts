'''
Design a notification system using Factory Method pattern with different delivery channels.

Requirements:
- Create an abstract Notification class with methods: `send(message, recipient)` and `format_message(message)`
- Implement concrete notification classes:
  - EmailNotification: formats with subject line and HTML
  - SMSNotification: formats with character limit (160 chars)
  - PushNotification: formats with title and body
  - SlackNotification: formats with channel and mentions
- Create a NotificationFactory with method `create_notification(channel_type, **config)`
- Each notification type should accept different configuration:
  - Email: smtp_server, sender_email
  - SMS: service_provider, api_key
  - Push: app_id, platform
  - Slack: workspace, bot_token
- Add a NotificationManager class that uses the factory to send bulk notifications
- Include error handling for unsupported channels and missing configuration

Example usage:
```python
manager = NotificationManager()
manager.send_notification("email", "Hello World!", "user@example.com", 
                         smtp_server="smtp.gmail.com", sender_email="admin@company.com")
manager.send_notification("sms", "Your order is ready!", "+1234567890",
                         service_provider="twilio", api_key="abc123")
```

Expected behavior:

Email should format with proper headers and HTML structure
SMS should truncate long messages and add "..." if needed
Push should create structured payload with title/body
Slack should format with proper markdown and channel notation
'''