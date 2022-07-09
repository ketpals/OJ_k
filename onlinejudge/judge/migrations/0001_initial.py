# from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import judge.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ]


    operations = [


        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=255)),
                ('problem_desc', models.CharField(max_length=500)),
                ('diff', models.CharField(max_length=50)),

            ],
        ),
        migrations.CreateModel(
            name='Testcases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=500)),
                ('output', models.CharField(max_length=500)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Problem')),

            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Coder')),
                # ('status', models.CharField(choices=[('NT', 'Not tested'), ('TS', 'Tested')],
                #                             default='NT', max_length=2)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Problem')),
                ('verdict', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('code', models.CharField(max_length=1000)),

            ],
        ),
        migrations.CreateModel(
            name='Important',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Problem')),
               # ('Imp_status', models.BooleanField(default=False)),

            ],
        ),


    ]

