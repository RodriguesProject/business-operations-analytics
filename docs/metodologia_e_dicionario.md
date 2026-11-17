# Metodologia e dicionário de dados

## Escopo

Estudo demonstrativo de análise descritiva de operações. A base foi criada artificialmente para exercitar perguntas gerenciais, preparação de dados, cálculo de indicadores e visualização. Não contém dados reais ou identificáveis.

## Etapas da análise

1. **Entendimento do problema:** definir quais perguntas de gestão a análise deve responder.
2. **Inspeção:** verificar estrutura, tipos, identificadores, datas e valores.
3. **Validação:** checar colunas obrigatórias, identificadores únicos e coerência temporal.
4. **Preparação:** converter campos de data e valor para tipos apropriados.
5. **Análise:** calcular volume, taxa de conclusão, tempo de ciclo e demandas em atraso.
6. **Visualização:** gerar gráficos de volume por área e fluxo mensal de entradas/conclusões.
7. **Comunicação:** interpretar os indicadores sem extrapolar o que a base permite concluir.

## Dicionário de dados

| Campo | Descrição |
|---|---|
| id_demanda | Identificador fictício e único da demanda |
| area | Área operacional simulada |
| data_recebimento | Data de entrada do registro |
| data_conclusao | Data de conclusão; vazia enquanto em aberto |
| status | concluida, em_andamento ou aguardando_informacao |
| etapa | Etapa operacional simulada |
| prioridade | baixa, media ou alta |
| equipe | Equipe fictícia responsável |
| data_alvo | Data de referência operacional fictícia |
| valor_referencial | Valor numérico sintético, sem significado financeiro real |

## Definições dos indicadores

- **Taxa de conclusão:** demandas com status concluida ÷ total de demandas × 100.
- **Tempo médio de conclusão:** média da diferença entre data de conclusão e data de recebimento para demandas concluídas.
- **Demanda em atraso:** registro ainda aberto com data_alvo anterior a 17/11/2026.
- **Fluxo mensal:** quantidade recebida por mês e quantidade concluída por mês de encerramento.

## Limitações

A data de referência (17/11/2026) é fixa para reprodutibilidade. A data-alvo é ilustrativa e não corresponde a prazo legal, contratual ou SLA real. A base é pequena, sintética e adequada apenas para demonstrar técnicas básicas de análise descritiva. Não sustenta inferências causais ou preditivas.
