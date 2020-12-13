from oscar.apps.shipping.models import *  # noqa isort:skip

from django.utils.translation import ugettext_lazy as _
from oscar.apps.shipping.abstract_models import AbstractOrderAndItemCharges


class StandardMethod(AbstractOrderAndItemCharges):
    """Модель с обычным набором атрибутов"""

    class Meta(AbstractOrderAndItemCharges.Meta):
        verbose_name = _('Shipping method')
        verbose_name_plural = _('Shipping methods')

from oscar.apps.shipping.models import *  # noqa