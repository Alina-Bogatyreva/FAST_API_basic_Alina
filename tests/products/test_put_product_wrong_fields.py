import pytest
import random


@pytest.mark.parametrize("new_name, new_price, new_dimension, exp_code", [
    ([25], None, None, 422),
    (None, 'test_price', None, 422),
    (None, None, {"length": 'test_length',
                  "width": random.uniform(1, 100000),
                  "height": random.uniform(1, 100000)
                  }, 422)
])
def test_negative(product_fixture, new_name, new_price, new_dimension, exp_code):
    product_id = product_fixture.product_id

    response = product_fixture.api_client.product.update_product(product_id,  new_name, new_price, new_dimension)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"