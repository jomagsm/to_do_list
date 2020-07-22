from django.db import models
STATUS_CHOICE = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Article(models.Model):
    name = models.TextField(max_length=1000, null=False, default=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, choices=STATUS_CHOICE, default='new')
    create_at = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)
