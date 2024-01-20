from fastapi import FastAPI

from app.core.config import get_settings
from app.routes.user import auth_router, guest_router
from app.routes.widget import widget_router
from fastapi.middleware.cors import CORSMiddleware

settings = get_settings()


def create_application():
    application = FastAPI(title=settings.APP_NAME, version=settings.VERSION, debug=settings.DEBUG)
    application.include_router(guest_router)
    application.include_router(auth_router)
    application.include_router(widget_router)
    return application


app = create_application()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

