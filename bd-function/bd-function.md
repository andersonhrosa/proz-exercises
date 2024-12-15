Para somar todos os clientes que foram cadastrados em um dia específico, pode-se criar uma função em SQL. Aqui está um exemplo:

```sql
CREATE FUNCTION contar_clientes_dia(data DATE)
RETURNS INT
BEGIN
    DECLARE total_clientes INT;
    SELECT COUNT(*) INTO total_clientes
    FROM clientes
    WHERE DATE(data_cadastro) = data;
    RETURN total_clientes;
END;
```
Esse código cria uma função chamada `contar_clientes_dia` que recebe uma data como parâmetro. A função conta o número de clientes cadastrados na tabela clientes com base na data de cadastro e retorna esse número.

Para usar a função, você pode chamá-la assim:

```sql
SELECT contar_clientes_dia('2024-12-15');
```

Isso retornará o número de clientes cadastrados no dia 15 de dezembro de 2024