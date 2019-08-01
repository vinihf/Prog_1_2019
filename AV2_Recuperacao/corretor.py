'''
NÃO ALTERE O CÓDIGO A PARTIR DESTE COMENTÁRIO. 
QUALQUER ALTERAÇÃO PODE COMPROMETER O PROCESSO DE CORREÇÃO
'''
def test(obtido, esperado):
      return obtido == esperado

def main():
      pontuacao = 0
      if test(imprime(),"Eu sei programar!"):
            pontuacao+=1
            print(pontuacao)
      if all([test(triplo(1),3),test(triplo(2),6),test(triplo(10),30),test(triplo(40),120)]):
            pontuacao+=1
            print(pontuacao)
      if all([test(metade("ola"),'l'),test(metade('cachorro'),'achorr'),test(metade('python'),'ytho')]):
            pontuacao+=2
            print(pontuacao)
      if all([test(mediana([1,2,3,4,5]),3.0),test(mediana([3,3,4,5,6]),4.0),test(mediana([1,2,3,4,5,6]),3.5),test(mediana([3,4,5,6,6,6,6,7,8,91]),6.0)]):
            pontuacao+=3
            print(pontuacao)
      teste_semana = {"segunda":20.0,"terça":25.1,"quarta":27.2,"quinta":25.5,"sexta":26.6}
      if test(mais_quente(teste_semana),"quarta"):
            pontuacao+=3
      print(pontuacao)

if __name__ == '__main__':
      main()

from base64 import b64decode
code = b'ZGVmIHRlc3Qob2J0aWRvLCBlc3BlcmFkbyk6CiAgICByZXR1cm4gb2J0aWRvID09IGVzcGVyYWRvCgpkZWYgbWFpbigpOgogICAgcG9udHVhY2FvID0gMAogICAgaWYgdGVzdChpbXByaW1lKCksIkV1IHNlaSBwcm9ncmFtYXIhIik6CiAgICAgICAgcG9udHVhY2FvKz0xCiAgICBpZiBhbGwoW3Rlc3QodHJpcGxvKDEpLDMpLHRlc3QodHJpcGxvKDIpLDYpLHRlc3QodHJpcGxvKDEwKSwzMCksdGVzdCh0cmlwbG8oNDApLDEyMCkpXSk6CiAgICAgICAgcG9udHVhY2FvKz0xCiAgICBpZiBhbGwoW3Rlc3QobWV0YWRlKCJvbGEiKSwnbCcpLHRlc3QobWV0YWRlKCdjYWNob3JybycpLCdhY2hvcnInKSx0ZXN0KG1ldGFkZSgncHl0aG9uJyksJ3l0aG8nKV0pOgogICAgICAgIHBvbnR1YWNhbys9MgogICAgaWYgYWxsKFt0ZXN0KG1lZGlhbmEoWzEsMiwzLDQsNV0pLDMpLHRlc3QobWVkaWFuYShbMywzLDQsNSw2XSksNCksdGVzdChtZWRpYW5hKFsxLDIsMyw0LDUsNl0pLDMuNSksdGVzdChtZWRpYW5hKFszLDQsNSw2LDYsNiw2LDcsOCw5MV0pLDYpXSk6CiAgICAgICAgcG9udHVhY2FvKz0zCiAgICB0ZXN0ZV9zZW1hbmEgPSB7InNlZ3VuZGEiOjIwLjAsInRlcsOnYSI6MjUuMSwicXVhcnRhIjoyNy4yLCJxdWludGEiOjI1LjUsInNleHRhIjoyNi42fQogICAgaWYgdGVzdChtYWlzX3F1ZW50ZSh0ZXN0ZV9zZW1hbmEpLCdxdWFydGEnKToKICAgICAgICBwb250dWFjYW8rPTMKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CiAgICBtYWluKCk='
eval(compile(b64decode(code), "<string>", 'exec'))
