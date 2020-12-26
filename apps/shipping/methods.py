from decimal import Decimal as D
from oscar.apps.shipping import methods
from oscar.core import prices

class Standard(methods.Base):
    code = 'Standard'
    name = 'Standard Worldwide'

    def calculate(self, basket):
        print("US calculate")
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('0.00'))
