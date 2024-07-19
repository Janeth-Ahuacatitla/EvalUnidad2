from jwt import encode, decode

def solicita_token (dato:dict)->str:
    token:str=encode(payload=dato,key='tu_clave_secreta',algorithm='HS256')
    return token
def valida_token(token:str)->dict:
    dato:dict = decode(token,key='tu_clave_secreta',algorithms=['HS256'])
    return dato