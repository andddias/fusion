import uuid
from django.db import models
from stdimage.models import StdImageField


# Função geradora de nomes aleatorios p/ imagens recebidas de up-load
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


ICONE_CHOICES = (
    ('lni-cog', 'Engrenagem'),
    ('lni-stats-up', 'Gráfico'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
    ('lni-laptop-phone', 'Laptop/Phone'),
    ('lni-leaf', 'Folha'),
    ('lni-layers', 'Camadas'),
)


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=35)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=110)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480,
                                                                                    'height': 480,
                                                                                    'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Recurso(Base):
    LADO_CAIXA_CHOICES = (
        ('box-item wow fadeInLeft', 'Esquerda'),
        ('box-item wow fadeInRight', 'Direita'),
    )

    titulo = models.CharField('Título', max_length=22)
    descricao = models.CharField('Descrição', max_length=85)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)
    lado = models.CharField('Lado', max_length=25, choices=LADO_CAIXA_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.titulo
