# Generated by Django 5.0 on 2023-12-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_documenter_document_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="documenter",
            name="password_repeat",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="documenter",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="documenter",
            name="password",
            field=models.CharField(max_length=50),
        ),
    ]
