# Generated by Django 2.0.4 on 2018-06-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0007_auto_20180604_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
