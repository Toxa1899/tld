from django.contrib.auth import get_user_model
from django.db import models
import uuid
# import uuid
# Create your models here.




timezone = (
    ('Alaska Daylight Time', 'Alaska Daylight Time'),
    ('Central Daylight Time', 'Central Daylight Time'),
    ('Eastern Daylight Time', 'Eastern Daylight Time'),
    ('Hawaii Standard Time', 'Hawaii Standard Time'),
    ('Mountain Daylight Time', 'Mountain Daylight Time'),
    ('Pheonix Standart Time', 'Pheonix Standart Time'),
    ('Pacific Daylight Time', 'Pacific Daylight Time'),
)


User = get_user_model()
class Company(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_user')
    name = models.CharField(max_length=50, verbose_name='Company Name', unique=True)
    phone = models.CharField(max_length=18, verbose_name='phone')
    usdot = models.CharField(max_length=100, verbose_name='usdot')
    home_terminal_address = models.CharField(max_length=50, verbose_name='home_terminal_address')
    home_terminal_timezone = models.CharField(max_length=50, choices=timezone, verbose_name='home_terminal_timezone')
    email = models.EmailField(verbose_name='email')
    company_address = models.CharField(max_length=60, verbose_name='company_address')
    owner = models.BooleanField(default=False, verbose_name='owner')
    is_active = models.BooleanField(default=False, verbose_name='is_active')
    activation_code = models.CharField(max_length=60, blank=True, null=True, verbose_name='activation_code')
    delete_code = models.CharField(max_length=60, blank=True, null=True, verbose_name='delete_code')


    def __str__(self):
        return self.name

role_company_user = (
    ('Loads viewer (read only)', 'Loads viewer (read only)'),
    ('Loads only', 'Loads only'),
    ('Logbook and Loads ', 'Logbook and Loads'),
    ('Logbook only', 'Logbook only'),
    ('Accounting', 'Accounting'),
    ('Super Dispatcher', 'Super Dispatcher'),
    ('Service Account', 'Service Account'),
    ('Owner', 'Owner')

)

class CompanyUser(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_company')
    is_driver = models.BooleanField(default=False, verbose_name='user is driver ?')
    
    
    def __str__(self):
        return self.user.email


    # def create_activation_code(self):
    #     import uuid
    #     return str(uuid.uuid4())
    #
    # def save(self, *args, **kwargs):
    #     if not self.activation_code:
    #         self.activation_code = self.create_activation_code()
    #     super().save(*args, **kwargs)





