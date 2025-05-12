DEFINE SCHEMA = DELASSMVP
DEFINE OUTDIR = C:/SQLSpool         -- carpeta SIN espacios (créala si no existe)

SPOOL &OUTDIR/client_inventory_&SCHEMA.lst

SELECT owner, table_name, column_name
FROM   all_tab_columns
WHERE  owner = '&SCHEMA'
  AND  column_name LIKE '%CLIENT%';

SPOOL OFF
