# Generated by Django 5.0.1 on 2024-01-20 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0012_alter_coursesubscription_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesubscription',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='lms.course', verbose_name='курс'),
        ),
    ]
