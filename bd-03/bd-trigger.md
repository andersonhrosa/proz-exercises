# Exemplo Prático: Um Banco de Dados de Livraria

## Criação de um banco de dados simples para gerenciar uma livraria.

1. Criando o Banco de Dados

Criação do banco de dados. A sintaxe exata varia de acordo com o sistema gerenciador de banco de dados (SGBD) que você está utilizando. Por exemplo, no MySQL, você usaria:

```SQL
CREATE DATABASE livraria;
```

2. Criando as Tabelas

Tabelas para armazenar informações sobre livros, autores e empréstimos:

```SQL

USE livraria;

CREATE TABLE livros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100),
    autor_id INT,
    ano_publicacao INT,
    genero VARCHAR(50)
);

CREATE TABLE autores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    nacionalidade VARCHAR(50)
);

CREATE TABLE emprestimos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    livro_id INT,
    cliente_id INT,
    data_emprestimo DATE,
    data_devolucao DATE
);
```

3. Criando um Trigger

Vamos criar um trigger que seja acionado quando um livro for emprestado. Esse trigger irá atualizar o campo data_emprestimo na tabela emprestimos com a data atual.

```SQL

CREATE TRIGGER atualizar_data_emprestimo
BEFORE INSERT ON emprestimos
FOR EACH ROW
SET NEW.data_emprestimo = CURDATE();
```

Explicando o Trigger:

`BEFORE INSERT`: O trigger será executado antes de cada inserção na tabela emprestimos.
`FOR EACH ROW`: O trigger será executado para cada linha que está sendo inserida.
`SET NEW.data_emprestimo = CURDATE();`: A coluna data_emprestimo da nova linha será preenchida com a data atual.