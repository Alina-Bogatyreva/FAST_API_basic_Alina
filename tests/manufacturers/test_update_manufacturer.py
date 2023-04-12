import random
import string

import pytest



@pytest.mark.parametrize("name, address, coefficient_sale", [
    ("Biy","Nalchik", 22.2),
    ('Biy', "Nalchik",22.2),
    ("Biy", "Nalchik", 22.2)
])
def test_positive(manufacturer_fixture, name, address, coefficient_sale):
    manufacturer_id = manufacturer_fixture.manufacturer_id
    response = manufacturer_fixture.api_client.manufacturer.update_manufacturer(manufacturer_id, name,
                                                                                address, coefficient_sale)

    assert response.status_code == 200, "Статус код не соответствует ожидаемому"