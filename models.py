from django.db import models

# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True,
                               verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубликовано')
    #Создадим во вторичной модели такое поле, назвав его rubric
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')
    #Класс ForeignKey представляет поле внешнего ключа, в котором
    # будет храниться ключ записи из первичной модели.

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20,
                            db_index=True, verbose_name='Название')
    def __str__(self):
        return self.name #В качестве строкового представления
        # мы выводим название рубрики

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


