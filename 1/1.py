-- Sustituye BORROWER por el nombre real de la tabla que quieras revisar
SELECT column_name
FROM   user_tab_columns
WHERE  table_name = 'BORROWER'       -- en mayúsculas
  AND  column_name LIKE '%CLIENT%';
