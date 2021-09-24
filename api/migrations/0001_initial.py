# Generated by Django 3.2.7 on 2021-09-24 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPlace',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=200)),
                ('skill_level', models.CharField(choices=[(1, 'Elementary'), (2, 'Not bad'), (3, 'Medium'), (4, 'Confident user'), (5, 'Expert')], default=1, max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=200)),
                ('skill_level', models.CharField(choices=[(1, 'Elementary'), (2, 'Not bad'), (3, 'Medium'), (4, 'Confident user'), (5, 'Expert')], default=1, max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('companies', models.ManyToManyField(to='api.Company')),
                ('job_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='api.jobplace')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('partnership_name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('companies', models.ManyToManyField(to='api.Company')),
            ],
        ),
        migrations.AddField(
            model_name='jobplace',
            name='languages',
            field=models.ManyToManyField(to='api.Language'),
        ),
        migrations.AddField(
            model_name='jobplace',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.person'),
        ),
        migrations.AddField(
            model_name='jobplace',
            name='skills',
            field=models.ManyToManyField(to='api.Skill'),
        ),
        migrations.AddField(
            model_name='company',
            name='offices',
            field=models.ManyToManyField(related_name='companies', to='api.Office'),
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
