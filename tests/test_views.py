import pytest
import usaddress
import json
from django import urls


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    url = urls.reverse('address-parse')
    resp = client.get(url, {'address': address_string})
    parsed_address = json.loads(resp.content)
    assert parsed_address


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    url = urls.reverse('address-parse')
    try:
        resp = client.get(url, {'address': address_string})
    except usaddress.RepeatedLabelError:
        assert True
    else:
        assert False
