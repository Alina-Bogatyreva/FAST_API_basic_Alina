from typing import Optional

from app.db.models import Manufacturer


def get_manufacturer_by_id(db_session, manufacturer_id) -> Optional[Manufacturer]:
    return db_session.query(Manufacturer).filter_by(id=manufacturer_id).first()


def get_manufacturer_by_name(db_session, name) -> list:
    return db_session.query(Manufacturer).filter_by(name=name).all()


def get_all_manufacturers(db_session):
    manufacturers = db_session.query(Manufacturer).all()
    return manufacturers


def create_manufacturer(db_session, name=None, address=None, coefficient_sale=None):
    manufacturer = Manufacturer(name=name, address=address, coefficient_sale=coefficient_sale)
    db_session.add(manufacturer)
    db_session.commit()
    db_session.refresh(manufacturer)
    return manufacturer


def update_manufacturer(db_session, manufacturer_id, new_manufacturer):
    old_manufacturer = get_manufacturer_by_id(db_session, manufacturer_id)
    if old_manufacturer is not None:
        old_manufacturer.name = new_manufacturer.name if new_manufacturer.name is not None else old_manufacturer.name
        if new_manufacturer.address is not None:
            old_manufacturer.address = new_manufacturer.address
        else:
            old_manufacturer.address = old_manufacturer.address

        if new_manufacturer.coefficient_sale is not None:
            old_manufacturer.coefficient_sale = new_manufacturer.coefficient_sale
        else:
            old_manufacturer.coefficient_sale = old_manufacturer.coefficient_sale

        db_session.commit()
        db_session.refresh(old_manufacturer)
        return old_manufacturer


def delete_manufacturer(db_session, manufacturer_id: int):
    manufacturer = get_manufacturer_by_id(db_session, manufacturer_id)
    if manufacturer:
        db_session.delete(manufacturer)
        db_session.commit()
        return True
    else:
        return False
