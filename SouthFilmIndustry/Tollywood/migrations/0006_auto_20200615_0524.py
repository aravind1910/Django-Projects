# Generated by Django 3.0.6 on 2020-06-14 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tollywood', '0005_contactform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Contact',
        ),
    ]