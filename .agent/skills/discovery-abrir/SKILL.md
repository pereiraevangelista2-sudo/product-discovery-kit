---
name: discovery-abrir
description: Abre um discovery de produto, iniciativa ou projeto (Etapa 0, enquadramento) e monta a pasta com os documentos vivos (andamento, mapa de requisitos, registro de pendências, log de decisões, protocolo de trabalho e pedidos de dados). Use sempre que o usuário quiser começar, abrir, iniciar, enquadrar ou estruturar um discovery, definir a pergunta de decisão, as opções, as hipóteses ou os critérios de decisão, ou criar a pasta de um novo discovery, mesmo que não use a palavra "enquadramento".
---

# Abrir um discovery (Etapa 0: enquadramento)

O enquadramento define o que o discovery precisa decidir e como. Tudo o que vem depois (benchmark, entrevistas, chamados, decisão, PRD) testa o que for definido aqui. Um enquadramento fraco gera pesquisa sem foco.

## Regras desta etapa

- **Pergunte antes de criar a pasta.** Um discovery novo só ganha pasta com autorização do usuário. Confirme o nome da pasta.
- **Nada aqui é conclusão.** Hipóteses são apostas a testar; critérios e pesos são proposta até o usuário aprovar.
- **Marque tudo** com [F] fato, [I] inferência e [O] opinião ou sugestão.
- **O status começa como Rascunho.** Só o usuário muda para Aprovado.

## Passo 1. Coletar as respostas da Etapa 0

Faça as perguntas abaixo de uma vez (use a ferramenta de perguntas, se houver). Aceite "não sei": a lacuna vira item de pesquisa, não bloqueio.

1. **O que é o produto ou iniciativa?** Produto novo, módulo, evolução de algo existente, mudança de modelo comercial?
2. **Por que agora?** Gatilhos: pedido de clientes, perda para concorrentes, estratégia, regulação, custo de manutenção.
3. **Quais opções devem ser comparadas?** Ex.: otimizar o existente, construir do zero, híbrido, comprar ou fazer parceria, não fazer nada. Se o usuário não tiver opções, proponha 2 a 4.
4. **Qual a situação atual?** O que existe hoje, quem usa, o que se sabe das dores.
5. **Restrições:** prazo-alvo, time, orçamento, dependências técnicas, decisões já tomadas pela diretoria.
6. **Público-alvo:** porte, segmento, persona compradora e persona usuária.
7. **Concorrentes ou referências conhecidas.**
8. **Quem precisa ser ouvido:** áreas internas, clientes, especialistas.
9. **Formato do entregável final:** existe um modelo de PRD da empresa? Peça exemplos (servem só de formato).
10. **Regras de confidencialidade:** o que nunca pode aparecer em material externo (nomes de clientes, empregador de entrevistados, preços, sistemas).
11. **Onde ficam os arquivos:** Google Drive (pasta "Discoverys"), outro repositório ou os documentos do próprio projeto.

Se o usuário não souber algo que existe publicamente (mercado, concorrentes, regulação), pesquise na internet e marque a fonte.

## Passo 2. Redigir o enquadramento

Use `assets/00-enquadramento.md`. Pontos de atenção:

- **Pergunta de decisão:** uma frase que termina em escolha. Bom: "Devemos lançar X e, se sim, por qual caminho: A, B ou C?". Ruim: "Entender o mercado de X".
- **Opções:** cada uma com descrição e a pergunta-chave que precisa ser respondida para escolhê-la.
- **Hipóteses (H1, H2...):** testáveis, cada uma com a etapa que a testa e o que a refutaria. Prefira 4 a 7. Cubra dor (existe problema?), demanda (alguém paga?), concorrência (perdemos por isso?), viabilidade técnica (quanto custa cada opção?) e modelo comercial.
- **Critérios de decisão com pesos (somam 100%):** proposta para o usuário validar. Separe **critérios de passagem** (eliminatórios, ex.: segurança, conformidade legal) dos critérios ponderados.
- **Lacunas:** o que dá para levantar na internet e o que só existe internamente (vira pedido de dados ou pergunta de entrevista).
- **Melhorias propostas na estrutura** do discovery, se fizer sentido (ex.: etapa de análise do produto atual, matriz de decisão, roteiros com hipóteses comparáveis).

