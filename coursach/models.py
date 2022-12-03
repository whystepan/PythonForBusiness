from django.db import models



class Tour(models.Model):
    title = models.CharField('Название тура', max_length=64)
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='static')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Туры'

class TourPetition(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)
    middle_name = models.CharField('Отчество', max_length=20)
    phone = models.CharField('Номер телефона', max_length=32)
    email = models.EmailField('E-mail')
    date = models.DateField('Дата проведения')
    persons_count = models.IntegerField('Количество персон', default=1)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.last_name + '' + self.first_name

    class Meta:
        verbose_name_plural = 'Записи на туры'