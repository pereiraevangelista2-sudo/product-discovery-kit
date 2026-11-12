---
name: discovery-atualizar
description: Mantém os documentos vivos de um discovery de produto em dia a cada dado novo - andamento (situação por etapa, entrevistas, hipóteses e força de evidência, achados, riscos), mapa de requisitos, registro de pendências e log de decisões - e responde "onde estamos?". Use sempre que chegar qualquer informação nova no discovery (entrevista, planilha, decisão, relato de reunião, resposta a uma pendência), quando o usuário disser "decidi que...", "atualiza o andamento", "onde estamos?", "o que falta?", ou pedir um retrato ou dossiê para continuar o trabalho em outra conversa.
---

# Atualizar o discovery (cascata de documentos vivos)

O discovery tem quatro documentos vivos. Se um deles fica desatualizado, o próximo passo é decidido com base errada. Esta skill garante que todo dado novo percorra a cascata inteira.

| Documento | Responde | Onde |
|---|---|---|
| andamento-do-discovery | Onde estamos e o que já se sabe | Raiz da pasta |
| mapa-de-requisitos | O que o produto pode precisar ter, com que evidência | Requisitos/ |
| registro-de-pendencias | O que falta, com quem, desde quando | Enquadramento/ |
| log-de-decisoes | O que foi decidido, quando e o que substituiu | Enquadramento/ |

## Regras gerais

- **Edite no próprio arquivo.** Nunca recrie um documento vivo (perde o link e a sincronização). No Google Docs, use edição por trecho.
- **Atualização por inserção.** Acrescentar é livre; apagar, mover ou reescrever conteúdo existente exige aprovação do responsável.
- **Atualize a linha "Atualizado em"** com data e uma frase sobre o que mudou.
- **Dado novo consolidado vira documento novo** na subpasta certa, com a numeração seguinte (ver skills de entrevista, benchmark e chamados). Os documentos vivos só recebem o resumo e o link.
- **Nada é concluído sem revisão.** Termine cada registro de decisão com "Nenhuma etapa foi concluída", salvo se a decisão for aprovar a etapa.

## A cascata (siga na ordem)

### 1. Andamento
- **Situação por etapa:** atualize a linha afetada (situação, documento, próximo passo).
- **Entrevistas:** linha nova ou atualizada (número, perfil, classificação, fonte e situação).
- **Hipóteses:** acrescente a evidência com a sigla da fonte. Ajuste a força **só** se a evidência justificar, e diga por quê. Escala: Sem evidência · Fraca · Fraca a moderada · Moderada · Forte · Refutada (no nível X). Uma voz só, de memória, não passa de Fraca a moderada. Contraevidência é registrada junto. Hipótese nova entra como "proposta, aguardando decisão".
- **Principais achados:** bloco por fonte, com [F], [I], [O] e o rótulo da fonte (ex.: "transcrição automática, a conferir").
- **Riscos e limites conhecidos:** acrescente vieses e lacunas novos.
- **Mudança de premissa** (ex.: o produto deixa de ser vendido separadamente): registre na seção 1 com data e propague para hipóteses e requisitos afetados.

### 2. Mapa de requisitos
- Requisito já existente: acrescente o que foi dito com a sigla da fonte e recalcule o número de fontes **independentes** (fontes internas das mesmas pessoas não somam).
- Requisito novo: R (funcional), N (não funcional ou comercial) ou X (uma só fonte, sem demanda confirmada).
- Tensões: quando uma fonte pede e outra desaconselha, registre numa "Atualização de DD/MM (<fonte>)".
- Nunca classifique em obrigatório/desejável/diferencial sem aprovação.

### 3. Registro de pendências
- Pendência nova: próximo ID livre (W para o responsável, C para o Claude), situação, data de referência, observação.
- Pendência atendida pelo dado novo: mude a situação (Resolvida, Feita, Parcial) e diga o que resta.
- Nunca reaproveite IDs.

### 4. Log de decisões
- Só quando o responsável decidiu ou informou algo. Classifique o tipo (Decisão, Informação, Relato sem ata, Operacional, Análise do Claude a validar).
- Decisão que substitui outra: marque a antiga como "Substituída em DD/MM" e aponte na nova.
- Atualize o resumo de decisões vigentes no andamento (seção 6).

### 5. Entregar
- Envie os links dos documentos **novos** e peça para adicioná-los ao conhecimento do projeto, se usar Projetos.
- Liste em poucas linhas o que mudou e o que precisa de revisão.
- Rode a verificação nos documentos novos.

## "Onde estamos?"

Leia andamento e registro de pendências e responda em até 15 linhas:
1. Pergunta de decisão atual (e a última mudança de premissa).
2. Situação por etapa em uma linha cada.
3. Hipóteses com a força atual.
4. Três a cinco pendências mais importantes do responsável (com ID).
5. Próximo passo sugerido [O].

## Retrato para continuidade (dossiê)

Quando o trabalho mudar de conversa, ferramenta ou pessoa, ou ficar parado muito tempo, gere `Dossie-de-Continuidade-DD-MM` na raiz: pergunta de decisão, premissas, decisões vigentes, hipóteses e força, achados por fonte, requisitos principais, pendências abertas, estrutura de pastas e regras de trabalho. Ele é um retrato daquela data; o andamento continua sendo o documento vivo.

## Relatórios de acompanhamento

Para compartilhar resultados parciais com uma área (Engenharia, Suporte, diretoria), crie em Relatórios/ um documento curto para aquele público: o que se perguntou, o que se encontrou, o que ainda não se sabe, o que se pede à área. Retire nomes de clientes, falas de terceiros e tudo que for confidencial para aquele público. Ver a skill `discovery-decisao-relatorio`.

O checklist de verificação está em `references/verificacao.md`.
