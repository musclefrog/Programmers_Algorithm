# 0부터 23까지의 시간(h)를 생성하는 재귀 CTE
WITH RECURSIVE hours AS (
		SELECT 0 AS hour
		UNION ALL
		SELECT hour + 1 
		FROM hours 
		WHERE hour < 23
)

# 각 시간별 입양 횟수를 집계
SELECT
		h.hour AS HOUR,
		COUNT(a.ANIMAL_ID) AS COUNT
FROM
		hours h
LEFT JOIN
		ANIMAL_OUTS a
		ON HOUR(a.DATETIME) = h.hour
GROUP BY h.hour
ORDER BY h.hour