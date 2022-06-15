from django.conf import settings
from django.db import models

from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    class State(models.TextChoices):
        NEW = 'NEW', _('New')
        UNDER_CONSTRUCTION = 'UNDER-CONSTRUCTION', _('Under-Construction')
        COMPLETE = 'COMPLETE', _('Complete')
        INCOMPLETE = 'INCOMPLETE', _('Incomplete')
        AVAILABLE = 'AVAILABLE', _('Available')
        UNAVAILABLE = 'UNAVAILABLE', _('Unavailable')

    class Type(models.TextChoices):
        VILLA = 'VILLA', _('Villa')
        APARTMENT_BUILDING = 'BUILDING', _('Apartment Building')
        RESIDENTIAL_COMPLEX = 'COMPLEX', _('Residential Complex')
        COMMERCIAL = 'COMMERCIAL', _('Commercial')
        INDUSTRIAL = 'INDUSTRIAL', _('Industrial')
        LAND = 'LAND', _('Lands')

    name = models.CharField(verbose_name=_('Project Name'), max_length=250, null=True)
    about = models.CharField(verbose_name=_('About'), max_length=250, null=True, blank=False)
    developer = models.ForeignKey(
        'Developer', verbose_name=_('developer'),
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    state = models.CharField(
        verbose_name=_('State of the Project'),
        max_length=20,
        choices=State.choices,
        default=State.NEW,
    )
    type = models.CharField(
        verbose_name=_('Type of the Project'),
        max_length=20,
        choices=Type.choices,
        default=Type.VILLA, blank=False,
    )
    location = models.TextField(verbose_name=_('Location'), null=True, blank=False)
    area = models.DecimalField(
        verbose_name=_('Area (square meters)'),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=False,
    )
    friends = models.TextField(verbose_name=_('Friends'), null=True, blank=True, )
    district = models.CharField(verbose_name=_('District'), max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Gender(models.TextChoices):
    MALE = 'M', _('male')
    FEMALE = 'F', _('female')


class Client(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), null=True, blank=False, on_delete=models.CASCADE)
    city = models.CharField(verbose_name=_('City'), max_length=250, null=True, blank=False)
    address = models.TextField(verbose_name=_('Address'), null=True, blank=False)
    birthday = models.DateField(verbose_name=_('Birthday'), null=True, blank=False)
    mobile = PhoneNumberField(verbose_name=_('Mobile'), null=True, blank=False)
    phone = PhoneNumberField(verbose_name=_('Phone'), null=True, blank=True)
    nationality = CountryField(verbose_name=_('Nationality'), null=True, blank=False)
    gender = models.CharField(
        verbose_name=_('Gender'),
        max_length=2,
        choices=Gender.choices,
        default=Gender.MALE,
        null=True,
        blank=False,
    )
    photo = models.ImageField(verbose_name=_('Personal Photo'), )

    def __str__(self):
        return self.user


class Developer(Client):
    is_company = models.BooleanField(verbose_name=_('Is a Company?'))
    company_name = models.CharField(verbose_name=_('Company Name'), max_length=250, null=True, blank=True, )
    commercial_license = models.FileField(verbose_name=_('Commercial License'), null=True, blank=True, )
    company_website = models.CharField(verbose_name=_('Company Website '), max_length=512, null=True, blank=True, )


class Subscription(models.Model):
    client = models.ForeignKey(
        'Client',
        verbose_name=_('Client'),
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    project = models.ForeignKey(
        'Project',
        verbose_name=_('Project'),
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    subscription_date = models.DateTimeField(verbose_name=_('Subscription Date'), auto_now_add=True, )
    referral = models.ForeignKey(
        'Client',
        verbose_name=_('Referral'),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='referrals',
    )

    def __str__(self):
        return '{} {}'.format(self.client, self.project)


class Stage(models.Model):
    project = models.ForeignKey(
        'Project',
        verbose_name=_('Project'),
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    title = models.CharField(verbose_name=_('Title'), max_length=150, null=True, blank=False, )

    def __str__(self):
        return self.title


class SubStage(models.Model):
    stage = models.ForeignKey(
        'Stage',
        verbose_name=_('Stage'),
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    title = models.CharField(verbose_name=_('Title'), max_length=150, null=True, blank=False, )
    start_date = models.DateField(verbose_name=_('Start Date'), null=True, blank=True, )
    end_date = models.DateField(verbose_name=_('End Date'), null=True, blank=True, )
    done = models.BooleanField(verbose_name=_('Done'))

    def __str__(self):
        return self.title


class StageUpdate(models.Model):
    sub_stage = models.ForeignKey(
        'SubStage',
        verbose_name=_('Sub Stage'),
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    update_text = models.TextField(verbose_name=_('Update Text'), null=True, blank=False, )
    update_date = models.DateTimeField(verbose_name=_('Update Date'), auto_now_add=True, )

    def __str__(self):
        return self.update_text


class Media(models.Model):
    stage_update = models.ForeignKey(
        'StageUpdate',
        verbose_name=_('Stage Update'),
        null=True,
        blank=False,
        on_delete=models.CASCADE,
    )
    media = models.FileField(verbose_name=_('media'), null=True, blank=True, )

    def __str__(self):
        return self.stage_update
