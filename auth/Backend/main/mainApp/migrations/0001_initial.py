# Generated by Django 5.0 on 2024-02-22 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Nodes",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Ip", models.CharField(max_length=50)),
                ("Username", models.CharField(max_length=50)),
                ("Password", models.CharField(max_length=50)),
                ("OS", models.CharField(max_length=30)),
                ("SysoId", models.CharField(max_length=25)),
                ("Node_type", models.CharField(max_length=20)),
                ("Fake_ip", models.CharField(max_length=50, unique=True)),
                ("Live", models.SmallIntegerField(default=1)),
                ("ParentId", models.IntegerField(blank=True, null=True)),
                ("is_Intermediate", models.SmallIntegerField()),
                ("is_Banned", models.SmallIntegerField()),
                ("Operator", models.CharField(max_length=50)),
                ("ServerName", models.CharField(max_length=10)),
                ("HostName", models.CharField(max_length=10)),
                ("Circle", models.CharField(max_length=100)),
                ("Status", models.CharField(max_length=50)),
                ("Comment", models.CharField(max_length=500)),
                ("Cygwin_Version", models.CharField(max_length=50)),
                ("Transfer_Status", models.CharField(max_length=500)),
                ("Installation_Status", models.CharField(max_length=500)),
                ("Time_Sync", models.SmallIntegerField()),
                ("Key_Enabled", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Username", models.CharField(max_length=50)),
                ("Fname", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="AppUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("username", models.CharField(max_length=50)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Ports",
            fields=[
                ("TunnleId", models.AutoField(primary_key=True, serialize=False)),
                ("RemotePort", models.IntegerField()),
                ("LocalPort", models.IntegerField()),
                ("Direction", models.CharField(max_length=100)),
                ("SocketPath", models.CharField(max_length=100)),
                ("Status", models.CharField(max_length=50)),
                ("Comment", models.CharField(max_length=2000)),
                (
                    "NodeId",
                    models.ForeignKey(
                        db_column="NodeId",
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ports",
                        to="mainApp.nodes",
                    ),
                ),
            ],
        ),
    ]