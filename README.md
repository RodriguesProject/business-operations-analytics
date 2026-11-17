# Business Operations Analytics — Análise de Dados de Demandas e Processos

**Projeto demonstrativo de portfólio | Thiago Rodrigues**

> Estudo autoral de análise de dados aplicada à gestão de demandas e processos. O contexto é inspirado em operações administrativas e jurídicas, mas todos os registros, equipes, datas e valores desta base são inteiramente sintéticos. O projeto não representa clientes, processos judiciais reais, empresas ou resultados profissionais.

## Visão geral

Este projeto demonstra como transformar registros operacionais em informação estruturada para apoiar decisões de gestão. A análise parte de uma base fictícia de demandas e percorre etapas de inspeção, tratamento, criação de indicadores, análise descritiva e visualização.

O domínio jurídico é utilizado apenas como contexto de negócio. O projeto concentra-se em **Análise de Dados e Business Analysis**, com análise descritiva de indicadores operacionais.

## Perguntas de negócio

- Qual é o volume de demandas por área e por período?
- Como as demandas se distribuem por status, etapa e prioridade?
- Qual é a taxa de conclusão no conjunto analisado?
- Qual é o tempo médio de conclusão das demandas encerradas?
- Quantas demandas em aberto ultrapassaram a data-alvo definida na base?
- Quais recortes merecem atenção gerencial?

## Competências demonstradas no estudo

| Etapa | Aplicação no projeto |
|---|---|
| Entendimento do negócio | Definição das perguntas gerenciais e dos indicadores |
| Preparação dos dados | Leitura, tipagem, validação e tratamento de datas |
| Análise exploratória | Distribuição por área, status, prioridade e mês |
| Indicadores (KPIs) | Volume, taxa de conclusão, tempo médio e demandas vencidas |
| Visualização | Gráficos para leitura de volume e fluxo mensal |
| SQL | Consultas agregadas para responder às perguntas de negócio |
| Comunicação analítica | Síntese dos resultados e registro das limitações |

## Tecnologias e nível de desenvolvimento

- **Python:** fundamentos e aplicação em scripts de análise.
- **Pandas:** leitura, transformação, agrupamento e sumarização de dados em desenvolvimento.
- **Matplotlib:** visualizações básicas.
- **SQL / PostgreSQL:** consultas relacionais e agregações em nível introdutório.
- **Git e GitHub:** versionamento e documentação do projeto.

As tecnologias são apresentadas como conhecimentos em desenvolvimento, coerentes com a formação atual. Este projeto não pretende sugerir experiência profissional avançada em engenharia de dados, desenvolvimento de software .

## Estrutura

```text
business-operations-analytics/
├── README.md
├── requirements.txt
├── data/
│   └── demandas_sinteticas.csv
├── src/
│   └── analise_operacional.py
├── sql/
│   └── consultas_analiticas.sql
├── docs/
│   └── metodologia_e_dicionario.md
└── outputs/                 # gerado ao executar o script
    ├── resumo_indicadores.json
    ├── demandas_por_area.csv
    ├── entrada_vs_conclusao_mensal.csv
    └── *.png
```

## Como executar

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a análise a partir da raiz do repositório:

```bash
python src/analise_operacional.py
```

O script imprime os principais indicadores e cria os arquivos de resumo e gráficos na pasta `outputs/`.

## Indicadores utilizados

- **Demandas registradas:** quantidade de identificadores únicos.
- **Demandas concluídas:** registros com status `concluida`.
- **Demandas em aberto:** registros ainda não concluídos.
- **Taxa de conclusão:** demandas concluídas divididas pelo total.
- **Tempo médio de conclusão:** média de dias entre recebimento e encerramento, considerando apenas as concluídas.
- **Demandas em atraso:** demandas em aberto cuja data-alvo é anterior à data de referência do estudo.

A data de referência é fixa (**17/11/2026**) para permitir reprodução dos mesmos resultados. Os indicadores descrevem exclusivamente a base sintética.

## Resultado de referência da base sintética

Na execução sobre os 30 registros fictícios, considerando a data de referência de 17/11/2026, os indicadores calculados são:

| Indicador | Resultado |
|---|---:|
| Demandas registradas | 30 |
| Demandas concluídas | 15 |
| Demandas em aberto | 15 |
| Taxa de conclusão | 50,0% |
| Tempo médio de conclusão | 23 dias |
| Demandas em aberto com data-alvo vencida | 14 |

Esses números servem para demonstrar o cálculo e a comunicação dos indicadores no conjunto sintético; não representam produtividade, desempenho ou prazos de uma operação real.

## Consultas SQL

O arquivo [sql/consultas_analiticas.sql](sql/consultas_analiticas.sql) contém exemplos de consultas para volume por área, status, evolução mensal, tempo médio de conclusão e demandas em atraso. O script Python não depende de um servidor PostgreSQL: as consultas são material de estudo para adaptação a uma tabela relacional.

## Limitações e integridade

- A base é pequena e artificial; não permite inferir desempenho real de uma organização.
- A data de referência é fixa e foi escolhida para reprodutibilidade.
- A data-alvo é um campo ilustrativo da base, não um prazo jurídico ou SLA validado.
- Os resultados são descritivos, não preditivos.
- Nenhum dado de cliente, processo judicial, parte, advogado ou instituição foi utilizado.

## Sobre o autor

Profissional com formação em Administração e Direito e trajetória em gestão administrativa, operações, contratos, análise documental e gestão de processos. Atualmente desenvolve competências em Business Analysis e Análise de Dados por meio da Carreira Tech – Trilha Análise de Dados (SCTEC/SENAI).

- **LinkedIn:** https://www.linkedin.com/in/thiago-rodrigues-2112188b/
- **GitHub:** https://github.com/RodriguesProject
- **Localização:** Joinville, Santa Catarina, Brasil

---
*Projeto educacional e demonstrativo. Os dados e resultados não representam uma operação real.*
