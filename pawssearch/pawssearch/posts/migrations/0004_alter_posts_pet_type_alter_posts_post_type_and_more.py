# Generated by Django 5.1.1 on 2024-11-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_posts_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pet_type',
            field=models.CharField(choices=[('CAT', 'Котка'), ('DOG', 'Куче'), ('OTHER', 'Друго')], max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_type',
            field=models.CharField(choices=[('FOUND', 'Намерено'), ('MISSING', 'Изгубено'), ('FOR_ADOPTION', 'За осиновяване'), ('FOR_SELLING', 'За продажба')], max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='region',
            field=models.CharField(choices=[('BLAGOEVGRAD', 'Благоевград'), ('BURGAS', 'Бургас'), ('VARNA', 'Варна'), ('VELIKO_TARNOVO', 'Велико Търново'), ('VIDIN', 'Видин'), ('VRATSA', 'Враца'), ('GABROVO', 'Габрово'), ('DOBRICH', 'Добрич'), ('KARDZHALI', 'Кърджали'), ('KYUSTENDIL', 'Кюстендил'), ('LOVECH', 'Ловеч'), ('MONTANA', 'Монтана'), ('PAZARDZHIK', 'Пазарджик'), ('PERNIK', 'Перник'), ('PLEVEN', 'Плевен'), ('PLOVDIV', 'Пловдив'), ('RAZGRAD', 'Разград'), ('RUSSE', 'Русе'), ('SILISTRA', 'Силистра'), ('SLIVEN', 'Сливен'), ('SMOLYAN', 'Смолян'), ('SOFIA', 'София - град'), ('SOFIA_OBLAST', 'София - регион'), ('STARA_ZAGORA', 'Стара Загарора'), ('TARGOVISHTE', 'Търговище'), ('HASKOVO', 'Хасково'), ('SHUMEN', 'Шумен'), ('YAMBOL', 'Ямбол')], max_length=200),
        ),
    ]
