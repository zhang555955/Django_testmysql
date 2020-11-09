# Generated by Django 3.0 on 2020-11-07 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者姓名')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='作者年龄')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, verbose_name='作者性别')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='作者邮箱')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='作者电话')),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32, verbose_name='分类标签')),
                ('description', models.TextField(verbose_name='分类描述')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='文章标题')),
                ('time', models.DateField(verbose_name='文章发表日期')),
                ('description', models.CharField(max_length=1024, verbose_name='文章描述')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('author', models.ForeignKey(default='默认值', on_delete=django.db.models.deletion.SET_DEFAULT, to='app01.Author')),
                ('classify', models.ManyToManyField(to='app01.Classify')),
            ],
        ),
    ]
