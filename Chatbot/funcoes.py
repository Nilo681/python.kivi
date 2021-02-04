def resposta():
    # capturando a resposta
    resp = input(':')
    resp = resp.lower()
    resp = resp.replace('é','eh')
    return resp
 
def pegaNome(nome):
    if 'o meu nome eh' in nome:
        nome = nome [14:]

    nome = nome.title()
    return nome

def respondeNome(nome):
    conhecidos = ['dan','fran','siba']

    if nome in conhecidos:
        frase = 'Olá novamente:'
    else:
        frase = 'Muito Prazer: '

    return frase+nome