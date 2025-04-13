# Generated by Django 4.2.20 on 2025-04-13 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partners', to='familytree.person'),
        ),
    ]
