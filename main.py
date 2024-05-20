import pytest
import requests
import allure


"""HELPERS"""


FORCES_LIST_URL = "https://data.police.uk/api/forces"


def get_specific_force(force_id):
    specific_force = requests.get(f"{FORCES_LIST_URL}/{force_id}")
    return specific_force.json()


"""FIXTURES"""


@pytest.fixture()
@allure.title("true_scalene_triangle")
def get_forces_list():
    forces_list = requests.get(FORCES_LIST_URL)
    return forces_list.json()


"""TESTS"""


class TestForces:
    @allure.title("test_specific_force_url")
    @allure.description("test_specific_force_url")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_specific_force_url(self, get_forces_list):
        dns_name = "police.uk"
        for force in get_forces_list:
            force_name = force['name']
            with allure.step(f"test the force id is true for the force: {force_name}"):
                assert force['id'], f"There no the force for force: {force_name}"
            force_id = force['id']
            with allure.step(f"test the dns name: {dns_name} in {force_id}"):
                specific_force = get_specific_force(force_id)
                specific_force_url = specific_force["url"]
                assert specific_force, f"There no the specific force for the force with id: {force_id}"
                assert specific_force_url, f"There no the specific force url for the force id: {force_id}"
                assert dns_name in specific_force_url, \
                    f"There no the dns name: {dns_name} in the specific force url: {specific_force_url}"
