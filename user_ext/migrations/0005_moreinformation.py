# Generated by Django 4.2 on 2025-02-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_ext', '0004_training_description_training_enddate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthDate', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('ext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='more_information', to='user_ext.ext')),
            ],
        ),
    ]
