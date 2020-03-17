class Token():
    def __init__(self,value,typee):
        self._typee=typee
        self._value=value
    def __repr__(self):
        return  f"value :{self._value}  type:{self._typee}"
    def __str__(self):
        return  f"value :{self._value}  type:{self._typee}"
    def __eq__(self, value):
        if type(self)==Token and type(value)==Token:
            if (self._value==value._value and self._typee==value._typee):
                 return True
            return False
        else:
            return False


