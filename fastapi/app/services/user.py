

from datetime import timedelta
from fastapi import HTTPException
from app.core.security import generate_token, load_user, verify_password

from app.core.config import get_settings

settings = get_settings()



async def get_login_token(data, db):
     # verify the email and password
    # Verify that user account is verified
    # Verify user account is active
    # generate access_token and refresh_token and ttl
    
    user = await load_user(data.username, db)
    if not user:
        raise HTTPException(status_code=400, detail="Email is not registered with us.")
    
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password.")
    
    if not user.verified_at:
        raise HTTPException(status_code=400, detail="Your account is not verified. Please check your email inbox to verify your account.")
    
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Your account has been dactivated. Please contact support.")
        
    # Generate the JWT Token
    token =  _generate_tokens(user)
    return token




def _generate_tokens(user):
    
    at_payload = {
        "sub": str(user.id),
    }

    at_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = generate_token(at_payload, settings.JWT_SECRET, settings.JWT_ALGORITHM, at_expires)
    return {
        "access_token": access_token,
        "refresh_token": None,
        "expires_in": at_expires.seconds
    }