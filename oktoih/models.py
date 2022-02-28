from django.db import models


class SundayServicesVespers(models.Model):
    objects = models.Manager()
    voice = models.IntegerField(verbose_name='Глас', null=True)
    gv1 = models.TextField(verbose_name='Октоиха 1', null=True)
    gv2 = models.TextField(verbose_name='Октоиха 2', null=True)
    gv3 = models.TextField(verbose_name='Октоиха 3', null=True)
    gv4 = models.TextField(verbose_name='Анатолиевы 1', null=True)
    gv5 = models.TextField(verbose_name='Анатолиевы 2', null=True)
    gv6 = models.TextField(verbose_name='Анатолиевы 3', null=True)
    gv7 = models.TextField(verbose_name='Анатолиевы 4', null=True)
    gv8 = models.TextField(verbose_name='Богородице 1', null=True)
    gv9 = models.TextField(verbose_name='Богородице 2', null=True)
    gv10 = models.TextField(verbose_name='Богородице 3', null=True)
    dogmatic = models.TextField(verbose_name='Догматик', null=True)
    st1 = models.TextField(verbose_name='На стиховне 1', null=True)
    st2 = models.TextField(verbose_name='На стиховне 2', null=True)
    st3 = models.TextField(verbose_name='На стиховне 3', null=True)
    st4 = models.TextField(verbose_name='На стиховне 4', null=True)
    bg_st = models.TextField(verbose_name='Богородичен на стиховне', null=True)
    matins = models.OneToOneField('SundayServicesMatins', on_delete=models.PROTECT, null=True)
    canon = models.OneToOneField('Canon', on_delete=models.PROTECT, null=True)
    trvs = models.ForeignKey('SundayTropar', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Воскресные службы вечерня'
        verbose_name_plural = 'Воскресные службы вечерня'
        ordering = ['voice']

    def __str__(self):
        return f'{str(self.voice)}, {self.gv1}'


class SundayServicesMatins(models.Model):
    voice = models.IntegerField(verbose_name='Глас')
    tropar = models.TextField(verbose_name='Тропарь')
    bg_tr = models.TextField(verbose_name='Богородичен тропаря')
    sed1a = models.TextField(verbose_name='По первой кафизме седален (а)')
    sed1b = models.TextField(verbose_name='По первой кафизме седален (б)')
    bg_sed1 = models.TextField(verbose_name='Богородичен первого седальна')
    sed2a = models.TextField(verbose_name='По второй кафизме седален (а)')
    sed2b = models.TextField(verbose_name='По второй кафизме седален (б)')
    bg_sed2 = models.TextField(verbose_name='Богородичен второго седальна')
    ipac = models.TextField(verbose_name='Ипакои',)
    step = models.TextField(verbose_name='Степенна',)
    bg_step = models.TextField(verbose_name='Слава, И ныне степенны')
    procimen = models.TextField(verbose_name='Прокимен перед Евангелием')
    st_proc = models.TextField(verbose_name='Стих прокимена')
    kondac = models.TextField(verbose_name='Кондак')
    icos = models.TextField(verbose_name='Икос')
    hv1 = models.TextField(verbose_name='Стихира на хвалитех 1')
    hv2 = models.TextField(verbose_name='Стихира на хвалитех 2')
    hv3 = models.TextField(verbose_name='Стихира на хвалитех 3')
    hv4 = models.TextField(verbose_name='Стихира на хвалитех 4')
    hv5 = models.TextField(verbose_name='Стихира на хвалитех 5')
    hv6 = models.TextField(verbose_name='Стихира на хвалитех 6')
    hv7 = models.TextField(verbose_name='Стихира на хвалитех 7')
    hv8 = models.TextField(verbose_name='Стихира на хвалитех 8')

    class Meta:
        verbose_name = 'Воскресные службы утреня'
        verbose_name_plural = 'Воскресные службы утреня'
        ordering = ['voice']

    def __str__(self):
        return str(self.voice)


class Canon(models.Model):
    voice = models.IntegerField(verbose_name='Глас')
    pesn1 = models.TextField(verbose_name='Песнь 1')
    pesn3 = models.TextField(verbose_name='Песнь 3')
    pesn4 = models.TextField(verbose_name='Песнь 4')
    pesn5 = models.TextField(verbose_name='Песнь 5')
    pesn6 = models.TextField(verbose_name='Песнь 6')
    pesn7 = models.TextField(verbose_name='Песнь 7')
    pesn8 = models.TextField(verbose_name='Песнь 8')
    pesn9 = models.TextField(verbose_name='Песнь 9')

    class Meta:
        verbose_name = 'Канон'
        verbose_name_plural = 'Канон'
        ordering = ['voice']

    def __str__(self):
        return str(self.voice)


class SundayTropar(models.Model):
    voices = models.CharField(max_length=10, verbose_name='Гласы')
    text = models.TextField(verbose_name='Тропарь воскресный')

    class Meta:
        verbose_name = 'Тропарь воскресный'
        verbose_name_plural = 'Тропать воскресный'

    def __str__(self):
        return self.text


class EvangSunday(models.Model):
    evang = models.TextField(verbose_name='Евангелие воскресное')
    exapost = models.TextField(verbose_name='Эксапостиларий')
    st_ev = models.TextField(verbose_name='Стихира еавнгельская')

    class Meta:
        verbose_name = 'Воскресное евангелие, эксапостиларий, стихира евангельская'
        verbose_name_plural = 'Воскресное евангелие, эксапостиларий, стихира евангельская'

    def __str__(self):
        return f'{self.evang} {self.exapost} {self.st_ev}'
