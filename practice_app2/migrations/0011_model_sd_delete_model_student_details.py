# Generated by Django 4.1.2 on 2022-11-29 09:58

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("practice_app2", "0010_alter_model_student_details_sd_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="model_sd",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sd_first_name", models.CharField(max_length=100)),
                ("sd_branch", models.CharField(max_length=100)),
                ("sd_age", models.IntegerField()),
                (
                    "sd_contact",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("sd_city", models.CharField(max_length=100)),
                (
                    "sd_email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="practice_app2.model_student",
                        to_field="s_email",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="model_student_details",),
    ]
