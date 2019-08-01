class ShortINputException(Exception):
    '''A user-defined exceprion class.'''
    def __init__(self,lenght,atleast):
        Exception.__init__(self)
        self.lenght = lenght
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text)<3:
        raise ShortINputException(len(text),3)
        # Other work can continue as usual here
except EOFError:
    print('Why did you do an EOF to me?')
except ShortINputException as ex:
    print('ShortInputException: The input was {0} long, expected at least {1}'.format(ex.lenght,ex.atleast))
else:
    print('No exception was raised')