from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    CHOICE_STATUS = (
        ('EE', 'Em execução'),
        ('PA', 'Parado'),
        ('AR', 'Aguardando recurso'),
        ('CD', 'Concluído'),
    )
    name = models.CharField(u'Nome', max_length=150)
    started_at = models.DateField(u'Data de início')
    finished_at = models.DateField(u'Data de fim')
    objective = models.CharField(u'Objetivo', max_length=250)
    specification = models.TextField(u'Espeficificação')
    users = models.ManyToManyField(User, verbose_name='Usuários')
    attachment = models.FileField(u'Anexo', upload_to='attachments', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    obs = models.TextField(u'Observação', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='owner', verbose_name='Usuário')
    status = models.CharField(u'Status', max_length=5,  choices=CHOICE_STATUS, default='EE')

    class Meta:
        ordering = ['id']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
    
    def __str__(self):
        return self.name
