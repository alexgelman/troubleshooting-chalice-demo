import pytest
import json
import app
import os

from http import HTTPStatus
from chalice.config import Config
from chalice.local import LocalGateway


@pytest.fixture
def api():
    return LocalGateway(app.app, Config())


def test_get_hello_world(api):
    response = api.handle_request(method='GET', path='/', headers={}, body=None)
    print(response)
    assert response['statusCode'] == HTTPStatus.OK
    response =  json.loads(response['body'])
    assert  response['hello'] == 'world'
