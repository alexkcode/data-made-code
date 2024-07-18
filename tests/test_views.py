import pytest, useaddress
import parserator_web.views.AddressParse as AddressParse

def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    parsed_address = AddressParse.parse(address_string)
    print(parsed_address)
    assert parsed_address


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    try:
        parsed_address = AddressParse.parse(address_string)
    except useaddress.RepeatedLabelError:
        assert True
    else:
        assert False