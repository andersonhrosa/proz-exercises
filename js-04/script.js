// Método Simples (Criando e adicionando elementos diretamente ao body)
const produto = document.createElement('div');
produto.classList.add('produto');

const nomeProduto = document.createElement('h2');
nomeProduto.textContent = 'Smartphone Top de Linha';
produto.appendChild(nomeProduto);

const descricao = document.createElement('p');
descricao.textContent = 'O melhor smartphone do mercado!';
produto.appendChild(descricao);

const preco = document.createElement('p');
preco.textContent = 'R$ 5.000,00';
produto.appendChild(preco);

document.body.appendChild(produto);



const sectionProdutos = document.createElement('section');
sectionProdutos.id = 'produtos';
document.body.appendChild(sectionProdutos);

const novoProduto = document.createElement('div');
novoProduto.classList.add('produto');


sectionProdutos.appendChild(novoProduto);