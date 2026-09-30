```duckdb
SELECT
  o_orderpriority AS priority,
  count(*) AS orders,
  round(sum(o_totalprice), 2) AS revenue
FROM read_parquet('https://shell.duckdb.org/data/tpch/0_01/parquet/orders.parquet')
GROUP BY 1
ORDER BY revenue DESC
```

