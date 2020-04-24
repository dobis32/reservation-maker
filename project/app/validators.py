from  django.core.exceptions import ValidationError

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
