function parImpar(n) {
    if (n % 2 == 0) {
        return 'par'
    } else {
        return 'impar'
    }
}
//console.log(parImpar(5))


function soma(n1 = 0, n2 = 0) { //se algum dos parametros nn for passado, equivale a 0
    return n1 + n2
}
//console.log(soma(2, 5))


let v = function(x) {
    return x*2
}
//console.log(v(3))


function fatorial(n) {
    let fat = 1
    for (let cont = n; cont > 1; cont--) {
        fat *= cont
    }
    return fat
}
//console.log(fatorial(5))