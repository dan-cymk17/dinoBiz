# Generated by Django 3.1.2 on 2020-12-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20201211_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dno', models.IntegerField(blank=True, max_length=10)),
                ('street', models.CharField(blank=True, max_length=200)),
                ('locality', models.CharField(blank=True, max_length=200)),
                ('pincode', models.IntegerField(blank=True, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]
