# Guia da arquitetura do discovery

## 1. As quatro camadas

| Camada | O que guarda | Onde |
|---|---|---|
| **Instruções do projeto** | Regras permanentes: quem você é, etapas, marcação [F]/[I]/[O], confidencialidade, onde ficam os arquivos | Projeto do Claude |
| **Skills** | Como fazer cada etapa: passos, modelos, checklist | Personalizar > Skills |
| **Pasta do discovery** | A memória: documentos vivos e documentos de cada etapa | Google Drive (ou documentos do projeto) |
| **Conhecimento do projeto** | Links dos documentos, para as próximas conversas acharem | Projeto do Claude |

O Claude não lembra conversas antigas por conta própria. A pasta e os documentos vivos são o que dá continuidade: cada conversa nova lê o andamento e sabe onde parou.

## 2. Fluxo das etapas

```
0. Enquadramento ──► pergunta de decisão, opções, hipóteses, critérios
        │
        ├─► 1. Benchmark (rodadas)          ┐
        ├─► Roteiros ─► 2. Entrevistas internas │  cada dado novo ─► cascata:
        │            └► 3. Clientes e especialistas │  andamento, mapa de requisitos,
        ├─► 4. Chamados de suporte          │  pendências, log de decisões
        └─► Pedidos de dados internos       ┘
                        │
                        ▼
        Mescla para decisão (matriz) ─► Relatório do discovery ─► PRD
```

As etapas 1 a 4 não precisam ser sequenciais. Comece pelo que dá fatos mais cedo (geralmente Engenharia, Suporte e benchmark).

## 3. Estrutura da pasta

```
Discoverys/
└── Discovery - <Nome>/
    ├── andamento-do-discovery          documento vivo
    ├── Enquadramento/
    │   ├── 00-enquadramento
    │   ├── 01-protocolo-de-trabalho
    │   ├── 02-registro-de-pendencias   documento vivo
    │   └── 03-log-de-decisoes          documento vivo
    ├── Benchmark/                      rodadas e planos
    ├── Entrevistas/                    roteiros e consolidações, numerados
    ├── Chamados/                       consolidações (v1, v2...)
    ├── Dados internos/                 pedidos e dados recebidos
    ├── Requisitos/
    │   └── mapa-de-requisitos          documento vivo
    ├── Relatórios/                     parciais por área e relatório final
    ├── Decisão/                        criada quando a etapa começar
    └── PRD/                            criada quando a etapa começar
```

**Numeração:** `NN-nome` em ordem de criação dentro de cada pasta. Versão nova ganha `-v2`; a anterior recebe "(substituída)" no título, sem ser apagada.

## 4. Os documentos vivos

| Documento | Pergunta que responde |
|---|---|
| Andamento | Onde estamos? O que já se sabe? |
| Mapa de requisitos | O que o produto pode precisar ter, e com quanta evidência? |
| Registro de pendências | O que falta, com quem, desde quando? (W = seu; C = do Claude) |
| Log de decisões | O que foi decidido e o que cada decisão substituiu? |

Eles são **editados no próprio arquivo**, nunca recriados, para o link continuar valendo.

## 5. Ciclo de cada rodada e pontos de aprovação

1. Pedido → 2. **Plano (ponto A, em rodada nova)** → 3. Execução com registro → 4. Autocrítica → 5. Verificação de 10 itens → 6. Rascunho + atualização da cascata + link → 7. **Revisão sua (ponto B)** → 8. Aprovado e pendência encerrada.

Sem o ponto B, nenhuma etapa é concluída. Isso evita que a pesquisa "conclua sozinha".

## 6. Níveis de autonomia

| O Claude faz sem perguntar | Só com sua aprovação | Nunca |
|---|---|---|
| Ler a pasta; pesquisar fontes públicas; criar rascunho na subpasta certa; inserir dados novos nos documentos vivos; rodar a verificação; enviar links | Aprovar documento; concluir etapa; registrar decisão; incluir hipótese; apagar ou reescrever conteúdo; criar tarefa agendada; mandar mensagem a terceiros; abrir discovery novo | Quebrar a confidencialidade; tratar nota de IA como fala literal; concluir etapa sem revisão; remover a marcação [F]/[I]/[O] |

## 7. Marcação e força da evidência

- **[F] fato:** dito pela fonte ou publicado, com referência.
- **[I] inferência:** leitura do Claude a partir dos fatos.
- **[O] opinião:** do entrevistado ou sugestão do Claude.
- **Fonte não literal:** transcrição automática e notas geradas por IA são rotuladas e nunca viram citação entre aspas.
- **Força das hipóteses:** Sem evidência · Fraca · Fraca a moderada · Moderada · Forte · Refutada. Sobe só com evidência nova e com justificativa.
- **Fontes independentes:** no mapa de requisitos, conta-se quantas fontes **independentes** sustentam cada item. Um workshop interno com pessoas já entrevistadas não é fonte nova.

## 8. Classificação dos dados

| Classe | Exemplos | Onde pode ser processada |
|---|---|---|
| Pública | Sites de concorrentes, editais, artigos | Qualquer ferramenta aprovada |
| Interna | Roteiros, andamento, mapa, relatórios | Claude da empresa e repositório da empresa |
| Confidencial | Gravações, transcrições, chamados, CRM, preços, dados de clientes, empregador de entrevistados | Só no ambiente aprovado; nunca em material externo |

Ajuste esta tabela à política da sua empresa no documento `01-protocolo-de-trabalho` de cada discovery.

## 9. Lições aprendidas (por que o método é assim)

1. **Notas de IA e transcrições automáticas erram nomes, siglas e números.** Por isso a seção "termos da transcrição" e a regra de não citar como literal.
2. **Números de memória parecem dados.** Registre sempre "dado ou memória" e peça o dado ao sistema de origem (CRM, helpdesk).
3. **Exportações de helpdesk podem vir cortadas** (limite de linhas, serviço genérico fora do filtro). Compare totais por mês e reconcilie com o que a área disse.
4. **Quem vende e quem constrói têm viés.** Entrevistas internas são necessárias, mas não provam demanda. Ouça clientes e especialistas do porte certo.
5. **Um especialista de empresa muito maior que o público-alvo pode descrever outro mercado** (ex.: quem desenvolve tudo internamente não compra ferramenta). Pergunte o que vale para cada porte.
6. **Premissas mudam no meio do caminho** (ex.: a diretoria muda o modelo comercial ou o escopo). Registre no log, marque a antiga como substituída e propague para hipóteses e requisitos.
7. **Andamento que mistura estado, histórico e regras fica ilegível.** Por isso pendências, decisões e protocolo têm documentos próprios desde o início.
8. **Chamados mostram atrito, não demanda.** Diga isso no documento para ninguém usar volume de chamado como prova de mercado.
9. **Relatórios parciais circulam.** Antes de compartilhar com uma área, retire falas atribuídas, nomes de clientes e opiniões fortes sobre pessoas ou produtos.
10. **Estimativas dadas em reunião são faixa inicial, não compromisso.** Registre premissa, confiança e o que falta (escopo, capacidade do time).

## 10. Extensões opcionais

- **Lente de IA no mapa de requisitos:** colunas "papel da IA" e "forma de interação", se o produto tiver diretriz de IA.
- **Dimensão "modelo de entrega" na decisão:** só software; software com implantação; resultado por assinatura; serviço gerenciado com parceiros.
- **Monitoramento semanal de concorrentes** como tarefa agendada, que só propõe mudanças.
- **Dossiê de continuidade** ao trocar de ferramenta, de conversa ou de responsável.
