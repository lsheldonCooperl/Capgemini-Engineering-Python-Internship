#describing of script
#first 3 conditions mean that password have to contain at least one lower letter,
#upper letter,digit and punctuation char. So, in algo I randomly choose the length
#of password(using normal distribution), randomly generate all symbols instead of
#the obvious 4. Last 4 choose from their corresponding sets, and randomly insert
#into already generated password.
import random
import string

def push(string, symbol):#insert symbol into random place of string
    order = random.randint(0,len(string))
    return string[:order]+symbol+string[order:]

if __name__=="__main__":
    password = ''
    symbols = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    #symbols - string, that contains all valid symbols

    length = 14+int(abs(random.gauss(0,5)))
    for i in range(length-4):
        password+=symbols[random.randint(0,len(symbols)-1)]

    lowerLetter = string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase)-1)]
    upperLetter = string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase)-1)]
    digit = string.digits[random.randint(0,len(string.digits)-1)]
    punct = string.punctuation[random.randint(0,len(string.punctuation)-1)]
    # obvious chars
    
    password = push(password,lowerLetter)
    password = push(password,upperLetter)
    password = push(password,digit)
    password = push(password,punct)

    print(password)