## Passo 3. Criar a estrutura (após autorização)

```
Discoverys/
└── Discovery - <Nome>/
    ├── andamento-do-discovery          (documento vivo: estado atual)
    ├── Enquadramento/
    │   ├── 00-enquadramento
    │   ├── 01-protocolo-de-trabalho
    │   ├── 02-registro-de-pendencias   (documento vivo)
    │   └── 03-log-de-decisoes          (documento vivo)
    ├── Benchmark/
    ├── Entrevistas/
    ├── Chamados/
    ├── Dados internos/
    │   └── pedidos-de-dados-internos
    ├── Requisitos/
    │   └── mapa-de-requisitos          (documento vivo)
    └── Relatórios/
```

Pastas `Decisão/` e `PRD/` só são criadas quando essas etapas começarem.

Modelos em `assets/`: `andamento-do-discovery.md`, `00-enquadramento.md`, `01-protocolo-de-trabalho.md`, `02-registro-de-pendencias.md`, `03-log-de-decisoes.md`, `mapa-de-requisitos.md`, `pedidos-de-dados-internos.md`.

**Onde criar:**
- Google Drive conectado: crie como Google Docs (texto) na pasta. Depois de criado, um documento é sempre **editado no próprio arquivo**, nunca recriado, para manter o link.
- Sem Drive: crie como documentos do projeto ou arquivos .md e avise o usuário.

**Numeração:** dentro de cada subpasta, `NN-nome-curto` em ordem de criação (`00`, `01`, `02`...). Versões novas de um mesmo documento ganham sufixo `-v2`, `-v3`, e a anterior recebe "(substituída)" no título.

## Passo 4. Pedidos de dados internos

Preencha `pedidos-de-dados-internos` com o mínimo necessário por área (Comercial/CRM, Suporte, CS, Engenharia, Produto, Financeiro, Segurança, Marketing). Cada pedido tem ID (C1, S1, CS1, E1...), campos, período, para quê (qual hipótese) e prioridade. Princípios: pedir por empresa e não por pessoa, sem dados pessoais, dados parciais já ajudam, registrar fonte e data de extração.

## Passo 5. Entregar

1. Envie os links dos documentos criados, pedindo que o usuário os adicione ao conhecimento do projeto, se usar Projetos.
2. Liste o que precisa da revisão dele: pergunta de decisão, opções, hipóteses, critérios e pesos.
3. Registre as pendências no `02-registro-de-pendencias` (IDs W para o usuário, C para o Claude).
4. Rode a verificação (abaixo) e coloque o resultado no fim do enquadramento.
5. Diga claramente: "Etapa 0 em rascunho, aguardando sua aprovação."

## Verificação antes de entregar (vale para qualquer documento do discovery)

Registre no fim do documento: "Verificação: x de 10 itens atendidos; exceções: ...".

1. Números e datas batem com a fonte; discrepâncias estão registradas.
2. Toda afirmação está marcada [F], [I] ou [O].
3. Nota gerada por IA e transcrição automática estão rotuladas como não literais.
4. Cada fala está atribuída à pessoa e à fonte certas.
5. Nenhuma informação confidencial aparece em material externo.
6. Cada fonte tem endereço ou nome de arquivo e data.
7. O que não foi encontrado está dito, sem preencher lacuna com estimativa.
8. Hipóteses mantêm a força de evidência registrada, sem elevação.
9. O status está declarado (Rascunho, Em revisão, Aprovado) e nenhuma etapa é dada como concluída.
10. Toda pendência nova tem ID, responsável e data.
