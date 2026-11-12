---
name: discovery-decisao-relatorio
description: Mescla as evidências de um discovery de produto para a decisão (matriz ponderada das opções, critérios de passagem, análise de sensibilidade, estado final das hipóteses, classificação de requisitos) e redige o relatório do discovery com recomendação e sugestões, além de relatórios de acompanhamento para áreas específicas. Use sempre que o usuário pedir matriz de decisão, comparação final das opções, recomendação, conclusão do discovery, relatório final, resultado da pesquisa, resumo executivo, ou um relatório parcial para apresentar a uma área ou à diretoria.
---

# Mescla para decisão e relatório do discovery

Esta etapa junta tudo o que foi coletado e mostra o que a evidência sustenta. Ela **recomenda**; quem decide é o responsável. Uma recomendação honesta diz também o que a mudaria.

## Antes de começar

Confira no andamento e no registro de pendências:
- Quais etapas estão aprovadas e quais ainda em rascunho (declare isso no topo).
- Se critérios e pesos foram aprovados (se não, use a proposta e marque).
- Pendências abertas que afetam a decisão (ex.: estimativa da Engenharia, capacidade do time).

Se faltar evidência para uma opção, **diga que falta** em vez de pontuar por intuição.

## Parte 1. Mescla para decisão (`Decisão/01-matriz-de-decisao`)

1. **Pergunta de decisão e premissas vigentes** (com data da última mudança).
2. **Critérios de passagem (eliminatórios):** cada opção passa, não passa ou "não se sabe ainda". Opção que não passa sai da matriz, com o motivo.
3. **Matriz ponderada:** opções x critérios, nota de 1 a 5, com uma linha de evidência (sigla da fonte) e confiança (alta, média, baixa) em cada célula. Mostre a soma ponderada.
4. **Sensibilidade:** recalcule com 2 ou 3 conjuntos de pesos alternativos (ex.: prioridade prazo; prioridade receita). Se a opção vencedora muda, diga.
5. **Hipóteses: estado final** (força, evidência principal, contraevidência).
6. **Requisitos:** proposta de classificação em obrigatório, desejável, diferencial e fora de escopo, citando o ID do mapa e o número de fontes independentes. Requisitos de passagem ficam fora da nota.
7. **Dimensões adicionais**, se o enquadramento as previu (ex.: modelo de entrega: só software; software com implantação; resultado por assinatura; serviço gerenciado com parceiros).
8. **Riscos e premissas** de cada opção.
9. **Recomendação [O]:** opção, escopo de uma primeira versão, condições, e "o que mudaria esta recomendação".
10. **Decisões que o responsável precisa tomar**, numeradas.

Use a planilha ou tabela que o responsável preferir. Calcule somas e sensibilidade por script, não de cabeça.

## Parte 2. Relatório do discovery (`Relatórios/Relatorio-final-do-discovery`)

Use `assets/modelo-relatorio-final.md`. Público: quem decide. Escreva para ser lido em 10 minutos, com anexos para quem quiser aprofundar.

Formato: documento editável (Google Docs, Word ou o documento do Claude), conforme o padrão da empresa. Se a empresa tem layout próprio, peça um exemplo.

## Parte 3. Relatórios de acompanhamento

Durante o discovery, áreas pedem resultados parciais (ex.: Engenharia quer saber o escopo para estimar; Suporte quer ver a análise dos chamados). Para cada um:
- Público e objetivo em uma linha.
- O que já se sabe, o que ainda não se sabe, o que se pede à área.
- **Retire** o que é confidencial para aquele público: nomes de clientes, falas atribuídas a pessoas de outras áreas, preços, opiniões fortes sobre colegas ou sobre o produto, empregador de entrevistados externos.
- Status "preliminar" bem visível.
- Registre no andamento (linha "Relatórios de acompanhamento").

## Regras

- Nada de "o discovery concluiu" enquanto a etapa não for aprovada. Use "a análise preliminar indica".
- Marque [F], [I], [O] também no relatório. No resumo executivo, as frases podem ser curtas, mas a marcação continua.
- Rode a verificação e atualize andamento, pendências e log (a recomendação entra no log como "Análise do Claude, a validar", não como decisão).
