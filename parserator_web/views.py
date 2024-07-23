import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        addr_param = request.GET.get('address')
        addr_components, addr_type = self.parse(addr_param)
        return Response({'AddressComponents': addr_components,
                         'AddressType': addr_type})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            parsed = usaddress.tag(address)
        except TypeError:
            raise usaddress.RepeatedLabelError

        address_components = parsed[0]
        address_type = parsed[1]

        return address_components, address_type
