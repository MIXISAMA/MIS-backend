# Generated by Django 3.0.4 on 2020-04-21 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('user', '__first__'),
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.FloatField(editable=False, verbose_name='预测指标值')),
                ('detailed_requirement', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='plan.DetailedRequirement', verbose_name='指标点')),
                ('student', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '指标点达成度预测',
                'verbose_name_plural': '指标点达成度预测',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_marks', models.FloatField(default=60.0, verbose_name='结课分数')),
                ('indicator', models.FloatField(default=0.0, verbose_name='评价分数')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Course', verbose_name='课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '成绩和评价',
                'verbose_name_plural': '成绩和评价',
            },
        ),
        migrations.CreateModel(
            name='DetailedPredictionWarning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailed_prediction', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='prediction.DetailedPrediction', verbose_name='指标点达成度预测')),
            ],
            options={
                'verbose_name': '指标点达成度预警',
                'verbose_name_plural': '指标点达成度预警',
            },
        ),
        migrations.AddConstraint(
            model_name='grade',
            constraint=models.UniqueConstraint(fields=('course', 'student'), name='unique_grade'),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('course', 'student')},
        ),
        migrations.AddConstraint(
            model_name='detailedprediction',
            constraint=models.UniqueConstraint(fields=('detailed_requirement', 'student'), name='unique_detailed_prediction'),
        ),
        migrations.AlterUniqueTogether(
            name='detailedprediction',
            unique_together={('detailed_requirement', 'student')},
        ),
    ]