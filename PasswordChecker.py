import string
import sys



def LowerUpperChecker(text):
    LowerUpperFlag = 1
    if text.lower()==text or text.upper()==text:
        LowerUpperFlag = 0
        
    return LowerUpperFlag

def DigitChecker(text):
    DigitFlag = 0
    for i in text:
        if i in string.digits:
            DigitFlag = 1
            break
        
    return DigitFlag

def PunctuationCharChecker(text):
    PunctuationCharFlag = 0
    for i in text:
        if i in string.punctuation:
            PunctuationCharFlag = 1
            break
        
    return PunctuationCharFlag
    
def LengthChecker(text):
    LengthFlag = 0
    if len(text)>=14:
        LengthFlag = 1
        
    return LengthFlag

if __name__=='__main__':
    try:
        password = sys.argv[1]
        ValidFlag = 1
        if not LowerUpperChecker(password):
            if ValidFlag: print('Weak password:')
            ValidFlag = 0
            print(' - Password must contain both lowercase and uppercase characters')
           
        if not DigitChecker(password):
            if ValidFlag: print('Weak password:')
            ValidFlag = 0
            print(' - Password must contain digits')
            
        if not PunctuationCharChecker(password):
            if ValidFlag: print('Weak password:')
            ValidFlag = 0
            print(' - Password must contain at least one punctuation character (!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~)')
            
        if not LengthChecker(password):
            if ValidFlag: print('Weak password:')
            ValidFlag = 0
            print(' - Password must be at least 14 characters long')
            
        if ValidFlag:
            print('Strong password')
    except BaseException:
        print('Write password please')
    















