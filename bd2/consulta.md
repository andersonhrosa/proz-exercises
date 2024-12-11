## Criando um Banco de Dados e Relacionando Tabelas com Chaves Estrangeiras
1. Escolhendo o Sistema Gerenciador de Banco de Dados (SGBD)
Para este exemplo, utilizaremos o MySQL. Você pode usar outros SGBDs como PostgreSQL, SQL Server, etc., mas a sintaxe dos comandos pode variar ligeiramente.

2. Criando o Banco de Dados
```SQL
CREATE DATABASE biblioteca;
```
Com este comando, criamos um banco de dados chamado "biblioteca".

3. Conectando-se ao Banco de Dados
```SQL
USE biblioteca;

```
Este comando indica ao MySQL que vamos trabalhar com o banco de dados "biblioteca".

4. Criando as Tabelas
Vamos criar duas tabelas: autores e livros.

```SQL
CREATE TABLE autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    nacionalidade VARCHAR(50)
);

CREATE TABLE livros (
    id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(200),
    ano_publicacao INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);
```

`autores`: Possui um identificador único (id_autor), nome e nacionalidade do autor.
`livros`: Possui um identificador único (id_livro), título, ano de publicação e um campo id_autor que faz referência à tabela autores (chave estrangeira).
5. Inserindo Dados
```SQL
INSERT INTO autores (nome, nacionalidade)
VALUES ('Stephen King', 'Estados Unidos'),
       ('J.K. Rowling', 'Reino Unido'),
       ('Gabriel Garcia Marquez', 'Colômbia');

INSERT INTO livros (titulo, ano_publicacao, id_autor)
VALUES ('It', 1986, 1),
       ('Harry Potter e a Pedra Filosofal', 1997, 2),
       ('Cem Anos de Solidão', 1967, 3);
```

6. Realizando Consultas com Joins
Para obter informações sobre os livros e seus respectivos autores, podemos usar o comando JOIN:

```SQL
SELECT livros.titulo, autores.nome
FROM livros
INNER JOIN autores ON livros.id_autor = autores.id_autor;
```

Este comando irá retornar uma tabela com o título de cada livro e o nome do seu autor.

### Outras opções de JOIN:

`LEFT JOIN`: Retorna todas as linhas da tabela da esquerda e as correspondentes da tabela da direita.
`RIGHT JOIN`: Retorna todas as linhas da tabela da direita e as correspondentes da tabela da esquerda.
`FULL OUTER JOIN`: Retorna todas as linhas de ambas as tabelas, mesmo que não haja correspondência.
Exemplo Completo:
```SQL
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    nacionalidade VARCHAR(50)
);

CREATE TABLE livros (
    id_livro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(200),
    ano_publicacao INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);

INSERT INTO autores (nome, nacionalidade)
VALUES ('Stephen King', 'Estados Unidos'),
       ('J.K. Rowling', 'Reino Unido'),
       ('Gabriel Garcia Marquez', 'Colômbia');

INSERT INTO livros (titulo, ano_publicacao, id_autor)
VALUES ('It', 1986, 1),
       ('Harry Potter e a Pedra Filosofal', 1997, 2),
       ('Cem Anos de Solidão', 1967, 3);

SELECT livros.titulo, autores.nome
FROM livros
INNER JOIN autores ON livros.id_autor = autores.id_autor;
```

