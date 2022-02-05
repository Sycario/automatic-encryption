import hashlib
from tkinter import E

uname = input('word that will be encrypted:')
print('choose one of the encryptions sha512, sha256, md5, sha1')
tipo = input('chosen encryption:')
if (tipo) == 'sha512':
    hash = hashlib.sha512(str( uname ).encode("utf-8") ).hexdigest()
    print (hash)
elif tipo == 'sha256':
    hash1  = hashlib.sha256(str( uname ).encode("utf-8") ).hexdigest()
    print(hash1)
elif tipo == 'md5':
    hash2  = hashlib.md5(str( uname ).encode("utf-8") ).hexdigest()
    print(hash2)
elif tipo == 'sha1':
    hash3  = hashlib.sha1(str( uname ).encode("utf-8") ).hexdigest()
    print(hash3)
else:
    print('try again something is wrong')
    exit()
print('yes to continue, if you dont want to put no')
quant = (input('you want to repeat the encryption == '))
if quant == 'no':
    print('were done here thanks for using')
    print('==================================')
    print('made by Sycario')
    exit()
elif quant == 'yes':
    print('unique sha512 encryption that has been built yet')
    cripto = input('choose encryption == ')
    if cripto == 'sha512':
        print('ok lets go then')
    else:
        print('you put some command wrong')
        exit()
    vezes = int(input('how many times do you want to encrypt? (3 is the maximum) == ')) 
if vezes == 1:
        a = hashlib.sha512(str( hash ).encode("utf-8") ).hexdigest()
        print(a)
        print('WE ARE FINISHED HERE!!!')
        print('made by Sycario')
elif vezes == 2:
    r = hashlib.sha512(str( hash ).encode("utf-8") ).hexdigest()
    e = hashlib.sha512(str( r ).encode("utf-8") ).hexdigest()
    print(r)
    print('============================================================================================================================')
    print(e)
    print('WE ARE FINISHED HERE!!!')
    print('made by Sycario')
elif vezes == 3:
    f = hashlib.sha512(str( hash ).encode("utf-8") ).hexdigest()
    d = hashlib.sha512(str( f ).encode("utf-8") ).hexdigest()
    s = hashlib.sha512(str( d ).encode("utf-8") ).hexdigest()
    print(f)
    print('==============================================================================================================================')
    print(d)
    print('==============================================================================================================================')
    print(s)
    print('WE ARE FINISHED HERE!!!')
    print('made by Sycario')
else:
    print('you must have put some command wrong')
    exit()
