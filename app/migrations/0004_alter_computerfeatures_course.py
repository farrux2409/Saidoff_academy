# Generated by Django 4.2.16 on 2024-10-10 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_courseplan_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerfeatures',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computer_feature', to='app.course'),
        ),
    ]
