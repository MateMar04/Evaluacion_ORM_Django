# Generated by Django 4.1.3 on 2022-11-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Barrios',
            fields=[
                ('cod_barrio', models.IntegerField(db_column='COD_BARRIO', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='NOMBRE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'BARRIOS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calles',
            fields=[
                ('cod_calle', models.IntegerField(db_column='COD_CALLE', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='NOMBRE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'CALLES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('cod_cliente', models.IntegerField(db_column='COD_CLIENTE', primary_key=True, serialize=False)),
                ('apellido', models.CharField(blank=True, db_column='APELLIDO', max_length=30, null=True)),
                ('nombre', models.CharField(blank=True, db_column='NOMBRE', max_length=30, null=True)),
                ('altura', models.IntegerField(blank=True, db_column='ALTURA', null=True)),
                ('telefono', models.DecimalField(blank=True, db_column='TELEFONO', decimal_places=0, max_digits=10, null=True)),
                ('cuit', models.DecimalField(blank=True, db_column='CUIT', decimal_places=0, max_digits=10, null=True)),
                ('deudor', models.CharField(blank=True, db_column='DEUDOR', max_length=1, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=75, null=True)),
            ],
            options={
                'db_table': 'CLIENTES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CondicionesIva',
            fields=[
                ('cod_condicion_iva', models.IntegerField(db_column='COD_CONDICION_IVA', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='DESCRIPCION', max_length=30, null=True)),
            ],
            options={
                'db_table': 'CONDICIONES_IVA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallesFacturas',
            fields=[
                ('cod_detalle', models.IntegerField(db_column='COD_DETALLE', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, db_column='CANTIDAD', null=True)),
            ],
            options={
                'db_table': 'DETALLES_FACTURAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('nro_factura', models.IntegerField(db_column='NRO_FACTURA', primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, db_column='FECHA', null=True)),
            ],
            options={
                'db_table': 'FACTURAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormasPago',
            fields=[
                ('cod_forma_pago', models.IntegerField(db_column='COD_FORMA_PAGO', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='DESCRIPCION', max_length=30, null=True)),
            ],
            options={
                'db_table': 'FORMAS_PAGO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('cod_localidad', models.IntegerField(db_column='COD_LOCALIDAD', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='NOMBRE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'LOCALIDADES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plantas',
            fields=[
                ('cod_planta', models.IntegerField(db_column='COD_PLANTA', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='DESCRIPCION', max_length=20, null=True)),
                ('precio', models.DecimalField(blank=True, db_column='PRECIO', decimal_places=2, max_digits=8, null=True)),
                ('stock', models.IntegerField(blank=True, db_column='STOCK', null=True)),
            ],
            options={
                'db_table': 'PLANTAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('cod_provincia', models.IntegerField(db_column='COD_PROVINCIA', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='NOMBRE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'PROVINCIAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposPlantas',
            fields=[
                ('cod_tipo_planta', models.IntegerField(db_column='COD_TIPO_PLANTA', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='NOMBRE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'TIPOS_PLANTAS',
                'managed': False,
            },
        ),
    ]
