import pytest


@pytest.mark.parametrize("employee_id, exp_code", [
    ("wrong_id", 422),
    ([1], 422),
    (999999999, 404)
])
def test_negative(employee_fixture, employee_id, exp_code):
    response = employee_fixture.api_client.employee.get_employee_by_id(employee_id)
    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"