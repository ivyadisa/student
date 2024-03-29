# Generated by Django 5.0 on 2023-12-25 12:25

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, choices=[('term_1', 'Term 1'), ('term_2', 'Term 2'), ('term_3', 'Term 3')], max_length=20)),
                ('session_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('year', models.CharField(blank=True, choices=[('2023', '2023'), ('2024', '2024')], max_length=20)),
                ('started_on', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('mathematics', 'Mathematics'), ('english', 'English'), ('kiswahili', 'Kiswahili'), ('chemistry', 'Chemistry')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_class_teacher', models.BooleanField(default=False)),
                ('is_finance', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('update_status', models.CharField(choices=[('pending', 'Pending'), ('updated', 'Updated')], default='pending', max_length=50)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'db_table': 'portal_customuser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('class_T', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.class')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='finance_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('exam_1', 'Exam 1'), ('exam_2', 'Exam 2'), ('exam_3', 'Exam 3'), ('opener', 'Opener')], max_length=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.session')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('adm_no', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('fee_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('gender', models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('yoa', models.DateField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
                ('user_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.class')),
                ('subjects', models.ManyToManyField(blank=True, to='portal.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Fee_entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=20, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.student')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.exam')),
                ('user_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
