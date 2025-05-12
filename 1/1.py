SET PAGES 500 LINES 200

-- Objetos cuyo NOMBRE contiene 'CLIENT'
SELECT object_type, object_name
FROM   all_objects
WHERE  owner = 'DELASSMVP'
  AND  object_name LIKE '%CLIENT%'
ORDER  BY object_type, object_name;

-- Columnas cuyo NOMBRE contiene 'CLIENT'
SELECT table_name, column_name
FROM   all_tab_columns
WHERE  owner = 'DELASSMVP'
  AND  column_name LIKE '%CLIENT%'
ORDER  BY table_name, column_name;
