from reportlab.pdfgen import canvas

#1- criar novo arquivo pdf
pdf = canvas.Canvas('exemplo.pdf')


#2- definir um titulo
pdf.setTitle('Relatório de Atividades')


#3- inserindo texto
pdf.drawString(100, 750, 'Relatório de Atividades - 2025')


#4- Inserindo subtitulo
pdf.setFont('Helvetica-Bold', 14)
pdf.drawString(100, 720, 'Atividades Realizadas')


#5- Criar lista
atividades = [
    '- Reunião com equipe de projetos',
    '- Desenvolvimento de novos módulos',
    '- Testes de funcionalidade',
    '- Treinamento para novos colaboradores'
]

#6- escrever no pdf
y = 700     #posicao inicial na vertical
for item in atividades:
    pdf.setFont('Helvetica', 12)
    pdf.drawString(120, y, item)
    y -= 20     #mover para baixo o textoa ser inserido


#7- salvar pdf
pdf.save()
print('Arquivo criado!')

