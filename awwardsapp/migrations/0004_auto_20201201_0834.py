# Generated by Django 3.1.3 on 2020-12-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsapp', '0003_auto_20201129_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='My Bio', max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_information',
            field=models.CharField(default='+254', max_length=300),
        ),
    ]