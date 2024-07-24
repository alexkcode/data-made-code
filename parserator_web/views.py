import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    permission_classes = [AllowAny] 
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        addr_param = request.query_params.get('address')
        addr_components, addr_type = self.parse(addr_param)
        
        output = {'status': 'success',
                  'input_string': addr_param,
                  'address_components': addr_components,
                  'address_type': addr_type}
        
        return Response(output)
        

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            parsed = usaddress.tag(address)
        except ParseError:
            raise usaddress.RepeatedLabelError

        address_components = parsed[0]
        address_type = parsed[1]

        return address_components, address_type
