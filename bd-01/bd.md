Criando um Banco de Dados e uma Tabela em SQL
Markdown:

```SQL
-- Criando o banco de dados ESCOLA
CREATE DATABASE ESCOLA;

-- Usando o banco de dados recém-criado
USE ESCOLA;

-- Criando a tabela ALUNO
CREATE TABLE ALUNO (
    ID INT PRIMARY KEY,
    NOME VARCHAR(100),
    EMAIL VARCHAR(100),
    ENDERECO VARCHAR(200)
);
```

Use o código com cuidado.

Explicação:

`CREATE DATABASE ESCOLA;`: Cria um novo banco de dados com o nome "ESCOLA".
`USE ESCOLA;`: Seleciona o banco de dados "ESCOLA" como o banco de dados ativo para as próximas operações.
`CREATE TABLE ALUNO` (...): Cria uma nova tabela chamada "ALUNO" dentro do banco de dados "ESCOLA".

`ID INT PRIMARY KEY`: Define um atributo chamado "ID" do tipo inteiro como a chave primária da tabela. A chave primária identifica de forma única cada registro na tabela.

`NOME VARCHAR(100)`: Cria um atributo chamado "NOME" do tipo caractere (varchar) com um tamanho máximo de 100 caracteres.

`EMAIL VARCHAR(100)`: Cria um atributo chamado "EMAIL" do tipo caractere (varchar) com um tamanho máximo de 100 caracteres.

`ENDERECO VARCHAR(200)`: Cria um atributo chamado "ENDERECO" do tipo caractere (varchar) com um tamanho máximo de 200 caracteres.

Observações:

Tamanho dos atributos: Os tamanhos dos atributos (100 e 200 caracteres) são apenas exemplos. Você pode ajustá-los de acordo com a quantidade de dados que espera armazenar.
Tipos de dados: Além de INT e VARCHAR, existem outros tipos de dados disponíveis no SQL, como DATE, DATETIME, DECIMAL, etc. A escolha do tipo de dado depende do tipo de informação que você deseja armazenar.
Chave primária: A chave primária é fundamental para garantir a integridade dos dados e evitar duplicações.
Consistência: É importante garantir que os nomes dos atributos e das tabelas sejam claros e consistentes para facilitar a compreensão e a manutenção do banco de dados.
Inserindo dados na tabela:

Para inserir dados na tabela "ALUNO", você pode usar a instrução INSERT INTO. Por exemplo:

```SQL
INSERT INTO ALUNO (ID, NOME, EMAIL, ENDERECO)
VALUES (1, 'João da Silva', 'joao@email.com', 'Rua dos Bobos, nº 0');
Use o código com cuidado.
```

Personalizando a tabela:

Você pode adicionar mais atributos à tabela "ALUNO" para armazenar outras informações sobre os alunos, como data de nascimento, telefone, etc. Por exemplo:

```SQL
ALTER TABLE ALUNO
ADD DATA_NASCIMENTO DATE;
Use o código com cuidado.
```

Lembre-se que a sintaxe exata pode variar ligeiramente dependendo do sistema gerenciador de banco de dados que você está utilizando (SQL Server, MySQL, PostgreSQL, etc.). Consulte a documentação do seu SGBD para obter mais informações.