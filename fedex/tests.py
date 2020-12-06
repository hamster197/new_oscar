# -*- coding: utf-8 -*-
"""
    FedEx API tests.
"""

from .config import FedexConfiguration
from .sevices import (AddressService, RateService)
from unittest import TestCase
import logging
import os

try:
    from PIL import Image
except ImportError:
    Image = None  # NOQA

logging.basicConfig()
logging.getLogger("suds.client").setLevel(logging.DEBUG)
file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(file_path)
file_name = os.path.join(directory_path, "tests.cfg")
CONFIGURATION = FedexConfiguration(wsdls="beta", file_name=file_name)

def set_from_address(address):
    """
    Set a test 'from' address.
    :param address: The address to populate.
    """
    address.StreetLines = ["300 Brannan St.", "Suite 405"]
    address.City = "San Francisco"
    address.StateOrProvinceCode = "CA"
    address.PostalCode = "94107"
    address.CountryCode = "US"

def set_package(package):
    """
    Set a test package.
    :param package: The package line item to populate.
    """
    package.PhysicalPackaging = "BOX"
    package.Weight.Value = 1.0
    package.Weight.Units = "LB"


def set_selection_details(selection_details):
    """
    Set test selection details.
    :param selection_details: The tracking selection details to populate.
    """
    selection_details.CarrierCode = "FDXG"
    selection_details.OperatingCompany = "FEDEX_GROUND"
    selection_details.PackageIdentifier.Type = "TRACKING_NUMBER_OR_DOORTAG"
    selection_details.PackageIdentifier.Value = "800026015050023"


def set_shipment(shipment, package):
    """
    Set a test shipment.
    :param shipment: The shipment to populate.
    :param package: The package to add.
    """
    shipment.DropoffType = "REGULAR_PICKUP"
    # FEDEX_GROUND if in the US
    # INTERNATIONAL_ECONOMY if outside the US
    shipment.ServiceType = "FEDEX_GROUND"
    shipment.PackagingType = "YOUR_PACKAGING"
    shipment.Shipper.Contact.CompanyName = "Pickwick & Weller"
    shipment.Shipper.Contact.PhoneNumber = "8777386171"
    set_from_address(shipment.Shipper.Address)
    shipment.Recipient.Contact.PersonName = "POTUS"
    shipment.Recipient.Contact.PhoneNumber = "1234567890"
    set_to_address_US(shipment.Recipient.Address)
    shipment.RateRequestTypes = ["NONE"]
    shipment.RequestedPackageLineItems.append(package)
    shipment.PackageCount = len(shipment.RequestedPackageLineItems)
    shipment.ShippingChargesPayment.PaymentType = "SENDER"
    shipment.ShippingChargesPayment.Payor.ResponsibleParty.AccountNumber =\
        CONFIGURATION.account_number

def set_to_address_russia(address):
    """
    Set a test 'to' address.
    :param address: The address to populate.
    """
    address.StreetLines = ["Bratislavskaya Ulitsa"]
    address.City = "Moscow"
    address.PostalCode = "109451"
    address.CountryCode = "RU"
    address.StateOrProvinceCode = "RU"

def set_to_address_US(address):
    """
    Set a test 'to' address.
    :param address: The address to populate.
    """
    address.StreetLines = ["1600 Pennsylvania Avenue NW"]
    address.City = "Washington"
    address.StateOrProvinceCode = "DC"
    address.PostalCode = "20500"
    address.CountryCode = "US"

def set_to_address_europe(address):
    #Germany
    """
    Set a test 'to' address.
    :param address: The address to populate.
    """
    address.StreetLines = ["Freiertweg 21A"]
    address.City = "Berlin"
    address.PostalCode = "12305"
    address.CountryCode = "DE"
    address.StateOrProvinceCode = "DE"

def set_to_address_brazil(address):
    """
    Set a test 'to' address.
    :param address: The address to populate.
    """
    address.StreetLines = ["St. F Norte"]
    address.City = "Berlin"
    address.PostalCode = "12305"
    address.CountryCode = "DE"
    address.StateOrProvinceCode = "DE"

class FedexTestCase(TestCase):

    def test_address_service_US(self):
        """
        Test the address service in US
        """
        service = AddressService(CONFIGURATION)
        address = service.create_address()
        set_to_address_US(address.Address)
        result = service.validate([address])
        print(result)

    def test_address_service_russia(self):
        """
        Test the address in Russia
        """
        service = AddressService(CONFIGURATION)
        address = service.create_address()
        set_to_address_russia(address.Address)
        result = service.validate([address])
        print(result)

    def test_address_service_europe(self):
        """
        Test the address in Germany
        """
        service = AddressService(CONFIGURATION)
        address = service.create_address()
        set_to_address_europe(address.Address)
        result = service.validate([address])
        print(result)

    def test_rate_service(self):
        """
        Test the rate service.
        """
        service = RateService(CONFIGURATION)
        shipment = service.create_shipment()
        package = service.create_package()
        package.GroupPackageCount = 1
        set_package(package)
        set_shipment(shipment, package)
        result = service.get_rates(shipment)
        for i in getattr(result, "RateReplyDetails"):
            for j in getattr(i, "RatedShipmentDetails"):
                totalCharge = getattr(getattr(j, "ShipmentRateDetail"), "TotalNetChargeWithDutiesAndTaxes")
                currency = getattr(totalCharge, "Currency")
                amount = getattr(totalCharge, "Amount")
        print(str(amount) + " " + currency)
        print("_________________________________________________________________________________________________")
        print(shipment)
