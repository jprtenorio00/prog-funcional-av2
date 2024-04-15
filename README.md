# AV2 de Programação Funcional - Lista de Exercícios

Este repositório contém a lista de exercícios valendo a nota da AV2 de Programação Funcional. Os exercícios são desenhados para praticar os conceitos e as técnicas da programação funcional, enfatizando a importância de evitar efeitos colaterais e promovendo um código mais puro e fácil de entender.

## Regras Gerais

- **Colaboração**: É proibido copiar resolução de algum colega. É permitido ajudar na resolução das questões, contanto que as soluções finais sejam diferentes.
- **Penalização por similaridade**: Similaridade entre soluções de diferentes alunos resultará em perda da nota da questão.
- **Uso de `for` e `if`**: As palavras reservadas `for` e `if` só podem ser utilizadas dentro de List Comprehensions ou Expressões Lambda. O uso fora destes escopos acarretará penalização de 50% na nota da questão.
- **Declaração de funções**: O uso da palavra reservada `def` para declarar funções deve seguir regras específicas:
  - Todas as variáveis dentro do escopo da função devem ser definidas utilizando Expressões Lambda.
  - Estruturas de dados como listas ou dicionários só são permitidas como retorno das expressões lambda.

### Exemplo de código inadequado

```python
def old_customers(d):
    retl = []
    for k in d.keys():
        if d[k][0] >= 60:
            retl.append(k)
    return retl
```

### Exemplo de código corrigido

```python
def old_customers_2(d):
    retl = lambda: [k for k in d.keys() if d[k][0] >= 60]
    return retl()
```

## Exercícios

### 1. Implementação de Diagrama de Atividades
Desenvolva um programa em Python que implemente um diagrama de atividades fornecido. Algumas atividades podem ser implementadas como funções sinalizadoras que imprimem sua função no console.

### 2. Testes Unitários e Teste de Stress
Desenvolva três testes unitários para verificar diferentes fluxos do programa implementado na questão anterior e um teste de stress para avaliar a robustez do programa.

### 3. Interação com Banco de Dados
Implemente um programa em Python que gerencia as tabelas `USERS`, `VIDEOGAMES`, `GAMES`, e `COMPANY`, e que seja capaz de realizar operações de inserção, remoção e consulta em um Banco de Dados MySQL.

### 4. Scaffold para Consultas SQL
Elabore um Scaffold que auxilie na escrita de consultas SQL, incluindo a geração de códigos para `INNER JOIN` e `SELECT` para as tabelas mencionadas na questão anterior.

### 5. Requisitos Não-funcionais
Adapte um dos programas anteriores para que satisfaça requisitos não-funcionais como disponibilidade e segurança, incluindo armazenamento de senhas criptografadas e autenticação de usuários.

## Contribuição

Este projeto é um trabalho acadêmico e a colaboração é limitada às discussões sobre abordagens de problemas e revisões de código, mantendo a integridade acadêmica e a originalidade do trabalho individual.

## Autor
João Pedro Rodrigues Tenório