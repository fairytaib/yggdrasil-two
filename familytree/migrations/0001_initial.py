# Generated by Django 4.2.20 on 2025-03-22 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, default='I am me!')),
                ('parents', models.ManyToManyField(blank=True, related_name='children', to='familytree.person')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='familytree.person')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyTree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familytrees', to=settings.AUTH_USER_MODEL)),
                ('person', models.ManyToManyField(related_name='persons', to='familytree.person')),
            ],
        ),
    ]
