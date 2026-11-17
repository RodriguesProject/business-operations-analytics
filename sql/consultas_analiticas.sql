-- Exemplos de consultas analíticas em PostgreSQL.
-- A tabela demands representa a estrutura da base CSV.
-- Todos os dados do projeto são sintéticos.

-- 1. Volume de demandas por área
SELECT area, COUNT(*) AS total_demandas
FROM demands
GROUP BY area
ORDER BY total_demandas DESC;

-- 2. Distribuição por status e prioridade
SELECT status, prioridade, COUNT(*) AS quantidade
FROM demands
GROUP BY status, prioridade
ORDER BY status, prioridade;

-- 3. Entradas mensais
SELECT DATE_TRUNC('month', data_recebimento)::date AS mes,
       COUNT(*) AS demandas_recebidas
FROM demands
GROUP BY 1
ORDER BY 1;

-- 4. Tempo médio de conclusão (somente demandas encerradas)
SELECT ROUND(AVG(data_conclusao - data_recebimento), 1) AS media_dias_conclusao
FROM demands
WHERE status = 'concluida'
  AND data_conclusao IS NOT NULL;

-- 5. Demandas em aberto com data-alvo anterior à data de referência
SELECT id_demanda, area, prioridade, equipe, data_alvo
FROM demands
WHERE status <> 'concluida'
  AND data_alvo < DATE '2026-11-17'
ORDER BY data_alvo;

-- 6. Volume em aberto por área
SELECT area, COUNT(*) AS demandas_em_aberto
FROM demands
WHERE status <> 'concluida'
GROUP BY area
ORDER BY demandas_em_aberto DESC;
