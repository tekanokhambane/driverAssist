from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin  # type: ignore
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

ROLE_DRIVER = "driver"
ROLE_ADMIN = "admin"
ROLE_CHOICES = (
    (ROLE_DRIVER, "driver"),
    (ROLE_ADMIN, "admin"),
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=ROLE_DRIVER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Driver(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="driver"
    )
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20, unique=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_driver(sender, instance, created, **kwargs):
    if kwargs["created"] and kwargs["instance"].role == "driver":
        Driver.objects.create(user=kwargs["instance"])


models.signals.post_save.connect(create_driver, sender=User)
