from django.http import HttpResponse

def hello(request):
    return HttpResponse('Olá mundo!')

def article(request, year):
    soma10 = year + 10
    return HttpResponse(f'O ano enviado mais 10 é: {soma10}')

def ler_banco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20 },
        {'nome': 'Pedro', 'idade': 25 },
        {'nome': 'Joaquim', 'idade': 27}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'Pessoa não encontrada', 'idade': 0}

def fname(request, nome):
    result = ler_banco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse('Pessoa não encontrada')