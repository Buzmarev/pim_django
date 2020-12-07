from django.db import models


class AttributeGroupe(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name='Code')
    title = models.CharField(max_length=100, verbose_name='Title')
    sort_order = models.PositiveSmallIntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')


class Attribute(models.Model):
    TEXT = 'text'
    TEXT_AREA = 'text_area'
    ATTR_TYPES = [
        (TEXT, 'Text'),
        (TEXT_AREA, 'TextArea')
    ]
    code = models.CharField(max_length=100, unique=True, verbose_name='Code')
    title = models.CharField(max_length=100, verbose_name='Title')
    attribute_type = models.CharField(
        max_length=30,
        choices=ATTR_TYPES,
        verbose_name='Attribute type'
    )
    attribute_groupe = models.ForeignKey(
        AttributeGroupe,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Attribute groupe'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')


class Category(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name='Code')
    title = models.CharField(max_length=100, verbose_name='Title')


class Family(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name='Code')
    title = models.CharField(max_length=100, verbose_name='Title')
    attribute_set = models.ManyToManyField(Attribute)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')


class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True, verbose_name='SKU')
    family = models.ForeignKey(
        Family,
        on_delete=models.PROTECT,
        verbose_name='Family'
    )
    is_enabled = models.BooleanField(default=True, verbose_name='Enabled')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')


class AbstractAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class AttributeValueText(AbstractAttributeValue):
    value = models.CharField(max_length=256)


class AttributeValueTextArea(AbstractAttributeValue):
    value = models.TextField()
