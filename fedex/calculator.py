from oscar.apps.checkout.session import ShippingAddress
from oscar.core import prices
from decimal import Decimal as D

from .config import FedexConfiguration
from .sevices import (RateService)
import os
import pycountry

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context
file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(file_path)
file_name = os.path.join(directory_path, "tests.cfg")
CONFIGURATION = FedexConfiguration(wsdls="beta", file_name=file_name)


def set_package(package):
    """
    Set package.
    :param package: The package line item to populate.
    """
    package.PhysicalPackaging = "BOX"
    package.Weight.Value = 1.0
    package.Weight.Units = "LB"


# Адрес отправления (откуда отправляем)
def set_from_address(address):
    """
    Set a 'from' address.
    :param address: The address to populate.
    """
    address.StreetLines = ["300 Brannan St.", "Suite 405"]
    address.City = "San Francisco"
    address.StateOrProvinceCode = "CA"
    address.PostalCode = "94107"
    address.CountryCode = "US"


def country_code_converter(input_countries):
    """
    :param input_countries: list containing the name of the countries (can be numpy array)
    :return: list with the ISO alpha 3 codes for the given input ('Unknown Country' if no match found)
    """
    countries = {}
    countries_official = {}
    countries_common = {}

    # loops over all of the countries contained in the pycountry library and populates dictionary
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2

    # loops over the alpha_3 codes from the countries dictionary
    # populates dictionary containing official names and codes
    for alpha_2 in list(countries.values()):
        try:
            countries_official[pycountry.countries.get(alpha_2=alpha_2).official_name] = alpha_2
        except:
            None
    # same for common names
    for alpha_2 in list(countries.values()):
        try:
            countries_common[pycountry.countries.get(alpha_2=alpha_2).common_name] = alpha_2
        except:
            None

    codes = []
    # appends ISO codes for all matches by trying different country name types
    # appends Unknown Country if no match found
    for i in input_countries:
        if i in countries.keys():
            codes.append(countries.get(i))

        elif i in countries_official.keys():
            codes.append(countries_official.get(i))

        elif i in countries_common.keys():
            codes.append(countries_common.get(i))

        else:
            codes.append('Unknown Country')
    return codes


def set_to_address(address, shippingAddress: ShippingAddress):
    """Set a test 'to' address.

    :param address: The address to populate.
    """
    # address.StreetLines = ["1600 Pennsylvania Avenue NW"]
    # address.City = "Washington"
    # # parameter optional even for US states
    # address.StateOrProvinceCode = "DC"
    # address.PostalCode = "20500"
    # address.CountryCode = "US"

    lineOfAddress = str(shippingAddress)
    listOfWords = lineOfAddress.split(",")
    print("LINE:" + lineOfAddress + " \nARRAY: " + str(listOfWords) + " \nSIZE:" + str(len(listOfWords)))
    if (len(listOfWords) == 5):
        print("Size -> 5")
        address.StreetLines = [listOfWords.__getitem__(1).strip()]
        print(str(address.StreetLines))
        address.City = listOfWords.__getitem__(2).strip()
        address.PostalCode = listOfWords.__getitem__(3).strip()
        if listOfWords.__getitem__(4) is not None:
            countryName = listOfWords.__getitem__(4).strip()
            if countryName == "The United States of America":
                countryName = "United States of America"
            resultOfConversion = country_code_converter([countryName])
            print("RESULT:" + str(resultOfConversion.__getitem__(0)))
            address.CountryCode = resultOfConversion.__getitem__(0)

    if (len(listOfWords) == 6):
        print("Size -> 6")
        address.StreetLines = [listOfWords.__getitem__(1).strip()]
        address.City = listOfWords.__getitem__(2).strip()
        address.PostalCode = listOfWords.__getitem__(4).strip()
        if listOfWords.__getitem__(5) is not None:
            countryName = listOfWords.__getitem__(5).strip()
            if countryName == "The United States of America":
                countryName = "United States of America"
            resultOfConversion = country_code_converter([countryName])
            print("RESULT:" + str(resultOfConversion.__getitem__(0)))
            address.CountryCode = resultOfConversion.__getitem__(0)

    if (len(listOfWords) == 7):
        print("Size -> 7")
        address.StreetLines = [listOfWords.__getitem__(1).strip()]
        address.City = listOfWords.__getitem__(2).strip()
        address.PostalCode = listOfWords.__getitem__(4).strip()
        if listOfWords.__getitem__(5) is not None:
            countryName = listOfWords.__getitem__(5).strip()
            if countryName == "The United States of America":
                countryName = "United States of America"
            resultOfConversion = country_code_converter([countryName])
            print("RESULT:" + str(resultOfConversion.__getitem__(0)))
            address.CountryCode = resultOfConversion.__getitem__(0)
        if listOfWords.__getitem__(6) is not None:
            print("Phone number:" + listOfWords.__getitem__(6).strip())
            print("Instructions:" + listOfWords.__getitem__(6).strip())

    if (len(listOfWords) == 8):
        print("Size -> 8")
        address.StreetLines = [listOfWords.__getitem__(1).strip()]
        address.City = listOfWords.__getitem__(2).strip()
        address.PostalCode = listOfWords.__getitem__(4).strip()
        if listOfWords.__getitem__(5) is not None:
            countryName = listOfWords.__getitem__(5).strip()
            if countryName == "The United States of America":
                countryName = "United States of America"
            resultOfConversion = country_code_converter([countryName])
            print("RESULT:" + str(resultOfConversion.__getitem__(0)))
            address.CountryCode = resultOfConversion.__getitem__(0)
        if listOfWords.__getitem__(6) is not None:
            print("Phone number:" + listOfWords.__getitem__(6).strip())
        print("Instructions:" + listOfWords.__getitem__(7).strip())


