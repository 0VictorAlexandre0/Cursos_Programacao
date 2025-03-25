let num = [1, 4, 7, 9]

console.log(`Nosso vetor é composto por: ${num}`)

num[4] = 11 //na posiçao 4, acrescente o numero 11
console.log(num)

//nn sei q posiçao ta, como adiciono?
num.push(15) //use o push
console.log(num)

//qual comprimento do array?
//use o: num.length
console.log(`O array tem ${num.length} posições por enquanto`) // q por enquanto é 6

//quero ordenar meu vetor por crescente
//use o num.sort()
console.log(num.sort()) //esta meio errado por conta que o JS é burro e como o 1 ta na frente de 11 e 15 acha q vem antes


// inicio, fim, acrescimo ou decremento
/*
Criei a variavel POSICAO valendo 0, e enquanto essa posição for menor que o TAMANDO DA LISTA ele irá ACRESCENTAR +1 até o fim dela
*/
for (var posicao = 0; posicao < num.length; posicao++){ 
    console.log(`A posição ${posicao} tem o valor ${num[posicao]}`)
}

//agora com FOR IN
/*
Para cada posição em num
*/
console.log('Feito com FOR IN:')
for (var posicao in num) {
    console.log(`A posição ${posicao} tem o valor ${num[posicao]}`)
}

//buscar valores num vetor:
//num.indexOf()
console.log(num.indexOf(4)) //existe o valor 4? SIM, retorna o index de onde está
console.log(num.indexOf(22)) //existe o valor 22? NÃO, retorna valor -1
// ou
let posicao = num.indexOf(22)
if (posicao == -1) {
    console.log('Valor não encontrado.')
} else {
    console.log(`O valor está na posição ${posicao}`)
}

