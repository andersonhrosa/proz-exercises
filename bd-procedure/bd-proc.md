# A empresa precisa de um relatório diário de produtos vendidos. Um procedure é a solução ideal.

## Criando o Procedure:

```SQL

DELIMITER $$
CREATE PROCEDURE sp_relatorio_vendas_diarias()
BEGIN
    SELECT data_venda, id_produto, SUM(quantidade) AS total_vendido
    FROM vendas
    GROUP BY data_venda, id_produto;
END $$
DELIMITER ;
```

## Explicação:
O código agrupa as vendas por data e produto, calculando o total vendido por dia para cada produto.

# Executando:
```SQL
CALL sp_relatorio_vendas_diarias();
```
# Personalizando:
Adicione filtros (WHERE), cálculos (SUM, AVG) e ordene os resultados conforme necessário.

Exemplo com filtro por mês e cálculo da receita:

```SQL

CREATE PROCEDURE sp_relatorio_vendas_mensal(IN p_mes INT)
BEGIN
    SELECT YEAR(data_venda), MONTH(data_venda), id_produto, SUM(quantidade), SUM(quantidade*preco)
    FROM vendas
    WHERE MONTH(data_venda) = p_mes
    GROUP BY YEAR(data_venda), MONTH(data_venda), id_produto;
END $$
```

# Considerações:

Crie índices para melhorar a performance.
Utilize ferramentas de agendamento para automatizar a geração de relatórios.
Exporte os resultados para visualização em ferramentas de BI.
Com este procedure, a empresa terá um relatório diário de vendas de forma rápida e eficiente.