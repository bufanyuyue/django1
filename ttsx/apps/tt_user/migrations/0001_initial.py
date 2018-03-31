# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings
import django.contrib.auth.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', unique=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('add_date', models.DateTimeField(verbose_name='添加时间', auto_now=True)),
                ('update_date', models.DateTimeField(verbose_name='修改时间', auto_now_add=True)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set')),
            ],
            options={
                'db_table': 'tt_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(verbose_name='添加时间', auto_now=True)),
                ('update_date', models.DateTimeField(verbose_name='修改时间', auto_now_add=True)),
                ('isDelete', models.BooleanField(verbose_name='逻辑删除', default=False)),
                ('receiver', models.CharField(max_length=10)),
                ('adde', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=11)),
                ('isDefault', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'df_address',
            },
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, to='tt_user.AreaInfo', null=True)),
            ],
            options={
                'db_table': 'tt_area',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='city'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='district'),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(to='tt_user.AreaInfo', related_name='province'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
