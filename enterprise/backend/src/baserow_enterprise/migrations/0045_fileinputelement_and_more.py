# Generated by Django 5.0.9 on 2025-04-08 11:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import baserow.core.formula.field


class Migration(migrations.Migration):
    dependencies = [
        ("baserow_enterprise", "0044_migrate_app_labels"),
        ("builder", "0056_ratingelement_ratinginputelement"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileInputElement",
            fields=[
                (
                    "element_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="builder.element",
                    ),
                ),
                (
                    "required",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this form element is a required field.",
                    ),
                ),
                (
                    "label",
                    baserow.core.formula.field.FormulaField(
                        default="", help_text="The text label for this input"
                    ),
                ),
                (
                    "default_name",
                    baserow.core.formula.field.FormulaField(
                        default="", help_text="This input's default file name."
                    ),
                ),
                (
                    "default_url",
                    baserow.core.formula.field.FormulaField(
                        default="", help_text="This input's default file url."
                    ),
                ),
                (
                    "help_text",
                    baserow.core.formula.field.FormulaField(
                        default="",
                        help_text="The help text which should be visible on the element.",
                    ),
                ),
                (
                    "multiple",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this file input allows users to choose multiple files",
                    ),
                ),
                (
                    "max_filesize",
                    models.PositiveIntegerField(
                        default=5,
                        help_text="Maximum file size a user can upload in MB.",
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="Value cannot be less than 1."
                            ),
                            django.core.validators.MaxValueValidator(
                                100, message="Value cannot be greater than 100."
                            ),
                        ],
                    ),
                ),
                (
                    "allowed_filetypes",
                    models.JSONField(
                        default=list, help_text="Allowed file types for this input."
                    ),
                ),
                (
                    "preview",
                    models.BooleanField(
                        default=False,
                        help_text="Whether to show a preview of image files.",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("builder.element",),
        ),
        migrations.AlterField(
            model_name="authformelement",
            name="login_button_label",
            field=baserow.core.formula.field.FormulaField(
                blank=True,
                db_default="",
                default="",
                help_text="The label of the login button",
            ),
        ),
    ]
