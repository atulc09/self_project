from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import models
import schemas
import utils
from database import engine,get_db
from jose import jwt
from datetime import datetime,timedelta,timezone
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import JWTError
import auth 
 
# OAuth2 scheme - define once at module level
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#HELPER function that take user data 
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc) + timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    encode_jwt=jwt.encode(to_encode,auth.SECRET_KEY,algorithm=auth.ALGORITHM)
    return encode_jwt

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "Shoap backend running"}

@app.post("/signup")
def register_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    #check the user exist or not 
    existing_user=db.query(models.User).filter(models.User.username== user.username).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="user already exist")
    
    #hash the password
    password_hashed=utils.get_password_hash(user.password)
             
    #create new user instance
    new_user=models.User(
        username=user.username,
        email=user.email,
        password_hash=.password_hashed,
        is_verified=user.is_verified
    )

    #save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    #return the value of (excluding password)
    return {"id":new_user.id,"username":new_user.username,"email":new_user.email,"is_verified":new_user.is_verified}





