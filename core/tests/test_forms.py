from django.test import TestCase

from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'André Luiz'
        self.email = 'and.ddias@gmail.com'
        self.assunto = 'Assunto de teste'
        self.mensagem = 'Mensagem de teste!\nMensagem de teste!\nMensagem de teste!\nMensagem de teste!'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)  # ContatoForm(request.POST)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()  # Necessario para validação dos dados do formulario
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()  # Necessario para validação dos dados do formulario
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)
