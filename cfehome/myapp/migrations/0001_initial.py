# Generated by Django 3.1.5 on 2021-05-04 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/')),
                ('f_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('m_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('l_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('age', models.IntegerField()),
            ],
        ),
    ]
