# Generated by Django 2.2.16 on 2020-10-01 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Mail'), ('Femail', 'Femail')], max_length=6, verbose_name='Gender')),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product', verbose_name='Product')),
            ],
        ),
    ]
