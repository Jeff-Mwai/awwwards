# Generated by Django 3.1.3 on 2020-11-29 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('screenshot', models.ImageField(blank=True, upload_to='images/')),
                ('url', models.URLField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='awwardsapp.profile')),
            ],
        ),
    ]
