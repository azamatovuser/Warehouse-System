from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError(_('User should have a username'))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if password is None:
            raise TypeError(_('Password should not be None'))

        user = self.create_user(
            username=username,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    ROLE = (
        (0, 'Manager'),
        (1, 'Employee'),
        (2, 'Client'),
    )

    username = models.CharField(max_length=50, unique=True, verbose_name=_('Username'), db_index=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=50, verbose_name=_('Full name'), null=True, blank=True)
    phone_number = models.CharField(max_length=221, null=True, blank=True)
    role = models.IntegerField(choices=ROLE, default=2, null=True)
    is_superuser = models.BooleanField(default=False, verbose_name=_('Super user'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Staff user'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active user'))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date modified'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.full_name:
            return f'{self.full_name} ({self.username})'
        return f'{self.username}'

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data