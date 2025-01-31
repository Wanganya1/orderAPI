import africastalking

africastalking.initialize(username='your-username', api_key='your-api-key')

sms = africastalking.SMS

def send_sms(phone_number, message):
    response = sms.send(message, [phone_number])
    return response

