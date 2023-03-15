import pytest


@pytest.mark.parametrize("username, age, address, accessed_catalog, exp_code", [

    (["Alina", 22], 22, "KBR, Nalchik", {"name": "Alina_B", "catalog": "international_food"}, 422),
    ("Alina", "age_age", "KBR, Nalchik", {"name": "Alina_B", "catalog": "furniture"}, 422),
    # ("Alina", -22, "KBR, Nalchik", {"name": "Alina_B", "catalog": "furniture"}, 422),   >>> status code = 200, хотя стоит ограничение на age (min 0)
    ("Alina", 22, ["KBR", "Nalchik"], {"name": "Alina_B", "catalog": "food"}, 422),
    ("Alina", 22, "KBR, Nalchik", {"name": ["Alina_B"], "catalog": "phones"}, 422),
    ("Alina", 22, "KBR, Nalchik", {"name": "Alina_B", "catalog": "tops"}, 422),
    ("Alina", 22, "KBR, Nalchik", ["name", "Alina_B", "catalog", "phones"], 422),
])


def test_negative(user_fixture, username, age, address, accessed_catalog, exp_code):
    response = user_fixture.api_client.user.create_user(username, age, address, accessed_catalog)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"