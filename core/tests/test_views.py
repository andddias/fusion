from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados_validos = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
        }
        self.dados_invalidos = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
        }
        self.cliente = Client()

    def test_fom_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados_validos)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados_invalidos)
        self.assertEquals(request.status_code, 200)
