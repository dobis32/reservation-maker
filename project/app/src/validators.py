from  django.core.exceptions import ValidationError
import jwt
import os
import datetime
def reservationTimeValidator(value):
    try:
        tokens = value.upper().split('-')
        if len(tokens) != 3:
            raise Exception()
        int(tokens[0])
        int(tokens[1])
        if tokens[2] != 'AM' and tokens[2] != 'PM':
            raise Exception()
    except:
        print('TIME VALIDATOR FAILED')
        raise ValidationError('Invalid time')

def reservationDateValidator(value):
    try:
        tokens = value.split('-')
        if len(tokens) != 3:
            raise Exception()
        for t in tokens:
            if len(t) > 2:
                raise Exception()
            int(t)
    except:
        print('DATE VALIDATOR FAILED')
        raise ValidationError('Invalid date')

def adminValidator(token):
    try:
        decoded = jwt.decode(token, os.environ.get('JWT_SECRET'), algorithms='HS256')
        formatttedExpiration =(datetime.datetime.utcnow() + datetime.timedelta(minutes=30)).isoformat()
        headers = {'exp': formatttedExpiration}
        return str(jwt.encode({'username': decoded['username'], 'password': decoded['password']}, os.environ.get('JWT_SECRET'), algorithm='HS256', headers=headers))[1:].replace("'", "")
    except Exception as e:
        print(e)
        return False
    
