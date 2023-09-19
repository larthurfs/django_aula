"""
Antes de falar sobre o arquivo de modelo forms.py, vamos revisar o que é um formulário HTML

Um formulário HTML é um elemento essencial da web que permite aos usuários interagirem com o sistema fornecendo informações por meio de campos de entrada, caixas de seleção, botões e etc.
Ao enviar o formulário, esses dados podem ser processados pelo servidor para executar ações, armazenar informações em um banco de dados ou gerar uma resposta personalizada.

O Django consegue simplificar a criação e o processamento de formulários HTML. Ele fornece um conjunto de classes e métodos que facilitam a construção e a manipulação de formulários.
Para criar um formulário HTML usando o Django, você precisa definir uma classe de formulário, essa classe herda da classe forms.Form ou forms.ModelForm,
dependendo se você deseja criar um formulário comum ou um formulário vinculado a um modelo de banco de dados.
Dentro da classe, você define os campos que deseja incluir no formulário, como campos de texto, caixas de seleção, etc.
Cada campo é representado por uma instância de uma classe de campo fornecida pelo Django, como forms.CharField,  forms.BooleanField e etc.
Você também pode adicionar validações aos campos para garantir que os dados fornecidos pelos usuários estejam corretos.

Após definir o formulário, você precisa passá-lo para a view Django para que ele seja renderizado no navegador do usuário.
Na view, você cria uma instância do formulário e a passa para o contexto do template para renderização.
A view também é responsável por processar os dados enviados pelo usuário quando o formulário é submetido.
Ao processar os dados enviados pelo usuário, a view verifica se o formulário é válido, ou seja, se os dados fornecidos são válidos de acordo com as regras definidas nos campos do formulário.
Se o formulário for válido, você pode acessar os dados enviados pelo usuário através do atributo cleaned_data do formulário e executar as ações necessárias.
Caso contrário, você pode renderizar novamente o formulário com mensagens de erro para o usuário corrigir os campos inválidos.

Como o Django fornece toda essa facilidade para a criação de formulários HTML, modularizar os formulários da app em um arquivo de modelo forms.py
traz benefícios de organização, reutilização de código, separação de responsabilidades, facilidade de teste e clareza do código.
Apesar do Djando não criar o arquivo de modelo forms.py de forma automática para a app, essa uma prática recomendada no desenvolvimento das suas apps Django que vai contribuir para um código mais limpo,
estruturado e fácil de manter.

"""


from django import forms #Importa o módulo forms do pacote django, que contém classes para criar formulários no Django.

class ReciboForm(forms.Form): #Cria uma classe chamada ReciboForm que herda da classe forms.Form. A classe forms.Form no Django é uma classe independente de banco de dados usada para criar e gerenciar formulários, permitindo definir a estrutura, validação e processamento dos dados submetidos pelos usuários, sem estar diretamente ligada a um banco de dados.
    nome_pagador = forms.CharField(label='Nome do Pagador') #Cria um campo de formulário do tipo CharField chamado nome_pagador. Esse campo será usado para capturar o nome do pagador. O parâmetro label define o rótulo exibido para o campo no formulário.
    endereco_pagador = forms.CharField(label='Endereço do Pagador')
    cpf_cnpj_pagador = forms.CharField(label='CPF/CNPJ do Pagador')
    nome_receptor = forms.CharField(label='Nome do Receptor')
    cpf_cnpj_receptor = forms.CharField(label='CPF/CNPJ do Receptor')
    descricao_servico = forms.CharField(label='Descrição do Serviço')
    valor = forms.DecimalField(label='Valor')
    cidade = forms.CharField(label='Cidade')
    data_emissao = forms.DateField(label='Data de Emissão')