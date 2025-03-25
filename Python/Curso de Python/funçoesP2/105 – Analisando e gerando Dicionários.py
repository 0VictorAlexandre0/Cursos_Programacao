#Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)


def notas(*notas, sit = False):
    """
    Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas de alunos(incontáveis).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicio = dict()
    dicio['total'] = len(notas)
    dicio['maior'] = max(notas)
    dicio['menor'] = min(notas)
    dicio['média'] = sum(notas)/len(notas)

    if sit:
        if dicio['média'] > 7:
            dicio['situção'] = 'BOA'
        elif dicio['média'] >= 5:
            dicio['situção'] = 'RAZOÁVEL'
        else:
            dicio['situção'] = 'RUIM'
    return dicio


help(notas)
resp = notas(5.5, 2.5, 4, 5, 9, sit=True)
print(resp)
