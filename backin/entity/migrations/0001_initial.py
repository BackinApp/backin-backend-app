# Generated by Django 2.2.9 on 2020-02-01 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_creator', to=settings.AUTH_USER_MODEL)),
                ('database', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_database', to='database.Database')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('type', models.CharField(choices=[(1, 'BigInt'), (2, 'Int')], max_length=150)),
                ('is_null', models.BinaryField(default=False)),
                ('is_auto_increment', models.BinaryField(default=False)),
                ('is_unique', models.BinaryField(default=False)),
                ('is_primary_key', models.BinaryField(default=False)),
                ('is_index', models.BinaryField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_creation', to=settings.AUTH_USER_MODEL)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_attribute', to='entity.Entity')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
