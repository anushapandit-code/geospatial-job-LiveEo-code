from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Type(str, Enum):
    type_2D = "2D"
    type_3D = "3D"


class Customer(BaseModel):
    id: Optional[UUID] = uuid4()
    type_: Type
    grid_file: str
    pole_file: str
    critical_distances: List




