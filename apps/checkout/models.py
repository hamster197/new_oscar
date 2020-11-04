from oscar.apps.checkout.models import *  # noqa isort:skip
from oscar.apps.catalogue.models import Product
from django.db import models

class ColorChoisesGuide(models.Model):
    color = models.CharField(verbose_name='Color', max_length=55)

class GoldSampleGuide(models.Model):
    gold_sample = models.IntegerField(verbose_name='Gold sample', )

class TypesGuide(models.Model):
    type = models.CharField(verbose_name='Type', max_length=55)

class ProductProfile(models.Model):
    product_id = models.OneToOneField(Product, verbose_name='Product', on_delete=models.CASCADE)
    gender_choises = (('Male','Mail'),('Femail','Femail'))
    gender = models.CharField(verbose_name='Gender', choices=gender_choises, max_length=6)
    color_id = models.ForeignKey(ColorChoisesGuide, verbose_name='Color', on_delete=models.CASCADE,
                                 related_name='color_id', null=True)
    gold_sample_id = models.ForeignKey(GoldSampleGuide, verbose_name='Gold sample', on_delete=models.CASCADE,
                                       related_name='gold_sample_id',null=True)
    types_id = models.ForeignKey(TypesGuide, verbose_name='Type', on_delete=models.CASCADE,
                                 related_name='types_id', null=True)
