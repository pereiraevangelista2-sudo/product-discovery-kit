---
name: discovery-prd
description: Escreve o PRD (documento de requisitos de produto) a partir de um discovery, com cada requisito rastreável até a evidência do mapa de requisitos, escopo por versão (MVP, incrementos, fora de escopo), métricas, riscos e perguntas em aberto, seguindo o modelo da empresa quando houver. Use sempre que o usuário pedir PRD, documento de requisitos, especificação de produto, épicos ou histórias a partir do discovery, ou quiser transformar a decisão do discovery em algo que o time possa construir.
---

# PRD a partir do discovery

O PRD traduz a decisão em algo construível. O valor de um PRD feito ao fim de um discovery é a **rastreabilidade**: cada requisito aponta para a evidência que o justifica, e o que não tem evidência aparece como aposta.

## Pré-requisitos

- Decisão registrada no log (opção escolhida e escopo). Se ainda não houver, avise: o PRD pode ser escrito como rascunho condicionado, com a premissa no topo.
- Mapa de requisitos atualizado e, idealmente, classificação aprovada (obrigatório, desejável, diferencial).
- **Modelo da empresa:** pergunte se há um modelo ou exemplos de PRD. Exemplos servem **só de formato**; não copie conteúdo deles. Sem modelo, use `assets/modelo-prd.md`.
- Formato de saída: documento editável (Google Docs, Word ou documento do Claude), conforme o padrão da empresa.

## Como escrever

1. **Contexto e problema** com as evidências principais (siglas e links), não com adjetivos.
2. **Objetivos e métricas de sucesso.** Se o discovery não trouxe linha de base, escreva "linha de base a medir" em vez de inventar número.
3. **Público e personas** (compradora e usuária), com o que se sabe e o que não se sabe.
4. **Escopo por versão:** MVP, incrementos, fora de escopo (com motivo). O MVP deve caber no prazo e na capacidade informados; se não houver dado de capacidade, registre o risco.
5. **Requisitos funcionais** em tabela: ID do PRD, descrição, ID do mapa (R#), fontes, prioridade, critério de aceite. Requisito sem ID do mapa é marcado **[O] proposta, sem evidência do discovery**.
6. **Requisitos não funcionais** (segurança, privacidade, desempenho, disponibilidade, auditoria, acessibilidade), com os critérios de passagem do discovery.
7. **Fluxos e jornadas** principais (texto ou diagrama simples).
8. **Regras de negócio.**
9. **Dependências** (técnicas, de outras áreas, de fornecedores).
10. **Riscos, premissas e perguntas em aberto**, puxando as pendências do registro que afetam o produto.
11. **Plano de lançamento e migração**, se houver base atual.
12. **Anexo de rastreabilidade:** requisito do PRD → ID do mapa → fontes → documento do discovery.

## Regras

- Não eleve a força da evidência: requisito de uma fonte continua sendo de uma fonte.
- Confidencialidade: o PRD costuma circular mais que o discovery. Não cite clientes, entrevistados externos, empregadores deles, preços internos nem falas atribuídas a pessoas. Use perfis genéricos (ex.: "especialista externo do setor financeiro" ou só "especialista externo", se o setor também for sensível).
- Status Rascunho até o responsável aprovar. Atualize andamento, pendências e log; envie o link; rode a verificação.
