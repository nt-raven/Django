# Generated by Django 4.1.2 on 2022-11-29 09:48

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("practice_app2", "0009_alter_model_student_details_sd_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="model_student_details",
            name="sd_contact",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None
            ),
        ),
    ]
