# Generated by Django 5.0.13 on 2025-04-11 08:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0186_alter_formviewfieldoptionscondition_value_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booleanfield",
            name="boolean_default",
            field=models.BooleanField(
                db_default=False,
                default=False,
                help_text="The default value for field if none is provided.",
            ),
        ),
        migrations.AddField(
            model_name="datefield",
            name="date_default_now",
            field=models.BooleanField(
                db_default=False,
                default=False,
                help_text="If enabled, the default value for new rows will be set to the current date and time when the row is created. If disabled, no default value will be set.",
            ),
        ),
        migrations.AddField(
            model_name="multiplecollaboratorsfield",
            name="multiple_collaborators_default",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveBigIntegerField(),
                blank=True,
                help_text="The default value for the field if none is provided. Can be None if no default is set, or the IDs of available collaborators or value 0 to automatically set the current user when row is created.",
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="multipleselectfield",
            name="multiple_select_default",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveBigIntegerField(),
                blank=True,
                help_text="The default value for the field if none is provided. Can be None if no default is set, or the IDs of an available select options.",
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="numberfield",
            name="number_default",
            field=models.DecimalField(
                blank=True,
                decimal_places=20,
                help_text="The default value for field if none is provided.",
                max_digits=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="singleselectfield",
            name="single_select_default",
            field=models.PositiveBigIntegerField(
                blank=True,
                help_text="The default value for the field if none is provided. Can be None if no default is set, or the ID of an available select option.",
                null=True,
            ),
        ),
    ]
