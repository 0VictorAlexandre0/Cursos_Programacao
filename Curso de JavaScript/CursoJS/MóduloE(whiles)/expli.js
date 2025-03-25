function linha() {
    console.log('-'.repeat(30))
}


//while:
var c = 0
while (c <= 10) {
    console.log(`Passo ${c}`)
    c++ //igual c+=1
}

linha()


//do while:
var c = 1
do {
    console.log(`Passo com DO ${c}`)
    c++
} while (c <= 10)

linha()


//for:
for (var c = 1; c <= 10; c++) {
    console.log(`Passo com FOR ${c}`)
}
