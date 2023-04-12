import pytest


@pytest.mark.parametrize("product_id, exp_code", [
    ("wrong_id", 422),
    ([1], 422),
    (9999999999, 404)
])
def test_negative(product_fixture, product_id, exp_code):
    response = product_fixture.api_client.product.delete_product(product_id)
    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
