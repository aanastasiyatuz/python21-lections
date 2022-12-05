import time
import jwt


SECRET_KEY = '3ah%_q!cr#3vj$4=9$jk&4+^w-20-gu)4zf#mtshhrfj3tkt%&'
JWT_ALGO = 'HS256'
JWT_ACCESS_TOKEN_EXPIRE = 10  # секунды

def signJWT(data: str):
    payload_access = {
        "data": data,
        "expiry": time.time() + JWT_ACCESS_TOKEN_EXPIRE
    }
    access_token = jwt.encode(payload_access, SECRET_KEY, algorithm=JWT_ALGO)
    return {"access": access_token}

def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGO])
        return decoded_token if decoded_token["expiry"] >= time.time() else None
    except:
        return {}

def verify_jwt(jwtoken: str) -> bool:
    payload = decodeJWT(jwtoken)
    if payload:
        return True
    return False
