def test(obtido, esperado):
    return obtido == esperado

def main():
    pontuacao = 0
    if (test(hello(),"Hello, Python!")):
        pontuacao+=1
    turmaTeste1 = {'Vinicius':9.8,"José":5,"Vitor":9,"Kelvin":3,"Mariana":8,"Arthur":5.5,"João":7.4}
    turmaTeste2 = {'Vinicius':9.6,"José":5,"Vitor":9,"Kelvin":3,"Mariana":8,"Arthur":5.5,"João":7.4,"Tiago":9.9}
    if all([test(maximoTurma(turmaTeste1),9.8),test(maximoTurma(turmaTeste2),9.9)]):
        pontuacao += 2
    if all([test(loja_tinta(50), 1),test(loja_tinta(54), 1),test(loja_tinta(55), 2),test(loja_tinta(108), 2),test(loja_tinta(109), 3),test(loja_tinta(162), 3)]):
        pontuacao += 2
    if all([test(conta2(['bola','ola','Bola','Aula','aula']),2),test(conta2(['aaaa','Aaaaa','elefante','Elefante','Rola','Dança','Azul','verde','azul']),3)]):
        pontuacao+=2
    if all([test(esquilos(70, False), True),test(esquilos(95, False), False),test(esquilos(95, True), True),test(esquilos(90, False), True),test(esquilos(90, True), True),test(esquilos(50, False), False),test(esquilos(50, True), False), test(esquilos(100, False), False),  test(esquilos(100, True), True),test(esquilos(105, True), False),test(esquilos(59, False), False),test(esquilos(59, True), False),test(esquilos(60, False), True)]):
        pontuacao+=2
    if all([test(somatorio([1,3,5,7,11]),0),test(somatorio([1,3,6,7,12,10,22]),50),test(somatorio([2,5,3,5,7,11]),2)]):
        pontuacao+=1
    print(pontuacao)

if __name__ == '__main__':
    main()


from base64 import b64decode
code = b'ZGVmIHRlc3Qob2J0aWRvLCBlc3BlcmFkbyk6CiAgICByZXR1cm4gb2J0aWRvID09IGVzcGVyYWRvCgpkZWYgbWFpbigpOgogICAgcG9udHVhY2FvID0gMAogICAgaWYgKHRlc3QoaGVsbG8oKSwiSGVsbG8sIFB5dGhvbiEiKSk6CiAgICAgICAgcG9udHVhY2FvKz0xCiAgICB0dXJtYVRlc3RlMSA9IHsnVmluaWNpdXMnOjkuOCwiSm9zw6kiOjUsIlZpdG9yIjo5LCJLZWx2aW4iOjMsIk1hcmlhbmEiOjgsIkFydGh1ciI6NS41LCJKb8OjbyI6Ny40fQogICAgdHVybWFUZXN0ZTIgPSB7J1ZpbmljaXVzJzo5LjYsIkpvc8OpIjo1LCJWaXRvciI6OSwiS2VsdmluIjozLCJNYXJpYW5hIjo4LCJBcnRodXIiOjUuNSwiSm/Do28iOjcuNCwiVGlhZ28iOjkuOX0KICAgIGlmIGFsbChbdGVzdChtYXhpbW9UdXJtYSh0dXJtYVRlc3RlMSksOS44KSx0ZXN0KG1heGltb1R1cm1hKHR1cm1hVGVzdGUyKSw5LjkpXSk6CiAgICAgICAgcG9udHVhY2FvICs9IDIKICAgIGlmIGFsbChbdGVzdChsb2phX3RpbnRhKDUwKSwgMSksdGVzdChsb2phX3RpbnRhKDU0KSwgMSksdGVzdChsb2phX3RpbnRhKDU1KSwgMiksdGVzdChsb2phX3RpbnRhKDEwOCksIDIpLHRlc3QobG9qYV90aW50YSgxMDkpLCAzKSx0ZXN0KGxvamFfdGludGEoMTYyKSwgMyldKToKICAgICAgICBwb250dWFjYW8gKz0gMgogICAgaWYgYWxsKFt0ZXN0KGNvbnRhMihbJ2JvbGEnLCdvbGEnLCdCb2xhJywnQXVsYScsJ2F1bGEnXSksMiksdGVzdChjb250YTIoWydhYWFhJywnQWFhYWEnLCdlbGVmYW50ZScsJ0VsZWZhbnRlJywnUm9sYScsJ0RhbsOnYScsJ0F6dWwnLCd2ZXJkZScsJ2F6dWwnXSksMyldKToKICAgICAgICBwb250dWFjYW8rPTIKICAgIGlmIGFsbChbdGVzdChlc3F1aWxvcyg3MCwgRmFsc2UpLCBUcnVlKSx0ZXN0KGVzcXVpbG9zKDk1LCBGYWxzZSksIEZhbHNlKSx0ZXN0KGVzcXVpbG9zKDk1LCBUcnVlKSwgVHJ1ZSksdGVzdChlc3F1aWxvcyg5MCwgRmFsc2UpLCBUcnVlKSx0ZXN0KGVzcXVpbG9zKDkwLCBUcnVlKSwgVHJ1ZSksdGVzdChlc3F1aWxvcyg1MCwgRmFsc2UpLCBGYWxzZSksdGVzdChlc3F1aWxvcyg1MCwgVHJ1ZSksIEZhbHNlKSwgdGVzdChlc3F1aWxvcygxMDAsIEZhbHNlKSwgRmFsc2UpLCAgdGVzdChlc3F1aWxvcygxMDAsIFRydWUpLCBUcnVlKSx0ZXN0KGVzcXVpbG9zKDEwNSwgVHJ1ZSksIEZhbHNlKSx0ZXN0KGVzcXVpbG9zKDU5LCBGYWxzZSksIEZhbHNlKSx0ZXN0KGVzcXVpbG9zKDU5LCBUcnVlKSwgRmFsc2UpLHRlc3QoZXNxdWlsb3MoNjAsIEZhbHNlKSwgVHJ1ZSldKToKICAgICAgICBwb250dWFjYW8rPTIKICAgIGlmIGFsbChbdGVzdChzb21hdG9yaW8oWzEsMyw1LDcsMTFdKSwwKSx0ZXN0KHNvbWF0b3JpbyhbMSwzLDYsNywxMiwxMCwyMl0pLDUwKSx0ZXN0KHNvbWF0b3JpbyhbMiw1LDMsNSw3LDExXSksMildKToKICAgICAgICBwb250dWFjYW8rPTEKICAgIHByaW50KHBvbnR1YWNhbykKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CiAgICBtYWluKCk='
eval(compile(b64decode(code), "<string>", 'exec'))
