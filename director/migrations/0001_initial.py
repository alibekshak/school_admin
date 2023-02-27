# Generated by Django 4.1.7 on 2023-02-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя директор')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия директора')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='Номер телефона')),
                ('image', models.ImageField(blank=True, null=True, upload_to='director_photo/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Директор',
                'verbose_name_plural': 'Директора',
            },
        ),
    ]
