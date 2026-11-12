---
name: discovery-benchmark
description: Planeja e executa rodadas de benchmark de concorrentes dentro de um discovery de produto (Etapa 1), só com fontes públicas, com quadro comparativo por eixo, qualidade da evidência, registro de execução, autocrítica e verificação. Use sempre que o usuário pedir benchmark, análise de concorrentes, comparação de ferramentas ou fornecedores, "abra a rodada N", concorrentes por função, editais públicos como referência, ou monitoramento de concorrentes, mesmo que não diga "benchmark".
---

# Benchmark de concorrentes (Etapa 1)

O benchmark mostra o que o mercado oferece **publicamente**, onde há lacunas e o que isso diz sobre as hipóteses. Ele não prova demanda nem disposição a pagar: isso vem das entrevistas e dos dados.

## Regras

- **Só fontes públicas**, sem login e sem contato com concorrentes. Demonstrações e "comprador oculto" só com aprovação explícita do responsável (algumas empresas proíbem).
- **"Não encontrado publicamente" (n.e.) não significa "não existe".** Escreva sempre n.e., nunca "não tem".
- **Autodeclarado é fato sobre a declaração**, não sobre o produto: "[F] o site declara ISO 27001".
- **Agregadores e diretórios de avaliação** contam como evidência fraca; notas de uma suíte inteira não valem para um módulo.
- Trabalhe em **rodadas**. Cada rodada é um documento novo na pasta Benchmark: `NN-benchmark` (rodada 1), `benchmark-rodada-2`, `benchmark-rodada-3`...

## Ciclo de cada rodada

### 1. Plano (ponto de aprovação A)

Crie `benchmark-rodada-N-plano` com:
- **Objetivo:** que hipóteses e requisitos a rodada alimenta.
- **Alvos:** concorrentes diretos, concorrentes por função (quem faz bem uma parte do problema) e referências que não são concorrentes (servem de vocabulário, não entram no quadro).
- **Perguntas fechadas** (Q1, Q2...), cada uma respondida por alvo com Sim / Não / Não encontrado publicamente, sempre com fonte e data, e a coluna "alimenta" (H# ou R#).
- **Fontes permitidas e proibidas.**
- **Critério de parada e limite:** ex. no máximo 8 buscas ou páginas por alvo; a rodada termina quando toda pergunta de todo alvo tem resposta ou n.e.
- **Entrega:** nome do documento final e o que será atualizado depois.

Na rodada 1 o plano pode ser curto e embutido no próprio pedido, se o responsável preferir. Em rodadas seguintes, espere a aprovação antes de executar.

### 2. Execução

Pesquise sites oficiais, páginas de produto, central de ajuda, documentação de API, páginas de segurança e confiança, notas de versão, preços, notícias, diretórios e agregadores de avaliação, e contratações públicas (editais, atas), quando existirem. Busque várias fontes em paralelo.

### 3. Documento da rodada

Use `assets/modelo-benchmark-rodada.md`. Ordem obrigatória:
1. **Qualidade da evidência (leia primeiro):** de onde veio quase tudo, o que não foi lido, onde a evidência é rasa.
2. **Visão comparativa:** tabela eixo x concorrente. Eixos típicos: origem, público e porte, como vende (separado ou dentro de plataforma), funções-chave do domínio, IA (com casos concretos ou só marketing), API e integrações, preço, implantação e UX segundo avaliações, prova social, setor público.
3. **Resumo por concorrente:** um parágrafo com [F] e [I] separados.
4. **Padrões que aparecem** (todos [I]): ex. ninguém publica preço; implantação lenta é fraqueza recorrente; lacuna que ninguém cobre; diferencial possível.
5. **O que isso diz sobre as hipóteses:** tabela hipótese, sinal, força. Diga quando a hipótese "não é testável por benchmark".
6. **Lacunas e próximos passos sugeridos.**
7. **Fontes** com endereço e data de acesso.
8. **Registro de execução** (data e pergunta, fonte, resultado, não encontrado ou bloqueado, confiança).
9. **Autocrítica:** o que ficou raso, o que se contradiz, o que falta.
10. **Verificação:** "x de 10 itens atendidos; exceções: ...".

### 4. Depois da entrega

- Atualize o andamento (situação da Etapa 1, achados do benchmark, hipóteses afetadas sem elevar força além da evidência).
- Atualize o mapa de requisitos: coluna "Cobertura no mercado" e itens X (só vistos no benchmark).
- Registre pendências (ex.: aprovar a rodada, decidir inclusão de concorrente).
- Envie o link e diga que está em rascunho.

## Variações

- **Concorrentes por função:** quando o produto cobre várias funções, faça uma rodada mapeando quem é forte em cada função, mesmo que não seja concorrente da plataforma toda.
- **Editais públicos e RFPs:** use como referência de exigências do comprador. Registre órgão, objeto, data, link e os requisitos exigidos.
- **Rodada temática:** ex. IA agêntica, integrações, preços. Mesma estrutura, perguntas fechadas próprias.
- **Monitoramento recorrente:** só como tarefa agendada aprovada pelo responsável (dia e hora definidos). Gera `monitoramento-AAAA-MM-DD` com o que mudou; propõe, não decide.
