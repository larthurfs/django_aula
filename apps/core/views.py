"""

O views.py desempenha o papel na camada de controle do padrão de arquitetura Model-View-Controller (MVC) ou Model-View-Template (MVT) do Django.

Em termos simples, o arquivo views.py contém as funções ou classes responsáveis por processar as requisições dos usuários e fornecer as respostas correspondentes.
Essas respostas podem ser páginas HTML renderizadas, redirecionamentos, dados JSON, ou qualquer outra forma de retorno que o sistema web precise fornecer.
O arquivo views.py age como um intermediário entre o usuário e os modelos de dados.
Ele recebe as solicitações HTTP (como GET, POST, PUT, DELETE) dos usuários, extrai os dados necessários dessas solicitações e os manipula de acordo.
Essa manipulação pode envolver a criação, leitura, atualização ou exclusão (CRUD) de objetos no banco de dados, bem como a interação com outros sistemas ou serviços externos.

Além disso, o arquivo views.py pode conter lógica adicional para processar formulários, autenticação de usuários, controle de acesso, tratamento de erros, e outras funcionalidades específicas do aplicativo.
Ele fornece a camada de controle que coordena a interação entre os modelos de dados (definidos no arquivo models.py) e as visualizações (templates HTML) do aplicativo.

"""

from django.shortcuts import render, redirect  # importa a função "render" do módulo "shortcuts" do Django. O módulo "shortcuts" contém várias funções utilitárias que simplificam o desenvolvimento de views no Django. A função "render" é uma das principais funções do módulo "shortcuts". Ela é amplamente utilizada para renderizar templates HTML com dados contextuais e retornar uma resposta HTTP ao navegador do usuário.
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from apps.core.forms import ReciboForm
from apps.core.models import Ferramentas  # importa o modelo Ferramentas do arquivo models.py localizado na app core. Isso permite que a view acesse e manipule os objetos Ferramentas definidos no modelo.
import qrcode
from io import BytesIO
from django.http import HttpResponse

from apps.core.numeros import verificar_intervalo, sequencia_numeros
from apps.core.recibo import gerador_recibo
from apps.core.senha import gerar_senha


# coment
def home(request):  # define uma função chamada home que recebe um objeto request como parâmetro. Essa função representa a view responsável por processar as requisições para a página inicial.

    qrcode = Ferramentas.objects.get(nome="Gerador de QR Code")  # Recupera um objeto Ferramentas do banco de dados com o atributo nome igual a " Gerador de QR Code" e o atribui à variável qrcode. O método get() retorna um único objeto que corresponde à consulta.
    recibo = Ferramentas.objects.get(nome="Gerador de Recibo")
    senha = Ferramentas.objects.get(nome="Gerador de Senha")
    numeros = Ferramentas.objects.get(nome="Números Aleatórios")

    context = {'qrcode': qrcode, 'recibo': recibo, 'senha': senha, 'numeros': numeros, }  # cria um dicionário chamado context que contém os objetos recuperados nas etapas anteriores. Os objetos são associados a chaves específicas, como, 'qrcode', 'recibo', 'senha' e 'numeros'. Esse dicionário será usado para fornecer os dados para o template.

    return render(request, 'index.html', context)  # retorna o resultado da função render(). Ela recebe o objeto request, o nome do template 'index.html' e o dicionário context como argumentos. A função render() renderiza o template com os dados fornecidos no contexto e retorna uma resposta HTTP que será enviada de volta ao navegador do usuário.


"""
Porem ainda não vamos conseguir renderizar o template index.html por um motivo claro.
No Djnago toda view tem uma URL e nos só vamos criar a url dessa view na nossa próxima etapa.
"""


