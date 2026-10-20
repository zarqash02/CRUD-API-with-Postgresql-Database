from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str | None
    done: bool
    created_at: datetime | None
    updated_at: datetime | None


class TaskCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1)
    done: bool = False


class TaskUpdate(BaseModel):
    model_config = (ConfigDict(str_strip_whitespace=True))

    title: Optional[str] = None
    done: Optional[bool] = None