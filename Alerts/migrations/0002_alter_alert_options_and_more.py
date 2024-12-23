# Generated by Django 4.2 on 2024-10-30 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Data', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alert',
            options={},
        ),
        migrations.RenameField(
            model_name='alert',
            old_name='target_price',
            new_name='price_target',
        ),
        migrations.AlterUniqueTogether(
            name='alert',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert_type',
            field=models.CharField(choices=[('above', 'Above'), ('below', 'Below')], max_length=20),
        ),
        migrations.AlterField(
            model_name='alert',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock_Data.stock'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='alert',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='updated_at',
        ),
    ]
