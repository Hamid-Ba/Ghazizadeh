"""
Account Module Models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _


from django.core.validators import validate_email
from account.vaidators import phone_validator


class UserManager(BaseUserManager):
    """User Manager"""

    def create_user(self, phone, password=None, **extra_fields):
        """Custome Create Normal User"""
        if not phone:
            raise ValueError
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create Super User"""
        if not phone:
            raise ValueError
        user = self.model(phone=phone, is_staff=True, is_superuser=True, **extra_fields)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model"""

    phone = models.CharField(max_length=11, unique=True, validators=[phone_validator], verbose_name="موبایل")
    first_name = models.CharField(max_length=72, blank=True, verbose_name="نام")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="نام خانوادگی")
    email = models.EmailField(max_length=255, validators=[validate_email], blank=True, verbose_name="پست الکترونیک")
    national_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="کد ملی")
    is_active = models.BooleanField(default=True, verbose_name="حساب فعال باشد ؟")
    is_staff = models.BooleanField(default=False, verbose_name="به پنل مدیریت دسترسی داشته باشد ؟")

    USERNAME_FIELD = "phone"

    objects = UserManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.phone

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')
