# Django ORM
ORM, ou Object-Relational Mapper, é uma técnica de mapeamento que permite relacionar objetos com os dados que eles representam, sendo uma alternativa para evitar a escrita direta de código SQL e tornar o desenvolvimento mais produtivo. No caso do Django, ele cria uma "ponte" entre a Programação Orientada a Objetos (POO) e o paradigma relacional dos bancos de dados.

Para iniciar a utilização do ORM do Django, é necessário, primeiramente, criar um model no app que está sendo desenvolvido. Ao criar o app, o próprio Django disponibiliza um arquivo chamado models.py, que é onde o Django reconhece quais tabelas serão criadas durante o desenvolvimento da aplicação. Em conjunto com comandos como `python manage.py makemigrations`e `python manage.py migrate`, o ORM do Django realiza essa criação no banco de dados utilizado.

Ao realizar essa migração, você cria a primeira versão do seu banco de dados, armazenada no arquivo `0001_initial.py`, que contém a migração responsável por aplicar a estrutura dos models ao banco de dados. Esse processo é repetido sempre que um model é criado ou alterado. Para aplicar as mudanças no banco, é necessário executar o comando `python manage.py migrate`.

Esse procedimento de migração trás inúmeras vantagens para o projeto de forma geral, por exemplo:
- `Controle de versão do banco de dados`
- `Automatização das mudanças`
- `Sincronização entre ambientes`
- `Integração com CI/CD`
- `Segurança na evolução do banco`
- `Testabilidade e previsibilidade`
- `Rollback de alterações (reversibilidade)`

**_migrate_ x _makemigrations_**
- `makemigrations`: gera os arquivos de migrações
- `migrate`: aplica os arquivos de migrações

**models**

Os models são o primeiro passo para que o Django realize o ORM entre o código e o banco de dados. É onde se utiliza POO para criar entidades e atributos no banco. Importando do módulo `django.db`, é possível utilizar outro módulo chamado `models`, o qual possui diversas classes responsáveis por definir e tipar atributos dentro do banco de dados, como no exemplo a seguir:
```python
from django.db import models


class Filho(models.Model):
    nome = models.CharField(max_length=64)
    idade = models.PositiveIntegerField()
    pai = modes.ForeignKey(
        Pai,
        on_delete=models.SET_NULL,
        null=True
    )
    ...

```
Nesse exemplo, a classe `Filho` herda de `Model` seus atributos e métodos, tornando-se uma entidade no banco de dados (somente após a migração). No módulo `models`, é possível utilizar outras classes que são responsáveis por definir o tipo de dado que os atributos receberão. Além disso, esses campos também aceitam parâmetros para configurar regras e padrões que os dados devem seguir.

Também é possível definir relações entre tabelas utilizando classes específicas que são responsáveis por se comunicar com outras entidades.

- **Campos Comuns (`Field Types`)**

| Campo                  | Descrição                                                                |
| ---------------------- | ------------------------------------------------------------------------ |
| `CharField`            | Campo de texto com limite de caracteres. Requer `max_length`.            |
| `TextField`            | Campo de texto sem limite definido. Ideal para descrições longas.        |
| `IntegerField`         | Armazena números inteiros positivos ou negativos.                        |
| `PositiveIntegerField` | Armazena somente inteiros positivos (>= 0).                              |
| `BooleanField`         | Armazena `True` ou `False`.                                              |
| `DateField`            | Armazena apenas datas (sem horário).                                     |
| `DateTimeField`        | Armazena data e hora.                                                    |
| `TimeField`            | Armazena apenas o horário.                                               |
| `EmailField`           | Campo de texto que valida se é um e-mail válido.                         |
| `URLField`             | Campo para URLs válidas.                                                 |
| `DecimalField`         | Armazena números decimais fixos. Requer `max_digits` e `decimal_places`. |
| `FloatField`           | Armazena números de ponto flutuante. Menos preciso que `DecimalField`.   |
| `SlugField`            | Armazena slugs (texto para URLs amigáveis).                              |
| `FileField`            | Armazena arquivos. Requer configuração de mídia.                         |
| `ImageField`           | Armazena imagens. Exige biblioteca Pillow instalada.                     |

- **Campos de Relacionamento**

| Campo             | Descrição                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------ |
| `ForeignKey`      | Cria um relacionamento muitos-para-um com outra tabela. Requer argumento `on_delete`.      |
| `OneToOneField`   | Relacionamento um-para-um. Uma instância está ligada diretamente a outra.                  |
| `ManyToManyField` | Relacionamento muitos-para-muitos. O Django cria uma tabela intermediária automaticamente. |


- **Parâmetros Comuns dos Campos**

| Parâmetro      | Aplicação                      | Descrição                                                                                                   |
| -------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `max_length`   | `CharField`, `SlugField`, etc. | Define o número máximo de caracteres. Obrigatório em alguns campos.                                         |
| `null`         | Todos                          | Permite que o campo aceite `NULL` no banco de dados.                                                        |
| `blank`        | Todos                          | Permite que o campo seja deixado em branco nos formulários (nível de validação).                            |
| `default`      | Todos                          | Define um valor padrão caso não seja informado.                                                             |
| `choices`      | Campos de texto/inteiros       | Define um conjunto fixo de valores possíveis.                                                               |
| `unique`       | Todos                          | Garante que o valor seja único no banco de dados.                                                           |
| `primary_key`  | Todos                          | Define o campo como chave primária da tabela.                                                               |
| `verbose_name` | Todos                          | Nome legível do campo para uso em formulários/admin.                                                        |
| `help_text`    | Todos                          | Texto auxiliar exibido em formulários/admin.                                                                |
| `on_delete`    | `ForeignKey`, `OneToOneField`  | Define o comportamento quando o objeto relacionado é deletado (ex: `CASCADE`, `SET_NULL`, `PROTECT`, etc.). |

**OBS**: Lembrando que existe muitos outros Fields e Parâmetros que podem ser utilizados, e é essencial consultar a documentação oficial do Django para analisar qual vai ser a melhor opção dentro do projeto.

**Manager**

O manager é criado a partir do momento que a classe criada herda de `models.Model`. Ao chamar o model criado é possível utilizar `Filho.objects` que é a materialização do `manager` no Django, o mesmo é responsável por fazer operações e consultas SQL utilizando o ORM do Django, dessa forma, vai ser possível utilizar um `SELECT`, por exemplo, chamando o método `Filho.object.get(alguma_coisa)`. Ao realizar esse procedimento irá retornar uma `QuerySet`, uma vez que a `Query` foi realizada.

`QuerySet` nada mais é que uma coleção de dados, sendo o resultado de uma `Query` realizada no banco de dados.

## Projeto
- Aqui é possível visualizar como os templates estão sendo utilizados nesse projeto: 
    - [👉 clique aqui](https://github.com/ThomasNicholas21/ProjetoReceitas/tree/main/base_templates)
    - [👉 clique aqui](https://github.com/ThomasNicholas21/ProjetoReceitas/tree/main/recipes/templates/recipes)

## Obs
Esse projeto está sendo feito para praticar habilidades técnicas e para aprimorar a resolução de problemas. A documentação utilizada para esse estudo foi:
- [Django Documentation 📚](https://docs.djangoproject.com/pt-br/3.2/topics/templates/)
- [Django Documentation 📚](https://docs.djangoproject.com/pt-br/3.2/ref/templates/language/)
- [Django Documentation 📚](https://docs.djangoproject.com/pt-br/3.2/ref/templates/builtins/#ref-templates-builtins-tags)

