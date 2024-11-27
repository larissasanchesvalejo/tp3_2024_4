# 1) O que é um dicionário em Python e qual a sua principal utilização?
"""
Um dicionário em Python é uma estrutura de dados que armazena pares de chave-valor. Ele é usado para associar valores a chaves únicas, permitindo acesso rápido e eficiente aos dados.
"""

# 2) Como você pode adicionar um novo par chave-valor a um dicionário existente? Dê um exemplo de código.
"""
Para adicionar um novo par chave-valor a um dicionário, basta usar a sintaxe de atribuição com uma nova chave.

Exemplo:
aluno = {"nome": "João", "idade": 20}
aluno["curso"] = "Engenharia de Software"
"""

# 3) Como você pode remover um item de um dicionário? Explique a diferença entre o método del e o método pop().
"""
O método del remove um par chave-valor do dicionário sem retornar o valor associado. Já o método pop() também remove o item, mas retorna o valor associado à chave removida.

Exemplo com del:
aluno = {"nome": "João", "idade": 20, "curso": "Engenharia"}
del aluno["curso"]

Exemplo com pop():
aluno = {"nome": "João", "idade": 20, "curso": "Engenharia"}
curso_removido = aluno.pop("curso")
"""

# 4) Quais são algumas das principais operações que você pode realizar com dicionários, como acesso a valores, verificação de chaves, etc.?
"""
- Acessar um valor: aluno["nome"]
- Verificar se uma chave existe: "nome" in aluno
- Obter todas as chaves: aluno.keys()
- Obter todos os valores: aluno.values()
- Iterar sobre pares chave-valor:
  for chave, valor in aluno.items():
      print(chave, valor)
- Atualizar o dicionário: aluno.update({"curso": "Engenharia"})
"""
