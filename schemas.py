from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str 
    is_verified: Optional[bool] = False

class OTPVerify(BaseModel):
    email: EmailStr
    otp: str = Field(..., min_length=6, max_length=6)

class WorkerCreate(BaseModel):
    name: str
    mobile_number: str
    adhar: str
    working_time: str
    working_days: str
    salary: int

class WorkerOut(WorkerCreate):
    id: int

    class Config:
        from_attributes= True
