import pytest

from tests.configuration import ROLE_ENUM


@pytest.mark.parametrize("employee_id, exp_code", [
    ("wrong_id", 422),
    ([1], 422),
    (9999999999, 404)
])
def test_positive(employee_fixture, employee_id, exp_code):
    response = employee_fixture.api_client.user.delete_user(employee_id)
    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"