def ferramenta_qrcode(request): #Definição de função ferramenta_qrcode. Essa função é a view Django que é responsável por processar uma solicitação HTTP relacionada à ferramenta de geração de QR Code. A função recebe um objeto request como parâmetro, que contém informações sobre a solicitação feita pelo usuário.
    qrcodee = Ferramentas.objects.get(nome="Gerador de QR Code") #Recebendo um objeto Ferramentas do banco de dados usando o método get(), retornamos o objeto com o campo nome igual a "Gerador de QR Code" e armazenando-o na variável qrcodee.
    if not qrcodee.ativa: #verifica se a propriedade ativa do objeto qrcodee é falsa. Se a ferramenta estiver desativada, redireciona o usuário para a página "home".
        return redirect('home')

    if request.method == "GET": #verifica se o método da solicitação é "GET". Se for o caso, retorna o template qrcode.html. Se for um POST a vew vai gerar o QR code com as informações fornecidas pelo o usuário.
        return render(request, 'qrcode.html')
    else:
        info = request.POST.get("informacao") #Nessa linha, estamos tratando a situação em que o método da solicitação é  um "POST". Estamos obtendo o valor do parâmetro " informacao " do objeto request.POST e atribuindo-o à variável info.
        # Gera o QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=5) #Cria um objeto QRCode usando a classe QRCode do módulo qrcode. O parâmetro version é definido como 1, o que determina a versão do código QR a ser gerado. O parâmetro box_size é definido como 10, o que especifica o tamanho de cada caixa (pixel) do código QR. O parâmetro border é definido como 5, que representa a largura da borda do código QR em caixas (pixels).
        qr.add_data(info) #Adicionamos os dados ao objeto qr gerado nalinha anterior. O valor info é passado como argumento para o método add_data(), que adiciona os dados ao código QR.
        qr.make(fit=True) #Chamamos o método make() do objeto qr. Passamos o argumento fit=True, que indica que o código QR deve ser ajustado automaticamente para caber em tamanho, se necessário.
        qr_image = qr.make_image(fill_color="black", back_color="white") #Chamamos novamente o método make() do objeto qr, mas desta vez estamos usando o método make_image(). Passamos fill_color="black" para definir a cor de preenchimento do código QR como preto e back_color="white" para definir a cor de fundo como branco. O resultado dessa chamada é a geração da imagem do código QR, que é atribuída à variável qr_image.

        # Cria um buffer de imagem
        buffer = BytesIO() #cria um objeto BytesIO vazio chamado buffer. O BytesIO é um objeto que age como um buffer de memória para armazenar dados binários.
        qr_image.save(buffer) #Chamando o método save() do objeto qr_image para salvar a imagem do código QR no buffer. O buffer é usado como destino para salvar a imagem.
        buffer.seek(0) #Chamando o método seek() no objeto buffer para definir o ponteiro de leitura/gravação para o início do buffer. Isso garante que, quando o buffer for lido mais tarde, ele começará a partir do início dos dados armazenados nele.

        # Define o cabeçalho de resposta para exibir a imagem
        response = HttpResponse(content_type='image/png') #Criando um objeto HttpResponse. Especificamos o tipo de conteúdo como 'image/png', indicando que a resposta será uma imagem PNG. O objeto response será usado para retornar a imagem do código QR como resposta HTTP.
        response['Content-Disposition'] = 'attachment; filename="qrcode.png"' #definindo o cabeçalho de resposta 'Content-Disposition' para indicar que o conteúdo é um anexo com o nome de arquivo "qrcode.png". Isso significa que, ao receber a resposta, o navegador ou cliente que está fazendo a solicitação poderá tratar a resposta como um arquivo para download com o nome especificado.
        response.write(buffer.getvalue()) #escrevendo os dados contidos no objeto buffer na resposta response. buffer.getvalue() retorna os dados do buffer como uma sequência de bytes, que são então escritos na resposta usando o método write(). Esses dados representam a imagem do código QR que foi armazenada no buffer anteriormente.

        return response #Retornamos a resposta contendo a imagem do QR Code ao usuário.



