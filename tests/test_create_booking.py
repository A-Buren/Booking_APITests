import pytest
import allure
import requests
from conftest import api_client
from core.clients.api_client import APIClient


@allure.feature('Test CreateBooking')
@allure.story('Test connection')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(booking_dates=generate_random_booking_data)
    with allure.step("Проверка структуры ответа"):
        assert "bookingid" in response["data"], "missing required field 'bookingid'"
        assert 'booking' in response['data'], "missing required field 'booking'"
        assert isinstance(response['data']['booking'], dict), (
            f"Field 'booking' should be dict, but got {type(response['data']['booking'])}")
    with allure.step("Проверка формата данных в ответе"):
        assert response['data']['booking']['firstname'] == generate_random_booking_data[
            'firstname'], f"Expected {generate_random_booking_data['firstname']}, but got {response['data']['booking']['firstname']}"
        assert isinstance(response["data"]["booking"]["firstname"], str), (
            f"Field 'firstname' should be str, but got {type(response['data']['firstname'])}")
        assert response['data']['booking']['lastname'] == generate_random_booking_data[
            'lastname'], f"Expected {generate_random_booking_data['firstname']}, but got {response['data']['booking']['firstname']}"
        assert isinstance(response["data"]["booking"]["lastname"], str), (
            f"Field 'lastname' should be str, but got {type(response['data']['lastname'])}")
        assert response['data']['booking']['totalprice'] == generate_random_booking_data[
            'totalprice'], f"Expected {generate_random_booking_data['totalprice']}, but got {response['data']['booking']['totalprice']}"
        assert isinstance(response["data"]["booking"]["totalprice"], int), (
            f"Field 'totalprice' should be int, but got {type(response['data']['totalprice'])}")
        assert response['data']['booking']['depositpaid'] == generate_random_booking_data[
            'depositpaid'], f"Expected {generate_random_booking_data['depositpaid']}, but got {response['data']['booking']['depositpaid']}"
        assert isinstance(response["data"]["booking"]["depositpaid"], bool), (
            f"Field 'depositpaid' should be bool, but got {type(response['data']['depositpaid'])}")
        assert response['data']['booking']['additionalneeds'] == generate_random_booking_data[
            'additionalneeds'], f"Expected {generate_random_booking_data['additionalneeds']}, but got {response['data']['booking']['additionalneeds']}"
        assert isinstance(response["data"]["booking"]["additionalneeds"], str), (
            f"Field 'additionalneeds' should be str, but got {type(response['data']['additionalneeds'])}")
        assert response['data']['booking']['bookingdates']['checkin'] == generate_random_booking_data['bookingdates'][
            'checkin'], f"Expected {generate_random_booking_data['bookingdates']['checkin']}, but got {response['data']['booking']['bookingdates']['checkin']}"
        assert isinstance(response['data']['booking']['bookingdates']['checkin'], str), (
            f"Field 'checkin' should be str, but got {type(response['data']['checkin'])}")
        assert response['data']['booking']['bookingdates']['checkout'] == generate_random_booking_data['bookingdates'][
            'checkout'], f"Expected {generate_random_booking_data['bookingdates']['checkout']}, but got {response['data']['bookingdates']['checkout']}"
        assert isinstance(response['data']['booking']['bookingdates']['checkout'], str), (
            f"Field 'checkout' should be str, but got {type(response['data']['checkout'])}")
        assert isinstance(response["data"]["booking"]["bookingdates"], dict), (
            f"Field 'bookingdates' should be dict, but got {type(response['data']['bookingdates'])}")