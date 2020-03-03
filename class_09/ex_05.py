import requests
import  unittest

def get_endereco(cep):
    return requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()

class TestGetEndereco(unittest.TestCase):

    def test_get_endereco(self):
        cep = '03136040'
        resposta = get_endereco(cep)
        self.assertEqual(
            resposta['logradouro'],
            'Rua Falchi Gianini'
        )

if __name__ == '__main__':
    unittest.main()