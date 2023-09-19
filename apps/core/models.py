"""
O arquivo de modelo, models.py desempenha o papel de definição e estruturação dos dados da app Django. 
O objetivo principal desse arquivo é criar as classes que representaram as tabelas do banco de dados da app django dentro do banco de dados configurado no projeto.


As classes que vão ser criadas no models.py  são subclasses da classe Model, fornecida pelo framework Django. 
Ao criar uma classe de modelo, você está essencialmente criando uma representação em código de uma tabela no banco de dados. 
Cada atributo da classe de modelo geralmente corresponde a uma coluna na tabela, especificando seu tipo de dados e quaisquer opções adicionais.

"""""


"""
Dentro das classes de modelo, você pode definir campos como CharField (campo de texto), 
IntegerField (campo numérico inteiro), DateTimeField (campo de data e hora), ForeignKey (relacionamento com outra tabela) e muitos outros. 
Esses campos determinam os tipos de dados que serão armazenados no banco de dados.

"""


from django.db import models # importando o módulo models do pacote django.db. O módulo models contém as classes que são usadas para definir modelos no Django.

class Ferramentas(models.Model): # definindo uma classe chamada Ferramentas que herda da classe Model. Isso significa que a classe Ferramentas será um modelo no Django, representando uma tabela no banco de dados.

    nome = models.CharField(max_length=50, unique=True, blank=True, null=True) #define um campo chamado nome no modelo Ferramentas. O campo é do tipo CharField, que é usado para armazenar texto. Ele possui alguns parâmetros adicionais, como max_length definido como 50 (indicando o tamanho máximo do campo), unique=True (indicando que cada valor deve ser único), blank=True (permitindo que o campo seja deixado em branco) e null=True (permitindo que o campo seja nulo no banco de dados).
    ativa = models.BooleanField(default=False) # Field, que é usado para armazenar texto. Ele possui alguns parâmetros adicionais, como max_length definido como 50 (indicando o tamanho máximo do campo), unique=True (indicando que cada valor deve ser único), blank=True (permitindo que o campo seja deixado em branco) e null=True (permitindo que o campo seja nulo no banco de dados).

    def __str__(self): # Esta é uma função especial chamada __str__, que é usada para retornar uma representação de string legível para o objeto quando ele precisa ser exibido. Nesse caso, estamos retornando o valor do campo nome.
        return self.nome

    class Meta: # Esta linha define uma classe interna chamada Meta, que é usada para fornecer metadados adicionais ao modelo.
        db_table = 'db_ferramentas_cadastradas' # O parâmetro db_table especifica o nome da tabela no banco de dados que será associada a esse modelo. Nesse caso, a tabela será chamada 'db_ferramentas_cadastradas'.
        verbose_name_plural = 'BD Ferramentas Cadastradas' # O parâmetro verbose_name_plural define o nome plural legível para humanos desse modelo. Aqui, ele está definido como 'BD Ferramentas Cadastradas'.
        verbose_name = 'BD Ferramentas Cadastradas'# O parâmetro verbose_name define o nome singular legível para humanos desse modelo. Nesse caso, também está definido como 'BD Ferramentas Cadastradas'.






"""
Um ponto de atenção para a classe Ferramentas que acabamos de criar é que só passamos duas colunas na tabela, a coluna nome e a coluna ativa! 
Não precisamos criar uma coluna para a criação das chaves primaria da tabela, 
pois lá na classe CoreConfig que fica dentro de apps.py configuramos o default_auto_field que vai ficar responsável por criar todos os Ids únicos dessa tabela.
"""




"""

Após definir a classe de modelo Ferramentas no arquivo models.py, você precisará executar uma migração.
As migrações são responsáveis por criar ou atualizar as tabelas no banco de dados. 
São arquivos que registram as alterações no esquema do banco de dados, 
como criação de tabelas, alteração de campos ou adição de relacionamentos. 
O Django fornece comandos para gerar e aplicar migrações, garantindo que o banco de dados esteja sincronizado com as definições do arquivo models.py.

"""


### RESUMO ###

"""
Em resumo, dentro do arquivo modelo models.py em uma app Django você vai definir as classes de modelo que representam as tabelas do banco de dados e especificar os campos e comportamentos dos dados. 
Para criação e atualização dessas tabelas no banco você precisa executar os comandos makemigrations e migrate e com o ORM Django você vai criar, acessar, atualizar e excluir registros no banco de dados de maneira conveniente e consistente.
"""