def set_shipment(shipment, package, shippingAddress: ShippingAddress):
    """
    :param shipment: The shipment to populate.
    :param package: The package to add.
    """
    print("IN SET SHIPMENT" + str(shippingAddress))

    set_to_address(shipment.Recipient.Address, shippingAddress)
    print("COUNTRY CODE" + str(shipment.Recipient.Address.CountryCode))
    if shipment.Recipient.Address.CountryCode == "US":
        print("FEDEX_GROUND")
        shipment.ServiceType = "FEDEX_GROUND"
    else:
        print("INTERNATIONAL_ECONOMY")
        shipment.ServiceType = "INTERNATIONAL_ECONOMY"

    shipment.ServiceType = "FEDEX_GROUND"
    shipment.DropoffType = "REGULAR_PICKUP"
    shipment.PackagingType = "YOUR_PACKAGING"
    shipment.Shipper.Contact.CompanyName = "CompanyName"  # Название компании
    shipment.Shipper.Contact.PhoneNumber = "8111223344"  # Номер телефона
    set_from_address(shipment.Shipper.Address)
    shipment.Recipient.Contact.PersonName = "POTUS"
    shipment.Recipient.Contact.PhoneNumber = "1234567890"
    shipment.RateRequestTypes = ["NONE"]
    shipment.RequestedPackageLineItems.append(package)
    shipment.PackageCount = len(shipment.RequestedPackageLineItems)
    shipment.ShippingChargesPayment.PaymentType = "SENDER"
    shipment.ShippingChargesPayment.Payor.ResponsibleParty.AccountNumber = \
        CONFIGURATION.account_number


class FedexCalculator:
    service = RateService(CONFIGURATION)

    @staticmethod
    def calculate(to_shipping_address: ShippingAddress):
        shipment = FedexCalculator.service.create_shipment()
        package = FedexCalculator.service.create_package()
        package.GroupPackageCount = 1
        set_package(package)
        set_shipment(shipment, package, to_shipping_address)
        result = FedexCalculator.service.get_rates(shipment)
        print(result)
        for i in getattr(result, "RateReplyDetails"):
            for j in getattr(i, "RatedShipmentDetails"):
                totalCharge = getattr(getattr(j, "ShipmentRateDetail"), "TotalNetChargeWithDutiesAndTaxes")
                currency = getattr(totalCharge, "Currency")
                amount = getattr(totalCharge, "Amount")
        print(str(amount) + " " + currency)
        return str(amount)
