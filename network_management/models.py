from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
    }


class Supplier(models.Model):
    """Model for supplier"""

    name = models.CharField(max_length=150, verbose_name='Name')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Email')
    country = models.CharField(max_length=150, verbose_name='Country')
    city = models.CharField(max_length=150, verbose_name='City')
    street = models.CharField(max_length=150, verbose_name='Street')
    house_number = models.CharField(max_length=50, verbose_name='Number of house')

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return f'{self.name} - {self.country}'


class Network(models.Model):
    """Model for network"""

    LEVEL_CHOICES = (
        (0, 'Factory'),
        (1, 'Retail network'),
        (2, 'Entrepreneur')
    )

    name = models.CharField(max_length=150, verbose_name='Name')
    email = models.EmailField(max_length=150, unique=True, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Phone', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Country')
    city = models.CharField(max_length=150, verbose_name='City')
    street = models.CharField(max_length=150, verbose_name='Street')
    house_number = models.CharField(max_length=50, verbose_name='Number of house')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Supplier')
    products = models.ManyToManyField('Product', verbose_name='Products',related_name='networks')
    debt = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Debt')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Level')

    class Meta:
        verbose_name = 'Network'
        verbose_name_plural = 'Networks'

    def __str__(self):
        return f'{self.name} - {self.country}, {self.city}, {self.street}, {self.house_number}'


class Product(models.Model):
    """Model for product"""

    name = models.CharField(max_length=150, verbose_name='Name')
    model = models.CharField(max_length=150, verbose_name='Model')
    release_date = models.DateField(verbose_name='Date of release')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Price')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='image', **NULLABLE)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name='Network')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created', **NULLABLE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.model} - {self.name}'
