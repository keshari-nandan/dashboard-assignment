from fastapi import APIRouter, Depends, status
from app.schemas.widgets import WidgetSchema
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import widgets
from app.core.security import get_current_user, oauth2_scheme

widget_router = APIRouter(
    prefix="/widgets",
    tags=["Widgets"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(oauth2_scheme), Depends(get_current_user)]
)

@widget_router.get("", status_code=status.HTTP_200_OK)
async def get_widgets(user = Depends(get_current_user), db: Session = Depends(get_db)):
    return await widgets.get_widgets(user, db)

@widget_router.put("", status_code=status.HTTP_200_OK)
async def save_widget(data: WidgetSchema, user = Depends(get_current_user), db: Session = Depends(get_db)):
    return await widgets.save_widget(user, data, db)


@widget_router.delete("/{pk}", status_code=status.HTTP_200_OK)
async def delete_widget(pk, user = Depends(get_current_user), db: Session = Depends(get_db)):
    return await widgets.delete_widget(user, pk, db)
