# Generated by Django 2.1.5 on 2019-03-04 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0010_document_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentMLMAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob', models.FloatField(blank=True, default=None, null=True)),
                ('manual', models.BooleanField(default=False)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('updated_date_time', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_mlm_annotations', to='server.Document')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Label')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='documentmlmannotation',
            unique_together={('document', 'label')},
        ),
    ]
