import random
import string
import pytest

from tests.clients.clients_bundle import employee_client
from tests.configuration import ROLE_ENUM
from tests.checkers.general import CheckerGeneral


# add parametrize
# 1 case: name = "test_" + "".join(random.sample(string.ascii_letters, 5)), role=None
# 2 case: name = None role=admin
# 3 case: name = None, role=expert
# 4 case: name = None, role=seller
# 5 case: name = "test_" + "".join(random.sample(string.ascii_letters, 5)), role=random.choice(ROLE_ENUM)



@pytest.mark.parametrize("name, role", [
    ("".join(random.sample(string.ascii_letters, 5)), None),
    (None, "admin"),
    (None, "expert"),
    (None, "seller"),
    ("".join(random.sample(string.ascii_letters, 5)), random.choice(ROLE_ENUM))
])


def test_positive(name, role):
    # precondition - предусловие. Создание данных
    # name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    # role = random.choice(ROLE_ENUM)http://127.0.0.1/docs

    # request execution
    response = employee_client.create_employee(name, role)


    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert CheckerGeneral().validate_json(response.json(), "schemas/employee.json")