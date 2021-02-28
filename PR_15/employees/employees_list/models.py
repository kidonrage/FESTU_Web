from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    second_name = models.CharField('Фамилия', max_length=255)
    date = models.DateTimeField('Дата рождения')
    address = models.CharField('Место жительства', max_length=255)
    education = models.TextField('Образование')
    job = models.CharField('Специальность', max_length=255)
    department = models.CharField('Подразделение', max_length=255)
    salary = models.DecimalField('Оклад ($)', decimal_places=2, max_digits=100)
    employment_date = models.DateTimeField('Дата прихода в фирму', max_length=255)
    last_promotion_date = models.DateTimeField('Дата последнего назначения', max_length=255)

    def __str__(self):
        return self.second_name
