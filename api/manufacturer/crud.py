"""
Create
Read
Update
Delete
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.manufacturer.schemas import ManufacturerIn, ManufacturerOut, ManufacturerInPut
from db import db_manufacturer


class Manufacturer:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_manufacturer(self, manufacturer_in: ManufacturerIn) -> ManufacturerOut:
        manufacturer = db_manufacturer.create_manufacturer(self.db_session, **manufacturer_in.dict())
        manufacturer_out = ManufacturerOut(id=manufacturer.id, name=manufacturer.name, address=manufacturer.address,
                                           coefficient_sale=manufacturer.coefficient_sale)
        return manufacturer_out

    def get_manufacturer_by_id(self, manufacturer_id: int):
        manufacturer = db_manufacturer.get_manufacturer_by_id(self.db_session, manufacturer_id)
        if manufacturer:  # ==  if user is not None
            return ManufacturerOut(id=manufacturer.id, name=manufacturer.name, address=manufacturer.address,
                                   coefficient_sale=manufacturer.coefficient_sale)
        else:
            raise HTTPException(status_code=404, detail={"message": "Manufacturer not found!"})

    def get_manufacturers(self) -> list[ManufacturerOut]:
        results = db_manufacturer.get_all_manufacturers(self.db_session)
        manufacturer_outs = []
        for m in results:
            mo = ManufacturerOut(id=m.id, name=m.name, address=m.address, coefficient_sale=m.coefficient_sale)
            manufacturer_outs.append(mo)
        return manufacturer_outs

    def put_manufacturer(self, manufacturer_id: int, manufacturer_in: ManufacturerInPut) -> ManufacturerOut:
        manufacturer = db_manufacturer.update_manufacturer(self.db_session, manufacturer_id, manufacturer_in)
        if manufacturer:
            return ManufacturerOut(id=manufacturer.id, name=manufacturer.name, address=manufacturer.address,
                                   coefficient_sale=manufacturer.coefficient_sale)
        else:
            raise HTTPException(status_code=404, detail={"message": "Manufacturer not found!"})

    def delete_manufacturer(self, manufacturer_id: int) -> None:
        if not db_manufacturer.delete_manufacturer(self.db_session, manufacturer_id):
            raise HTTPException(status_code=404, detail={"message": "Manufacturer not found!"})