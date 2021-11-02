"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

"""
def linear_merge(list1:list, list2:list) -> list:
    # +++ SUA SOLUÇÃO +++
    lst, i, j = [], 0, 0
    while(i<=len(list1)-1 and j<=len(list2)-1):
        if list1[i]<list2[j]:
            lst.append(list1[i])
            i+=1
        else:
            lst.append(list2[j])
            j+=1
    if i>len(list1)-1:
        while(j<=len(list2)-1):
            lst.append(list2[j])
            j+=1
    else:
        while(i<=len(list1)-1):
            lst.append(list1[i])
            i+=1
    return lst
"""

from heapq import merge

def linear_merge(list1:list, list2:list) -> list:
    # +++ SUA SOLUÇÃO +++
    return list(merge(list1, list2))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
