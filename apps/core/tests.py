"""
Para entender qual é a função do arquivo de modelo tests.py dentro de uma app Django, você precisa entender o que é um teste automatizado.

Um teste automatizado é um procedimento de verificação de software que é executado automaticamente, sem a necessidade de intervenção manual.
É uma prática fundamental no desenvolvimento de software, na qual casos de teste são definidos e executados por meio de código automatizado.
Os testes automatizados têm o objetivo de validar se o software está funcionando corretamente e se atende aos requisitos especificados.
Eles permitem identificar erros, regressões e comportamentos indesejados no código de forma rápida e eficiente.

No Django, Os testes automatizados são desenvolvidos dentro do arquivo de modelo tests.py e geralmente escritos usando a classe django.test.TestCase ou suas subclasses.
Essas classes fornecem métodos e recursos para criar e executar testes.
Você pode definir métodos dentro da classe de teste, cada um representando um caso de teste específico.

Os testes automatizados no Django podem ser usados para verificar diferentes aspectos do seu aplicativo, como a funcionalidade das views, a renderização correta de templates, a validação de formulários,
a lógica de negócios, entre outros. Eles ajudam a garantir que o código do seu aplicativo esteja funcionando corretamente em diferentes cenários e situações.

Ao escrever testes automatizados, você define uma série de assert que são verificadas durante a execução do teste.
Os assert são usadas para verificar se um resultado esperado é igual ao resultado real. Por exemplo, você pode verificar se uma determinada view retorna um código de status HTTP correto,
se um template é usado corretamente ou se os dados são salvos corretamente no banco de dados.

Ao executar os testes automatizados, o Django cria um ambiente isolado para cada teste e executa os casos de teste de forma independente.
Ele captura e relata os testes que passaram e os que falharam, fornecendo informações úteis para depuração.


python manage.py test

"""


from django.test import TestCase, Client #Importa a classe TestCase do módulo django.test, que é a base para escrever testes automatizados no Django.
from django.urls import reverse #Importa a função reverse do módulo django.urls, que permite obter a URL reversa de uma view com base no seu nome.
from apps.core.models import Ferramentas #Importa o modelo Ferramentas do aplicativo core.models.
from io import BytesIO
from PIL import Image

class HomeViewTest(TestCase): #Define uma classe de teste chamada HomeViewTest que herda da classe TestCase.
    def setUp(self): #Define um método setUp que será executado antes de cada caso de teste. É usado para configurar o ambiente de teste antes de executar os casos de teste.
        # Criação de objetos Ferramentas para simular dados do banco de dados
        self.qrcode = Ferramentas.objects.create(nome="Gerador de QR Code")
        self.recibo = Ferramentas.objects.create(nome="Gerador de Recibo")
        self.senha = Ferramentas.objects.create(nome="Gerador de Senha")
        self.numeros = Ferramentas.objects.create(nome="Números Aleatórios")

    def test_home_view(self): #Define um método de teste chamado test_home_view que verifica o comportamento da view "home".

        url = reverse('home') #Obtém a URL da view "home" usando a função reverse e atribui-a à variável url.


        response = self.client.get(url) #Envia uma solicitação GET para a URL da view "home" usando o cliente de teste self.client e armazena a resposta na variável response.


        self.assertEqual(response.status_code, 200) #Verifica se o código de status da resposta é igual a 200 (indicando uma resposta bem-sucedida).


        self.assertTemplateUsed(response, 'index.html') #Verifica se o template utilizado na resposta é "index.html".

        # Verificação dos objetos Ferramentas no contexto da resposta
        self.assertEqual(response.context['qrcode'], self.qrcode) #Verifica se o objeto qrcode no contexto da resposta é igual ao objeto self.qrcode criado no método setUp. Essa verificação é feita para garantir que o objeto qrcode esteja presente no contexto da view.
        self.assertEqual(response.context['recibo'], self.recibo)
        self.assertEqual(response.context['senha'], self.senha)
        self.assertEqual(response.context['numeros'], self.numeros)





"""
Os testes automatizados são uma parte essencial do desenvolvimento de aplicativos Django, 
ele fornece uma forma de verificar e validar o comportamento do seu aplicativo de forma automática, ajudando a garantir que ele funcione conforme o esperado e cumpra os requisitos definidos. 
Além disso, os testes automatizados também facilitam a manutenção do código, pois permitem detectar problemas quando alterações são feitas no código existente. 
Com uma variedade de testes automatizados, você pode ter mais confiança na estabilidade e no desempenho do seu aplicativo Django.
"""



