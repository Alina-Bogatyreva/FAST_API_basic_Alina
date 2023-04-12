from pydantic import BaseModel


class ManufacturerBase(BaseModel):
    name: str
    address: str
    coefficient_sale: float = None


class ManufacturerIn(ManufacturerBase):
    pass


class ManufacturerInPut(ManufacturerBase):
    name: str = None
    address: str = None


class ManufacturerOut(ManufacturerBase):
    id: int



