# Generated by Django 4.0.3 on 2022-04-01 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("proxylist", "0004_proxy_times_check_failed_proxy_times_checked"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="proxy",
            name="times_check_failed",
        ),
    ]
