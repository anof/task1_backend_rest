# Generated by Django 2.2.5 on 2019-09-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albums', models.TextField(null=True)),
                ('artists', models.TextField(null=True)),
                ('songs', models.TextField(null=True)),
            ],
        ),
    ]
