from email import message
import smtplib

from email.message import EmailMessage

message = EmailMessage()
def send_mail(send_to):
  message['from'] = 'sagar '
  message['to'] = send_to
  message['subject'] = ' confirmation'
  message.set_content('here we go python\n i have got your request ')
  
  with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyaccont1999@gmail.com', 'vkwtcjhiydxbfjqu')
    smtp.send_message(message)
    print("all good ")
  