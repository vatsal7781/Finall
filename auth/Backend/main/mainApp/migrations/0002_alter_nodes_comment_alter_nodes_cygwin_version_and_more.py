# Generated by Django 5.0 on 2024-02-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nodes",
            name="Comment",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="Cygwin_Version",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="Installation_Status",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="Key_Enabled",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="ServerName",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="Status",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="SysoId",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="Transfer_Status",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="is_Banned",
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="nodes",
            name="is_Intermediate",
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
