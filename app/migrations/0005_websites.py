# Generated by Django 3.0.8 on 2020-07-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200728_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Websites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('websiteName', models.CharField(max_length=1000)),
                ('websiteUsername', models.CharField(max_length=60)),
                ('websitePassword', models.CharField(max_length=1000)),
                ('userId', models.ManyToManyField(to='app.User')),
            ],
            options={
                'db_table': 'websites',
            },
        ),
    ]
