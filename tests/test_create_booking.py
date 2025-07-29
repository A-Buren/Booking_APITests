import allure
import pytest
import requests
from pydantic import ValidationError
from core.models.booking import BookingResponse


@allure.feature('Test Creating Booking')
@allure.story('Positive: creating booking with random data')
def test_create_booking_with_random_data(api_client, generate_random_booking_data):
    response = api_client.create_booking(booking_dates=generate_random_booking_data)
    response_data = response['booking']
    response_dates = response['booking']['bookingdates']
    with allure.step("Проверка структуры ответа"):
        assert "bookingid" in response, "missing required field 'bookingid'"
        assert 'booking' in response, "missing required field 'booking'"
        assert isinstance(response_data, dict), (
            f"Field 'booking' should be dict, but got {type(response_data)}")
    with allure.step("Проверка формата данных в ответе"):
        assert response_data['firstname'] == generate_random_booking_data[
            'firstname'], f"Expected {generate_random_booking_data['firstname']}, but got {response_data['firstname']}"
        assert response_data['lastname'] == generate_random_booking_data[
            'lastname'], f"Expected {generate_random_booking_data['firstname']}, but got {response_data['firstname']}"
        assert response_data['totalprice'] == generate_random_booking_data[
            'totalprice'], f"Expected {generate_random_booking_data['totalprice']}, but got {response_data['totalprice']}"
        assert response_data['depositpaid'] == generate_random_booking_data[
            'depositpaid'], f"Expected {generate_random_booking_data['depositpaid']}, but got {response_data['depositpaid']}"
        assert response_data['additionalneeds'] == generate_random_booking_data[
            'additionalneeds'], f"Expected {generate_random_booking_data['additionalneeds']}, but got {response_data['additionalneeds']}"
        assert response_dates['checkin'] == generate_random_booking_data['bookingdates'][
            'checkin'], f"Expected {generate_random_booking_data['bookingdates']['checkin']}, but got {response_data['bookingdates']['checkin']}"
        assert response_dates['checkout'] == generate_random_booking_data['bookingdates'][
            'checkout'], f"Expected {generate_random_booking_data['bookingdates']['checkout']}, but got {response_data['bookingdates']['checkout']}"
        assert isinstance(response_dates, dict), (
            f"Field 'bookingdates' should be dict, but got {type(response_data['bookingdates'])}")
        assert response_dates['checkin'] < response_dates['checkout'], "'checkin' must be less than 'checkout'"
        assert response["bookingid"] > 0, "'bookingid' must be greater or equal then 1"

        try:
            BookingResponse(**response)
        except ValidationError as e:
            raise ValidationError(f"Response validation failed: {e}")


@allure.feature('Test Creating Booking')
@allure.story('Positive: creating booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")


@allure.feature('Test Creating Booking')
@allure.story('Negative: creating booking without data')
def test_create_booking_without_data(api_client):
    payload = None
    with allure.step("Попытка создания бронирования без данных"):
        with pytest.raises(requests.exceptions.HTTPError) as error_info:
            api_client.create_booking(booking_dates=payload)

    with allure.step('Проверка кода ошибки'):
        assert error_info.value.response.status_code == 500, ("Ожидался статус-код 500 при отсутствии данных")