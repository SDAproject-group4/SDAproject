# Generated by Django 4.2.4 on 2023-08-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_repairs_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='repairs',
            name='status',
            field=models.CharField(choices=[('nowe', 'New'), ('w trakcie', 'Pending'), ('zakończone', 'Rejected')], default='New', max_length=100),
        ),
    ]