class FerramentaQRCodeTest(TestCase):
    def setUp(self):
        # Cria o objeto Ferramentas para o teste
        Ferramentas.objects.create(nome="Gerador de QR Code", ativa=True)

    def test_ferramenta_qrcode_get(self): #Este é o primeiro método de teste. Ele testa o comportamento quando uma requisição GET é feita para a view ferramenta_qrcode.

        client = Client() #Cria uma instância do cliente HTTP fornecido pelo Django para simular a realização de requisições.
        response = client.get(reverse('ferramenta_qrcode')) #Faz uma requisição GET para a URL mapeada para a view ferramenta_qrcode usando a função reverse para obter a URL com base no nome da view.
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta foi bem-sucedida

    def test_ferramenta_qrcode_post(self): #Este é o segundo método de teste. Ele testa o comportamento quando uma requisição POST é feita para a view ferramenta_qrcode.

        client = Client() #Cria uma nova instância do cliente HTTP.
        info = "Teste de informação" #Define uma variável info que armazena uma string de teste.
        response = client.post(reverse('ferramenta_qrcode'), {'informacao': info}) #Faz uma requisição POST para a URL mapeada para a view ferramenta_qrcode, passando a informação a ser inserida no qrcode.
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta foi bem-sucedida

        # Verifica se a resposta é uma imagem PNG
        self.assertEqual(response['Content-Type'], 'image/png')

        # Verifica se a imagem do QR Code é gerada corretamente
        qr_image = Image.open(BytesIO(response.content))
        self.assertEqual(qr_image.format, 'PNG')



class FerramentaRecibosTest(TestCase):
    def setUp(self):
        self.client = Client()
        Ferramentas.objects.create(nome="Gerador de Recibo", ativa=True)

    def test_envio_formulario_post_valido(self):


        url = reverse('ferramenta_recibos')

        # Dados do formulário válidos para o teste
        data = {
            'nome_pagador': 'João Silva',
            'endereco_pagador': 'Rua Teste, 123',
            'cpf_cnpj_pagador': '123.456.789-10',
            'cpf_cnpj_receptor': '987.654.321-00',
            'nome_receptor': 'Maria Souza',
            'descricao_servico': 'Serviço de Consultoria',
            'valor': '500.00',
            'cidade': 'São Paulo',
            'data_emissao': '2023-07-22',
        }

        # Faz uma requisição POST à view
        response = self.client.post(url, data)


        # Verifica se o PDF gerado não está vazio
        self.assertTrue(len(response.content) > 0)

        # Verifica se a view está retornando uma resposta com o content type correto
        self.assertEqual(response['Content-Type'], 'application/pdf')

        # Verifica se o nome do arquivo do PDF está definido corretamente na resposta
        self.assertIn('recibo.pdf', response['Content-Disposition'])


class FerramentaSenhaTest(TestCase):
    def setUp(self):
        # Crie um objeto Ferramentas para teste
        self.ferramenta_senha = Ferramentas.objects.create(nome="Gerador de Senha", ativa=True)

    def test_ferramenta_senha_get(self):
        # Teste para solicitação GET
        response = self.client.get(reverse('ferramenta_senha'))

        # Verifique se a resposta tem código de status 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifique se a chave 'senha_gerada' está no contexto do template
        self.assertIn('senha_gerada', response.context)

        # Verifique se a view está usando o template 'senha.html'
        self.assertTemplateUsed(response, 'senha.html')

    def test_ferramenta_senha_post(self):
        # Teste para solicitação POST
        qtdcaracter = 8  # Número de caracteres para a senha
        response = self.client.post(reverse('ferramenta_senha'), {'qtdcaracter': qtdcaracter})

        # Verifique se a resposta tem código de status 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifique se a chave 'senha_gerada' está no contexto do template
        self.assertIn('senha_gerada', response.context)

        # Verifique se a view está usando o template 'senha.html'
        self.assertTemplateUsed(response, 'senha.html')

        # Verifique se a senha gerada tem o número correto de caracteres
        senha_gerada = response.context['senha_gerada']
        self.assertEqual(len(senha_gerada), qtdcaracter)

    def test_ferramenta_senha_desativada(self):
        # Simule a desativação da ferramenta
        self.ferramenta_senha.ativa = False
        self.ferramenta_senha.save()

        response = self.client.get(reverse('ferramenta_senha'))

        # Verifique se a resposta é um redirecionamento (código de status 302)
        self.assertEqual(response.status_code, 302)



class FerramentaNumerosTest(TestCase):

    def setUp(self):
        self.ferramenta_numeros_url = reverse('ferramenta_numeros')
        self.ferramenta = Ferramentas.objects.create(nome="Números Aleatórios", ativa=True)


    def test_get_request(self):
        # Testa se a view é carregada corretamente quando uma solicitação GET é feita.
        response = self.client.get(self.ferramenta_numeros_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'numeros.html')

    def test_invalid_interval(self):
        # Testa se a mensagem correta é exibida quando o intervalo informado é inválido.
        response = self.client.post(self.ferramenta_numeros_url, data={'qtdnumeros': '5', 'ninicio': '10', 'nfim': '5'})
        self.assertContains(response, "Você informou o número de início maior do que o número de fim")
        self.assertTemplateUsed(response, 'numeros.html')

    def test_insufficient_interval(self):
        # Testa se a mensagem correta é exibida quando o intervalo informado é insuficiente para a quantidade de números desejada.
        response = self.client.post(self.ferramenta_numeros_url, data={'qtdnumeros': '10', 'ninicio': '1', 'nfim': '5'})
        self.assertContains(response, "Você informou um intervalo de número insuficiente para a quantidade de número desejada")
        self.assertTemplateUsed(response, 'numeros.html')

    def test_valid_sequence_generation(self):
        # Testa se a sequência de números é gerada corretamente quando uma solicitação POST válida é feita.
        response = self.client.post(self.ferramenta_numeros_url, data={'qtdnumeros': '5', 'ninicio': '1', 'nfim': '10'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'numeros.html')
