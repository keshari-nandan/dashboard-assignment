

from datetime import datetime
import uuid
from fastapi import HTTPException
from app.models.dashboard import DashboardModel

async def get_widgets(user, db):
    dashboard = db.query(DashboardModel).filter(DashboardModel.user_id == user.id).first()
    widgets = dashboard.config if dashboard.config else []
    return widgets


async def save_widget(user, data, db):
    dashboard = db.query(DashboardModel).filter(DashboardModel.user_id == user.id).first()
    print(data)
    widgets = dashboard.config if dashboard.config else []
    widgetData = {
        'name': data.name,
        'type': data.type,
        'dimension': data.dimension if data.dimension else None,
        'measure': data.measure
    }
    all_widget = []
    if data.id:
        requested_widget = next((item for item in widgets if item['id'] == data.id), None)
        if not requested_widget:
            raise HTTPException(status_code=404, detail="Widget not found")
        for wdgt in widgets:
            if wdgt.get('id', None) == data.id:
                all_widget.append({**wdgt, **widgetData})
            else:
                all_widget.append(wdgt)
    else:
        all_widget = widgets
        widgetData['id'] = str(uuid.uuid4())
        all_widget.append(widgetData)

    db.query(DashboardModel).filter(DashboardModel.user_id == user.id).update({"config": all_widget, "updated_at": datetime.now()}, synchronize_session=False)
    db.commit()
    db.refresh(dashboard)
    return dashboard
    
    
async def delete_widget(user, widget_id, db):
    dashboard = db.query(DashboardModel).filter(DashboardModel.user_id == user.id).first()
    widgets = dashboard.config if dashboard.config else []
    widget_list = [widget for widget in widgets if widget.get('id', None) != widget_id]
    dashboard.config = widget_list
    dashboard.updated_at = datetime.now()
    db.add(dashboard)
    db.commit()
    return dashboard