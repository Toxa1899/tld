from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.create_activation_code()
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)




class CustomUser(AbstractUser):
    DRIVERS_LICENSE_ISSUING_STATE_CHOICES = (
        ("Alabama", "Alabama"),
        ("Alaska", "Alaska"),
        ("Arizona", "Arizona"),
        ("Arkansas", "Arkansas"),
        ("California", "California"),
        ("Colorado", "Colorado"),
        ("Connecticut", "Connecticut"),
        ("Delaware", "Delaware"),
        ("Florida", "Florida"),
        ("Georgia", "Georgia"),
        ("Hawaii", "Hawaii"),
        ("Idaho", "Idaho"),
        ("Illinois", "Illinois"),
        ("Indiana", "Indiana"),
        ("Iowa", "Iowa"),
        ("Kansas", "Kansas"),
        ("Louisiana", "Louisiana"),
        ("Maine", "Maine"),
        ("Maryland", "Maryland"),
        ("Massachusetts", "Massachusetts"),
        ("Michigan", "Michigan"),
        ("Minnesota", "Minnesota"),
        ("Mississippi", "Mississippi"),
        ("Missouri", "Missouri"),
        ("Montana", "Montana"),
        ("Nebraska", "Nebraska"),
        ("Nevada", "Nevada"),
        ("New Hampshire", "New Hampshire"),
        ("New Jersey", "New Jersey"),
        ("New Mexico", "New Mexico"),
        ("New York", "New York"),
        ("North Carolina", "North Carolina"),
        ("North Dakota", "North Dakota"),
        ("Ohio", "Ohio"),
        ("Oklahoma", "Oklahoma"),
        ("Oregon", "Oregon"),
        ("Pennsylvania", "Pennsylvania"),
        ("Rhode Island", "Rhode Island"),
        ("South Carolina", "South Carolina"),
        ("South Dakota", "South Dakota"),
        ("Tennessee", "Tennessee"),
        ("Texas", "Texas"),
        ("Utah", "Utah"),
        ("Vermont", "Vermont"),
        ("Virginia", "Virginia"),
        ("Washington", "Washington"),
        ("Washington, DC", "Washington, DC"),
        ("West Virginia", "West Virginia"),
        ("Wisconsin", "Wisconsin"),
        ("Wyoming", "Wyoming"),
        ("Alberta", "Alberta"),
        ("British Columbia", "British Columbia"),
        ("Manitoba", "Manitoba"),
        ("New Brunswick", "New Brunswick"),
        ("Newfoundland and Labrador", "Newfoundland and Labrador"),
        ("Northwest Territories", "Northwest Territories"),
        ("Nova Scotia", "Nova Scotia"),
        ("Nunavut", "Nunavut"),
        ("Ontario", "Ontario"),
        ("Prince Edward Island", "Prince Edward Island"),
        ("Quebec", "Quebec"),
        ("Saskatchewan", "Saskatchewan"),
        ("Yukon Territory", "Yukon Territory"),
        ("Distrito Federal", "Distrito Federal"),
        ("Aguascalientes", "Aguascalientes"),
        ("Baja California", "Baja California"),
        ("Baja California Sur", "Baja California Sur"),
        ("Campeche", "Campeche"),
        ("Chiapas", "Chiapas"),
        ("Chihuahua", "Chihuahua"),
        ("Coahuila", "Coahuila"),
        ("Colima", "Colima"),
        ("Durango", "Durango"),
        ("Guanajuato", "Guanajuato"),
        ("Guerrero", "Guerrero"),
        ("Hidalgo", "Hidalgo"),
        ("Jalisco", "Jalisco"),
        ("Michoacán", "Michoacán"),
        ("Morelos", "Morelos"),
        ("México", "México"),
        ("Nayarit", "Nayarit"),
        ("Nuevo León", "Nuevo León"),
        ("Oaxaca", "Oaxaca"),
        ("Puebla", "Puebla"),
        ("Querétaro", "Querétaro"),
        ("Quintana Roo", "Quintana Roo"),
        ("San Luis Potosí", "San Luis Potosí"),
        ("Sinaloa", "Sinaloa"),
        ("Sonora", "Sonora"),
        ("Tabasco", "Tabasco"),
        ("Tamaulipas", "Tamaulipas"),
        ("Tlaxcala", "Tlaxcala"),
        ("Veracruz", "Veracruz"),
        ("Yucatán", "Yucatán"),
        ("Zacatecas", "Zacatecas")



    )

    COLORS = (
        ("Yellow", "Yellow"),
        ("Green", "Green"),
        ("Orange", "Orange"),
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Cyan-Blue", "Cyan-Blue"),
        ("Tealish Green", "Tealish Green"),
        ("Magenta", "Magenta"),
        ("Purple", "Purple"),
        ("Red-Orange", "Red-Orange"),
        ("Grey", "Grey"),
        ("Bluewood", "Bluewood"),
        ("Default color", "Default color"),


    )


    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=18)
    company = models.CharField(max_length=80, blank=True, null=True)
    usdot = models.IntegerField(blank=True, null=True)
    number_employees = models.IntegerField(blank=True, null=True)
    activation_code = models.CharField(max_length=60, blank=True)
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name="username")
    is_active = models.BooleanField(default=False)
    vin = models.CharField(max_length=20, blank=True, null=True, verbose_name="Vehicle ID")
    drivers_license = models.CharField(max_length=50, blank=True, null=True, verbose_name="Driver's License No*")
    drivers_license_issuing_state = models.CharField(max_length=50, blank=True, null=True,
                                                     verbose_name="Driver's License Issuing State*",
                                                     choices=DRIVERS_LICENSE_ISSUING_STATE_CHOICES)
    home_terminal_address = models.CharField(max_length=100, blank=True, null=True,
                                             verbose_name="Home Terminal Address"),
    co_driver = models.CharField(max_length=100, blank=True, null=True, verbose_name="co_driver")
    colors = models.CharField(max_length=50, verbose_name="Colors", blank=True, null=True, choices=COLORS)
    address1 = models.CharField(max_length=125, blank=True, null=True, verbose_name="address1")
    address2 = models.CharField(max_length=125, blank=True, null=True, verbose_name="address2")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="city")
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name="State")
    postal_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Zip")
    notes = models.TextField(verbose_name='Notes')
    allow_personal_conveyance = models.BooleanField(default=False, verbose_name='Allow Personal Conveyance')
    allow_yard_move = models.BooleanField(default=False, verbose_name='Allow Yard Move')
    is_driver = models.BooleanField(default=False)
    



    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
        
        



# class Driver(models.model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)