# Generated by Django 4.0.2 on 2022-06-25 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_alter_phase_options_alter_sequence_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookahead',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lookaheads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='well',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wells', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='phase',
            name='order',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='order',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='order',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
