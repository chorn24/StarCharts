# Generated by Django 4.2.7 on 2024-01-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_systemchart_star_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemchart',
            name='star_type',
            field=models.CharField(choices=[('Yellow Dwarf Star', 'Yellow Dwarf Star'), ('Red Dwarf Star', 'Red Dwarf Star'), ('Red Giant Star', 'Red Giant Star'), ('Red Supergiant Star', 'Red Supergiant Star'), ('Blue Giant Star', 'Blue Giant Star'), ('White Dwarf Star', 'White Dwarf Star'), ('Brown Dwarf Star', 'Brown Dwarf Star')], max_length=50, null=True),
        ),
    ]
