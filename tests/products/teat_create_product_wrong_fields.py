import random
import pytest


@pytest.mark.parametrize("name, price, dimension, exp_code", [
    (['test_name'], random.randint(0, 1000000), None, 422),
    ('test_name', 'test_price', None, 422),
    ('test_name', random.randint(0, 1000000),
     {"length": random.uniform(1, 100000),
      "width": 'test_width',
      "height": random.uniform(1, 100000)
      }, 422)
])
def test_negative(product_fixture, name, price, dimension, exp_code):
    # request execution
    response = product_fixture.api_client.product.create_product(name, price, dimension)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
