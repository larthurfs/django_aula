
"""

O arquivo apps.py é um arquivo de configuração de aplicativo em um projeto Django, ele contém uma classe chamada Config que por padrão o Django cria essa classe com o nome do python packge seguido de Config,
para o nosso caso o Django nomearia a classe como CoreConfig essa classe  é uma subclasse da classe de AppConfig fornecida pelo Django.
Essa classe que vai permite que você defina várias opções e comportamentos específicos para o seu aplicativo. Aqui vamos falar das configurações que vem como padrão que são a name e o default_auto_field

"""




from django.apps import AppConfig # Essa linha importa a classe AppConfig do módulo django.apps do Django. A classe AppConfig é usada para configurar um aplicativo Django.


class CoreConfig(AppConfig): #Aqui, estamos definindo uma nova classe chamada CoreConfig, que é uma subclasse da classe AppConfig. Isso significa que CoreConfig herdará todos os atributos e métodos da classe AppConfig e poderá ser usada para configurar um aplicativo específico.

    default_auto_field = 'django.db.models.BigAutoField' #default_auto_field : É usado para especificar o tipo de campo automático a ser usado como chave primária para os models do aplicativo. Vamos entender melhor essa configuração quando estiver criando o models.py

    name = 'apps.core'  # name: Serve para definir o nome do aplicativo atribuindo uma string à variável "name" dentro da classe "Config".  Por padrão, o Django usa o nome do diretório do aplicativo como o nome do aplicativo.




"""
Agora que temos todo o código necessário dentro do apps.py, 
podemos integrar ela ao sistema colocando ela dentro da lista INSTALLED_APPS que fica dentro do settings.py que faz partes dos arquivos de configuração do projeto Djnago.

"""

###### RESUMO ########

"""
Em resumo, o arquivo apps.py é usado para configurar e personalizar uma app Django específica, 
definindo opções como name, default_auto_field e outras configurações relacionadas a app. Para o projeto django identificar a app, você precisa incluir ela dentro da lista INSTALLED_APPS.
"""