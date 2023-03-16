import pytest

from tests.configuration import ROLE_ENUM


@pytest.mark.parametrize("employee_id", [
    ("wrong_id"),
    ([1]),
    (9999999999)
])
def test_positive(employee_fixture, employee_id):
    response = employee_fixture.api_client.user.delete_user(employee_id)
    assert response.status_code == 422 or 404, "Статус код не соответствует ожидаемому"