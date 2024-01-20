from pydantic import BaseModel
from typing import List, Optional, Any

class WidgetSchema(BaseModel):
    id: Optional[str] = None
    name: str
    type: str
    dimension: Optional[str] = None
    measure: str