# Generated by Django 2.2 on 2019-04-15 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impressora', '0005_auto_20190415_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='ip',
            field=models.GenericIPAddressField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='printer',
            name='serial',
            field=models.CharField(max_length=20),
        ),
    ]
