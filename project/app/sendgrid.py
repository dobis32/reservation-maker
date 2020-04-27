import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()
def getSendgridClient():
    try:
        return SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    except Exception as e:
        print(e)
        return False

def sendSingleEmail(nonce, email_to, email_content):
    confirmationEmail = Mail(
    from_email='admin@reso.maker',
    to_emails=email_to,
    subject='Rservation Confirmation',
    html_content=email_content
    )
    sg = getSendgridClient()
    if not sg:
        return False
    else:
        response = sg.send(confirmationEmail)
        return handleSgResponse(response)


def sendReservationConfirmation(nonce, email_to):
    print('send reservation confirmation email')
    email_content = '<h1>We need you to confirm your reservation!</h1><h2><a href="http://localhost:8000/reservation/confirm?id={n}">Click here to confirm your reservation.</a></h2>'.format(n = nonce)
    return sendSingleEmail(nonce, email_to, email_content)


def sendClientVerification(nonce, email_to):
    print('send client verification email')
    result = None
    try:
        email_content = '<h1>Greetings!</h1><h2>We need you fill out some basic information for us.</h2><h2><a href="http://localhost:8000/clients/verify?id={n}">Click here to fill-out our new-client form!</a></h2>'.format(n = nonce)
        result = sendSingleEmail(nonce, email_to, email_content)
        return result
    except Exception as e:
        print(e)
        result = False
    finally:
        return result


def handleSgResponse(response):
    print('RESPONSE STATUS CODE', response.status_code)
    if 199 < response.status_code < 300:
        return True
    else:
        return False
