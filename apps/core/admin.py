"""
Por padrão o Django já fornece uma aplicação interna para administração do sistema que é O Django Admin,
ele é um componente fundamental do framework. Ele fornece uma interface de administração pronta para uso, que permite aos desenvolvedores e administradores gerenciar os dados de uma aplicação Django
por meio de uma interface web intuitiva.

Alguns dos recursos principais da aplicação interna Django Admin incluem:

Painel de controle personalizado: O Django Admin apresenta um painel de controle onde os modelos registrados são listados.
A partir desse painel, os administradores podem navegar pelos modelos e acessar as diversas funcionalidades disponíveis.


Gerenciamento de modelos: O Django Admin permite visualizar, criar, atualizar e excluir registros dos modelos registrados.
Essas operações são executadas em formulários gerados automaticamente, com base nas definições do modelo.


Pesquisa e filtragem: O Django Admin fornece recursos de pesquisa e filtragem integrados,
permitindo que os administradores localizem registros com base em critérios específicos.
Isso é especialmente útil quando há grandes quantidades de dados e é necessário encontrar informações específicas.


Controle de permissões: O Django Admin possui um sistema de controle de permissões embutido,
que permite definir quais usuários têm acesso a determinados modelos e ações.
Os desenvolvedores podem configurar permissões granulares para controlar o que cada usuário pode fazer no painel de administração.


Para o Django admin se tornar mais flexível as necessidades de cada app Django do seu projeto, você pode configurar tudo através do arquivo de modelo admin.py.

Agora fica mais fácil de entender o porquê do admin.py  ser  um componente importante em uma aplicação Django.
Ele é o ponto de partida para as personalizações. Nele, o programador pode definir as configurações de administração para os modelos de dados da app.

"""



from django.contrib import admin #importa o módulo admin da biblioteca django.contrib. Esse módulo contém as classes e funcionalidades necessárias para configurar e personalizar o painel de administração do Django.
from apps.core.models import Ferramentas #importa o modelo Ferramentas do aplicativo core localizado na pasta apps. O modelo Ferramentas é o modelo de dados que será registrado e gerenciado no painel de administração.

class FerramentasModelAdmin(admin.ModelAdmin): #Aqui, uma classe chamada FerramentasModelAdmin é definida. Essa classe herda da classe admin.ModelAdmin, que é a classe base para criar configurações personalizadas de administração. Ao criar essa classe, estamos criando uma configuração personalizada para o modelo Ferramentas no painel de administração.
    list_display = ('nome', 'ativa') #Esta linha define o atributo list_display da classe FerramentasModelAdmin. O list_display especifica quais campos do modelo serão exibidos na lista de registros no painel de administração. Nesse caso, os campos nome e ativa serão exibidos.
    search_fields = ('nome', 'ativa')#Aqui, o atributo search_fields é definido. Ele especifica quais campos serão usados para realizar a pesquisa no painel de administração. Neste caso, a pesquisa será feita nos campos nome e ativa.
    list_filter = ('nome','ativa') #Essa linha define o atributo list_filter. Ele permite que os registros sejam filtrados com base nos valores dos campos especificados. Neste caso, será possível filtrar os registros por nome e ativa.


admin.site.register(Ferramentas, FerramentasModelAdmin) #Finalmente, o modelo Ferramentas é registrado no painel de administração usando a função admin.site.register(). Passamos o modelo Ferramentas como primeiro argumento e a classe FerramentasModelAdmin como segundo argumento. Isso associa a configuração personalizada FerramentasModelAdmin ao modelo Ferramentas no painel de administração.





### RESUMO ###

"""

o arquivo admin.py da sua app Django, permite a configuração dos modelos da app na interface administrativa,
oferecendo uma maneira fácil de gerenciar e manipular os dados dos modelos configurados por meio de uma interface web intuitiva criada pelo Django Admin.

"""