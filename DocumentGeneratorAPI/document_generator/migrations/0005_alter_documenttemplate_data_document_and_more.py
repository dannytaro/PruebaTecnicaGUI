# Generated by Django 4.2.4 on 2023-08-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_generator', '0004_alter_documenttemplate_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttemplate',
            name='data_document',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='documenttemplate',
            name='template_document',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
