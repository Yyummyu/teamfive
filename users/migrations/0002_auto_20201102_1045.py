# Generated by Django 3.1.2 on 2020-11-02 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu',
            name='sinstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.institute'),
        ),
        migrations.AlterField(
            model_name='stu',
            name='ssupervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]