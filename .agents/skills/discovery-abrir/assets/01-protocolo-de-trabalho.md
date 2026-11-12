# 01. Protocolo de trabalho com o Claude neste discovery

**Status:** RASCUNHO, aguardando aprovação de <responsável>.
**Atualizado em:** DD/MM/AAAA.
**Legenda:** [F] fato; [I] inferência; [O] opinião ou sugestão. Nota gerada por IA ou transcrição automática não é fala literal.

## 1. Para que serve

Reúne as regras de como o Claude conduz cada rodada de pesquisa, o que faz sem perguntar, o que depende de aprovação e como os dados são tratados. Não altera nenhuma conclusão do discovery.

## 2. Ciclo de trabalho de cada rodada

1. **Pedido.** O responsável pede uma rodada ou envia um dado novo.
2. **Plano.** O Claude escreve as perguntas, as fontes permitidas, o critério de parada e o limite de buscas. **Ponto de aprovação A:** obrigatório em rodada nova ou mudança de escopo; dispensável em atualização de rotina.
3. **Execução.** O Claude pesquisa ou consolida e preenche o registro de execução (seção 3).
4. **Autocrítica.** Antes de mostrar o resultado, lista o que ficou raso, o que se contradiz e o que falta.
5. **Verificação.** Roda o checklist da seção 4 e registra o resultado no fim do documento.
6. **Rascunho e atualização.** Entrega com status Rascunho, na subpasta certa e com a numeração seguinte; atualiza andamento, mapa de requisitos, pendências e log; envia o link.
7. **Revisão.** **Ponto de aprovação B:** só o responsável muda o status para Aprovado. Sem isso, nenhuma etapa é concluída.
8. **Fechamento.** Status passa a Aprovado e a pendência correspondente é encerrada.

## 3. Registro de execução

Cada rodada de benchmark e cada consolidação de dado externo traz, no fim do documento:

| Campo | O que registra |
|---|---|
| Data e pergunta | Quando a consulta foi feita e qual pergunta respondia |
| Fonte | Endereço ou arquivo consultado e data de acesso |
| Resultado | O que foi encontrado, com [F], [I] ou [O] |
| Não encontrado ou bloqueado | Páginas que não abriram, perguntas sem resposta e motivo |
| Confiança | Alta, média ou baixa, com uma linha de justificativa |

## 4. Verificação antes de entregar

Formato: "Verificação: x de 10 itens atendidos; exceções: ...".

1. Números e datas batem com a fonte; discrepâncias registradas.
2. Toda afirmação marcada [F], [I] ou [O].
3. Nota de IA e transcrição automática rotuladas como não literais.
4. Cada fala atribuída à pessoa e à fonte certas.
5. Nenhuma informação confidencial em material externo.
6. Cada fonte com endereço ou nome de arquivo e data.
7. O que não foi encontrado está dito, sem estimativa no lugar.
8. Hipóteses mantêm a força registrada, sem elevação.
9. Status declarado e nenhuma etapa dada como concluída.
10. Toda pendência nova tem ID, responsável e data.

## 5. Níveis de autonomia

| Nível | Ações |
|---|---|
| **Faz sem perguntar** | Ler arquivos da pasta do discovery; pesquisar fontes públicas; redigir rascunho em documento novo na subpasta certa; atualizar andamento e mapa de requisitos com dado novo, por inserção; rodar a verificação; enviar links. |
| **Só com aprovação** | Mudar documento para Aprovado; concluir etapa; registrar decisão; incluir hipótese; apagar, mover ou reescrever conteúdo existente; criar tarefa agendada; enviar e-mail ou mensagem a terceiros; abrir discovery novo; processar dado Interno ou Confidencial fora do ambiente aprovado. |
| **Nunca** | <regras de confidencialidade específicas>; apresentar nota de IA ou transcrição automática como fala literal; concluir etapa sem revisão; remover a marcação [F], [I], [O]; <outras proibições, ex.: pedir demonstração a concorrente>. |

## 6. Classificação dos dados (proposta)

| Classe | Exemplos | Onde pode ser processada |
|---|---|---|
| Pública | Sites e documentação de concorrentes, editais, artigos, normas | Claude e ferramentas aprovadas |
| Interna | Roteiros, andamento, mapa de requisitos, relatórios, backlog | Claude da empresa e repositório da empresa |
| Confidencial | Gravações, transcrições e notas de entrevistas; empregador de entrevistado; chamados; CRM; preços; dados de clientes e parceiros | Somente no ambiente aprovado, com a pasta do discovery. Nunca em material externo |

## 7. Monitoramento recorrente de fontes públicas (opcional)

Só é criado como tarefa agendada após o responsável definir dia, hora e aceitar que rode sem acompanhamento. Saída: documento curto `monitoramento-AAAA-MM-DD` em Benchmark, com o que mudou, fonte, data e marcação. O monitoramento **propõe**; não altera andamento, hipóteses nem decisões.

## 8. Como pedir cada coisa

| Você quer | Diga algo como | O Claude faz |
|---|---|---|
| Registrar uma entrevista | "Segue a transcrição da entrevista com <perfil>, da área <Y>." | Consolida, marca, verifica e atualiza andamento e mapa |
| Abrir rodada de benchmark | "Abra a rodada 2 do benchmark." | Plano (ponto A), execução após aprovação, entrega com registro e verificação |
| Consolidar chamados ou CRM | "Segue a planilha de chamados." | Consolida com script, reconcilia números, atualiza andamento |
| Registrar uma decisão | "Decidi que..." | Registra no log e atualiza documentos afetados, sem concluir etapa |
| Saber onde estamos | "Onde estamos?" | Situação por etapa, pendências abertas e próximos passos |
| Abrir discovery novo | "Quero abrir o discovery de..." | Pergunta antes e só cria a pasta com autorização |