def ferramenta_recibos(request):
    recibo = Ferramentas.objects.get(nome="Gerador de Recibo")
    if not recibo.ativa:
        return redirect('home')

    if request.method == 'POST':
        form = ReciboForm(request.POST) #Cria uma instância do formulário ReciboForm, passando os dados submetidos através do request.POST.
        if form.is_valid(): #Verifica se os dados do formulário são válidos, realizando a validação com base nas regras definidas no ReciboForm.
            # Obter os dados do formulário
            nome_pagador = form.cleaned_data['nome_pagador'] # Obtém o valor do campo "nome_pagador" do formulário validado e atribui a variável nome_pagador.
            endereco_pagador = form.cleaned_data['endereco_pagador']
            cpf_cnpj_pagador = form.cleaned_data['cpf_cnpj_pagador']
            cpf_cnpj_receptor = form.cleaned_data['cpf_cnpj_receptor']
            nome_receptor = form.cleaned_data['nome_receptor']
            descricao_servico = form.cleaned_data['descricao_servico']
            valor = form.cleaned_data['valor']
            cidade = form.cleaned_data['cidade']
            data_emissao = form.cleaned_data['data_emissao']


            response = HttpResponse(content_type='application/pdf') #): Cria um objeto HttpResponse para armazenar a resposta HTTP que será enviada ao cliente. A resposta é definida com o tipo de conteúdo 'application/pdf', indicando que se trata de um arquivo PDF.
            response['Content-Disposition'] = 'attachment; filename="recibo.pdf"' #Define o cabeçalho Content-Disposition da resposta HTTP. Neste caso, o valor 'attachment' indica que o arquivo deve ser tratado como um anexo e não ser exibido diretamente no navegador. Em seguida, é especificado o nome do arquivo como 'recibo.pdf'.



            # Cria o PDF no objeto Canvas

            pdf = canvas.Canvas(response, pagesize=(A5[1], A5[0])) #Cria um objeto canvas.Canvas para criar um PDF. O objeto response é passado como parâmetro, indicando que o PDF será gerado na resposta HTTP. O tamanho da página é definido como (A5[1], A5[0]), que corresponde ao tamanho da página A5.
            gerador_recibo(pdf, nome_pagador, cpf_cnpj_pagador, descricao_servico, cidade, data_emissao, valor,
                           nome_receptor, cpf_cnpj_receptor, endereco_pagador) #Chama a função gerador_recibo passando o objeto pdf e os dados do recibo como argumentos. Essa função é responsável por gerar o conteúdo do recibo no PDF.


            return response #Retorna a resposta HTTP, que contém o PDF gerado, para ser enviada ao cliente.

    else:
        form = ReciboForm()
    return render(request, 'recibo.html', {'form': form}) #Renderiza o template 'recibo.html', passando o objeto request, o formulário form e seus campos como contexto. Isso permite que o formulário seja exibido na página 'recibo.html' para o usuário preencher e submeter os dados.




def ferramenta_senha(request):
    senha = Ferramentas.objects.get(nome="Gerador de Senha")
    if not senha.ativa:
        return redirect('home')

    if request.method == "GET":
        senha_gerada = ""
        return render(request, 'senha.html', {"senha_gerada":senha_gerada})

    else:
        caracter = request.POST.get("qtdcaracter")
        senha_gerada = gerar_senha(int(caracter))

        return render(request, 'senha.html', {"senha_gerada":senha_gerada})



def ferramenta_numeros(request):
    numeros = Ferramentas.objects.get(nome="Números Aleatórios")
    if not numeros.ativa:
        return redirect('home')


    if request.method == "GET":

        numeros_gerados = ""
        return render(request, 'numeros.html', {"numeros_gerados":numeros_gerados})

    else:
        qtd_numeros = int(request.POST.get("qtdnumeros"))
        n_inicio = int(request.POST.get("ninicio"))
        n_fim = int(request.POST.get("nfim"))
        if n_inicio > n_fim:
            numeros_gerados = "Você informou o número de início maior do que o número de fim"
            return render(request, 'numeros.html', {"numeros_gerados": numeros_gerados})

        intervalo = verificar_intervalo(n_fim, n_inicio, qtd_numeros)
        if intervalo:
            numeros_gerados = "Você informou um intervalo de número insuficiente para a quantidade de número desejada"
            return render(request, 'numeros.html', {"numeros_gerados": numeros_gerados})



        numeros_gerados = sequencia_numeros(qtd_numeros, n_inicio, n_fim)

        return render(request, 'numeros.html', {"numeros_gerados":numeros_gerados})