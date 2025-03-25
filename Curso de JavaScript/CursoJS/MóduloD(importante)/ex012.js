var hoje = new Date()
var hora = hoje.getHours()
var min = hoje.getMinutes()
var dia = hoje.getDate()

console.log(`Agora são ${hora} horas e ${min} minutos, do dia ${dia}`)
if (hora < 12) {
    console.log('Bom dia!')
} else if (hora <= 18) {
    console.log('Boa tarde!')
} else {
    confirm.log('Boa noite!')
}