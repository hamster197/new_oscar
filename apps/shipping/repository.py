from oscar.apps.shipping import repository
from . import methods as shipping_methods


class Repository(repository.Repository):

    # methods = [
    #     shipping_methods.Standard(),
    #     shipping_methods.International()
    # ]

    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):
        methods = []
        # print("SHIPPING ADDR:" + shipping_addr)
        # print("Country code: ", shipping_addr.country.code)
        # if shipping_addr and shipping_addr.country.code == 'US':
        #     # Only available in the US
        methods += [shipping_methods.Standard()]
        # else:
        #     methods += [shipping_methods.International()]
        return methods
