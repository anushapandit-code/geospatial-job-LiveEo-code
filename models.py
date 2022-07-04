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


# create class for update request
class CustomerUpdateRequest(BaseModel):
    id: Optional[UUID] = uuid4()
    type_: Optional[Type]
    grid_file: Optional[str]
    pole_file: Optional[str]
    critical_distances: Optional[List]


