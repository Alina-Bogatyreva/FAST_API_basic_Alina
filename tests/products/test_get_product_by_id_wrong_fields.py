import pytest


@pytest.mark.parametrize("product_id, exp_code", [
    ("wrong_id", 422),
    ([1], 422),
    (9999999999, 404)
])
def test_negative(product_fixture, product_id, exp_code):
    response = product_fixture.api_client.product.get_product_by_id(product_id)
    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"
