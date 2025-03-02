import pytest
import allure
import requests


@allure.feature('Test CreateBooking')
@allure.story('Test connection')
def test_create(api_client):
    status_code = api_client.create_booking()
    assert status_code == 200, f"Expected status code 200 but got {status_code}"


@allure.feature('Test CreateBooking')
@allure.story('Test connection')
def test_create_server_unavailable(api_client, mocker):
    mocker.patch.object(api_client.session, 'post', side_effect=Exception("Server unavailable"))
    with pytest.raises(Exception, match="Server unavailable"):
        api_client.ping()