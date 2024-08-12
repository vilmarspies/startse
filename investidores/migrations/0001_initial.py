# Generated by Django 5.1 on 2024-08-12 12:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresarios', '0003_metricas'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PropostaInvestimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('percentual', models.FloatField()),
                ('status', models.CharField(choices=[('AS', 'Aguardando assinatura'), ('PE', 'Proposta enviada'), ('PA', 'Proposta aceita'), ('PR', 'Proposta recusada')], default='AS', max_length=2)),
                ('selfie', models.FileField(blank=True, null=True, upload_to='selfie')),
                ('rg', models.FileField(blank=True, null=True, upload_to='rg')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='empresarios.empresas')),
                ('investidor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
