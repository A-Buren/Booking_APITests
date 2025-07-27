import pytest
import allure
import requests
from conftest import api_client
from core.clients.api_client import APIClient


@allure.feature('Test CreateBooking')
@allure.story('Test connection')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(booking_dates=generate_random_booking_data)
    response_data = response['data']['booking']
    with allure.step("Проверка структуры ответа"):
        assert "bookingid" in response["data"], "missing required field 'bookingid'"
        assert 'booking' in response['data'], "missing required field 'booking'"
        assert isinstance(response_data, dict), (
            f"Field 'booking' should be dict, but got {type(response_data)}")
    with allure.step("Проверка формата данных в ответе"):
        assert response_data['firstname'] == generate_random_booking_data[
            'firstname'], f"Expected {generate_random_booking_data['firstname']}, but got {response_data['firstname']}"
        assert isinstance(response_data["firstname"], str), (
            f"Field 'firstname' should be str, but got {type(response_data['firstname'])}")
        assert response_data['lastname'] == generate_random_booking_data[
            'lastname'], f"Expected {generate_random_booking_data['firstname']}, but got {response_data['firstname']}"
        assert isinstance(response_data["lastname"], str), (
            f"Field 'lastname' should be str, but got {type(response_data['lastname'])}")
        assert response_data['totalprice'] == generate_random_booking_data[
            'totalprice'], f"Expected {generate_random_booking_data['totalprice']}, but got {response_data['totalprice']}"
        assert isinstance(response_data["totalprice"], int), (
            f"Field 'totalprice' should be int, but got {type(response_data['totalprice'])}")
        assert response_data['depositpaid'] == generate_random_booking_data[
            'depositpaid'], f"Expected {generate_random_booking_data['depositpaid']}, but got {response_data['depositpaid']}"
        assert isinstance(response_data["depositpaid"], bool), (
            f"Field 'depositpaid' should be bool, but got {type(response_data['depositpaid'])}")
        assert response_data['additionalneeds'] == generate_random_booking_data[
            'additionalneeds'], f"Expected {generate_random_booking_data['additionalneeds']}, but got {response_data['additionalneeds']}"
        assert isinstance(response["data"]["booking"]["additionalneeds"], str), (
            f"Field 'additionalneeds' should be str, but got {type(response_data['additionalneeds'])}")
        assert response_data['bookingdates']['checkin'] == generate_random_booking_data['bookingdates'][
            'checkin'], f"Expected {generate_random_booking_data['bookingdates']['checkin']}, but got {response_data['bookingdates']['checkin']}"
        assert isinstance(response_data['bookingdates']['checkin'], str), (
            f"Field 'checkin' should be str, but got {type(response_data['bookingdates']['checkin'])}")
        assert response_data['bookingdates']['checkout'] == generate_random_booking_data['bookingdates'][
            'checkout'], f"Expected {generate_random_booking_data['bookingdates']['checkout']}, but got {response_data['bookingdates']['checkout']}"
        assert isinstance(response_data['bookingdates']['checkout'], str), (
            f"Field 'checkout' should be str, but got {type(response_data['checkout'])}")
        assert isinstance(response_data["bookingdates"], dict), (
            f"Field 'bookingdates' should be dict, but got {type(response_data['bookingdates'])}")
