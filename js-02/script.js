// Capturando os elementos pelo ID
const titulo = document.getElementById('titulo');
const listaNaoOrdenada = document.querySelector('ul');
const link = document.querySelector('a');
const listaOrdenada = document.getElementById('lista-ordenada');

// Adicionando conteúdo aos elementos
titulo.innerText = 'Este é o título da página';
link.innerText = 'Acesse a Prozeducacao';

// Adicionando itens à lista não ordenada
const itensNaoOrdenados = ['Item 1', 'Item 2', 'Item 3'];
listaNaoOrdenada.innerHTML = itensNaoOrdenados.map(item => `<li>${item}</li>`).join('');

// Adicionando itens com links à lista ordenada
const itensOrdenados = [
    { texto: 'Google', link: 'https://www.google.com' },
    { texto: 'MDN Web Docs', link: 'https://developer.mozilla.org' },
    { texto: 'W3Schools', link: 'https://www.w3schools.com' }
];
const itensHTML = itensOrdenados.map(item => `<li><a href="${item.link}">${item.texto}</a></li>`).join('');
listaOrdenada.innerHTML = itensHTML;