# -*- coding: utf-8 -*-
"""
    FedEx web services.
"""

from .addresses import AddressService
from .commons import BaseService
from .rates import RateService


class FedexService(BaseService):
    """
    FedEx service wrapper.
    :param configuration: API configuration.
    """

    def __init__(self, configuration):
        self.address_service = AddressService(configuration)
        self.rate_service = RateService(configuration)

    def get_addresses(self, addresses, **kwargs):
        """
        Get a list of addresses.
        :param addresses: A list of addresses to get valid shipping addresses
            for.
        :param kwargs: Additional service keyword arguments.
        """
        return self.address_service.validate(addresses, **kwargs)

    def get_rates(self, shipment, **kwargs):
        """
        Get shipment rates.
        :param shipment: Shipment instance to get rates for.
        :param kwargs: Additional service keyword arguments.
        """
        return self.rate_service.get_rates(shipment, **kwargs)