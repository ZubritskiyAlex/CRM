from django.db import models
from django.contrib.auth. models import User
from django_countries.fields import CountryField



LEVELS = (
    (1, 'Elementary',),
    (2, 'Not bad',),
    (3, 'Medium',),
    (4, 'Confident user',),
    (5, 'Expert',),
)


class Company(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null=True, blank=True)
    offices = models.ManyToManyField('Office', related_name='companies')
    updated = models.DateTimeField(auto_now=True)


class Office(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    country = CountryField()
    is_active = models.BooleanField(null=True, blank=True)


class Partnership(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    partnership_name = models.CharField(max_length=200)
    companies = models.ManyToManyField(Company)
    is_active = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    skill_name = models.CharField(max_length=200)
    skill_level = models.CharField(
        max_length=2,
        choices=LEVELS,
        default=1,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Language(models.Model):

    language = models.CharField(max_length=200)
    _id = models.AutoField(primary_key=True, editable=False)
    skill_level = models.CharField(
        max_length=2,
        choices=LEVELS,
        default=1,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class JobPlace(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, null=True)
    languages = models.ManyToManyField(Language)
    skills = models.ManyToManyField(Skill)
    is_active = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Person(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = CountryField()
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    job_place = models.ForeignKey(JobPlace, on_delete=models.CASCADE, related_name='persons')
    companies = models.ManyToManyField(Company)
