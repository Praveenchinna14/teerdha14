# Generated by Django 4.2.3 on 2024-02-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_naviagtion_bar_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
