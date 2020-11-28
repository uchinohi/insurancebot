from .database import Query

class Option:

    def __init__(self,op, num):
        self.op = op
        self.num = num


    def one(self):
        return "Yaay premium calculation - paisa hi paisa hoga"

    def two(self):
        claims = Query.return_claims(self.num)
        noclaims = len(claims)
        if noclaims==0:
            message = f'Sorry, you have no active claims at the moment.'
        elif noclaims==1:
            message = f'You only have one claim active. Here:\n1. {next(iter(claims))}.\nType the claim number to view details.'
        else:
            claimiter = iter(claims)
            message = f'Here are two of your most recent claims:\n1. {next(claimiter)}\n2. {next(claimiter)}\nType the respective claim number or enter it manually to get details of a specific claim.'
        return message

    def three(self):
        return "Yayya renewal, more money"

    def four(self):
        return "Yayay your policies (not enough, get more)"

    def five(self):
        return "you get sick, we get rich"

    def six(self):
        return "download awayyy"

    def executeOption(self):
        switcher = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five,
            '6': self.six
        }

        func = switcher.get(self.op, lambda: 'Invalid Choice')

        return func()
        
