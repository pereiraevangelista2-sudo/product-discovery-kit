---
name: discovery-roteiros
description: Cria e versiona roteiros de entrevista para discovery de produto, ligados às hipóteses, para áreas internas (Engenharia, Suporte, CS, Comercial, Produto, Jurídico, Marketing, Segurança da Informação, Financeiro), clientes e especialistas externos, com versão enxuta de 30 a 40 minutos, perguntas essenciais marcadas e entrevistas em dois níveis (gestão e analistas). Use sempre que o usuário pedir roteiro, perguntas para entrevista, preparação de reunião de discovery, pauta para conversar com uma área ou cliente, ou quiser ajustar um roteiro existente.
---

# Roteiros de entrevista

Um bom roteiro testa hipóteses, colhe fatos e números e evita induzir respostas. Cada pergunta deve existir por um motivo: uma hipótese (H#), uma lacuna do enquadramento ou um requisito (R#) a validar.

## Antes de escrever

Leia o enquadramento, o andamento e o mapa de requisitos. Pergunte ao responsável, se não estiver claro:
- Quem será entrevistado (área, cargo, nível) e quanto tempo há.
- É interno, cliente ou especialista externo?
- Há ponto em aberto de entrevistas anteriores para fechar com essa pessoa?

## Princípios (valem para todo roteiro)

1. **Foco declarado por seção:** "Foco: H2 e H3".
2. **Essenciais marcadas com ⭐** para quando o tempo for curto.
3. **"Como é hoje?" antes de qualquer ideia de solução.** Não apresentar o produto a externos; só no fim, se perguntarem.
4. **Peça exemplos reais e números** (último caso, quantos, quanto tempo). Anote se vem de **dado** ou de **memória**.
5. **Dois níveis** quando possível: gestão (riscos, prioridades, orçamento, critério de compra) e analistas da ponta (passo a passo, planilhas paralelas, atritos, tempo por tarefa).
6. **Confidencialidade:** pergunte a externos se podem ser citados por nome ou só por perfil e o que não pode ser registrado. Informação do empregador do entrevistado nunca vai para material externo.
7. **Segurança da Informação:** não registrar vulnerabilidades nem detalhes sensíveis; só o nível geral (existe / atende / não atende).
8. **Separar papéis:** se o especialista também vende serviço no tema, peça que responda primeiro como comprador ou observador e depois como fornecedor; anote o viés.
9. **Sempre fechar com:** "Se pudesse mudar uma coisa, qual seria?", "O que eu não perguntei e deveria?", "Quem mais devo ouvir? Que dados ou documentos você pode compartilhar?".
10. **Perguntas de confirmação** de pontos levantados por outras entrevistas entram num bloco "Complemento para <perfil>", com o ID do ponto (ex.: Q4 da entrevista 02).

## Tipos de roteiro

- **Roteiro geral** (`01-roteiros-entrevistas`): uma seção por área interna + especialistas + clientes, abertura e fechamento comuns, modelo de registro e ordem sugerida.
- **Roteiro específico** (`NN-roteiro-<area>-DD-MM`): para uma reunião marcada, com os pontos em aberto daquela área.
- **Roteiro enxuto** para especialistas ou clientes (30 a 40 min, cerca de 8 perguntas principais e 4 de apoio), com tempo por bloco.

O banco de perguntas por área está em `references/banco-de-perguntas.md`. Adapte ao tema; não copie tudo.

## Ordem sugerida das entrevistas

1. Engenharia, Suporte e Segurança da Informação: dão fatos que orientam as demais.
2. CS, Comercial e Marketing: demanda, perdas, mercado, receita.
3. Especialistas externos e clientes: visão sem viés interno.
4. Produto e Jurídico: refinamento.

## Versões

Ao mudar um roteiro já usado, crie versão nova (v2, v3) e inclua uma tabela "Mudanças em relação à versão anterior" (antes, depois, motivo). Um bloco novo ligado a uma hipótese nova leva o ID da hipótese e uma nota de origem.

## Modelo de registro (fim de todo roteiro)

| Campo | Preencher |
|---|---|
| Entrevistado (nome ou perfil, área, cargo) | |
| Nível (gestão ou analista) | |
| Data e duração | |
| Entrevistador | |
| Fonte do registro (anotação própria, transcrição automática, notas de IA) | |
| Hipóteses testadas | |
| Dados e números citados (dado ou memória) | |
| Dores e necessidades | |
| Citações marcantes (só se literais) | |
| Oportunidades ou ideias | |
| Riscos ou alertas | |
| Evidências a pedir | |
| Indicações (com permissão de contato) | |
| Confidencial: o que não pode ser citado | |

## Depois de entregar

Status Rascunho, link enviado, pendência registrada ("revisar roteiro X"), linha "Preparação das entrevistas" do andamento atualizada. Verificação no fim do documento.
