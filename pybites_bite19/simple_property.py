from datetime import datetime

NOW = datetime.now()


class Promo:
    from datetime import datetime, timedelta

NOW = datetime.now()
now = NOW

future = NOW + timedelta(days=1)
past = NOW - timedelta(seconds=3)

class Promo:  
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires
        
    def __str__(self):
        return f"{self.name}"
    
    @property    
    def expired(self):
        return self.expires == past
        
    def for_future(self):
        return self.expires == future
        
    def property1(self):
        #for n in future:
        if n > now:
            return True
        else:
            return False
            
        return property1
        
