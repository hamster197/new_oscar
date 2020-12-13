from decimal import Decimal as D
from oscar.apps.shipping import methods
from oscar.core import prices

class Standard(methods.Base):
    code = 'fedexUS'
    name = 'Fedex US'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('0.00'))


class International(methods.Base):
    code = 'fedexInternational'
    name = 'Fedex International'

    def calculate(self, basket):

        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('0.00'))
