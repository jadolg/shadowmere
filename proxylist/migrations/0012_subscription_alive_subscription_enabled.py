# Generated by Django 4.2 on 2023-04-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proxylist", "0011_alter_subscription_kind"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="alive",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="subscription",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
    ]