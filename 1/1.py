/* ------------- CONFIGURACIÓN DE SALIDA ------------- */
SET TERMOUT OFF
SET HEADING ON
SET PAGESIZE 500
SET LINESIZE 200
COLUMN owner           FORMAT A15
COLUMN table_name      FORMAT A30
COLUMN column_name     FORMAT A30
COLUMN constraint_name FORMAT A30
COLUMN index_name      FORMAT A30
COLUMN trigger_name    FORMAT A30
COLUMN name            FORMAT A30
COLUMN type            FORMAT A12
COLUMN referenced_name FORMAT A30

/* ------------- INICIO DEL SPOOL ------------- */
SPOOL C:/SPOOLTEST/client_references.lst

PROMPT === COLUMNAS ==================================================
SELECT owner, table_name, column_name
FROM   all_tab_columns
WHERE  column_name LIKE '%CLIENT%'
ORDER  BY owner, table_name, column_name;

PROMPT === CONSTRAINTS (PK, FK, CHECK…) =============================
SELECT owner, constraint_name, table_name, constraint_type
FROM   all_constraints
WHERE  constraint_name LIKE '%CLIENT%'
   OR  r_constraint_name LIKE '%CLIENT%'
ORDER  BY owner, table_name, constraint_name;

PROMPT === ÍNDICES ==================================================
SELECT owner, index_name, table_name
FROM   all_indexes
WHERE  index_name LIKE '%CLIENT%'
ORDER  BY owner, table_name, index_name;

PROMPT === SECUENCIAS ===============================================
SELECT sequence_owner AS owner, sequence_name
FROM   all_sequences
WHERE  sequence_name LIKE '%CLIENT%'
ORDER  BY owner, sequence_name;

PROMPT === TRIGGERS =================================================
SELECT owner, trigger_name, table_name
FROM   all_triggers
WHERE  trigger_name LIKE '%CLIENT%'
   OR  table_name   LIKE '%CLIENT%'
ORDER  BY owner, trigger_name;

PROMPT === DEPENDENCIAS (vistas / PL-SQL) ===========================
SELECT owner, name, type, referenced_name, referenced_type
FROM   all_dependencies
WHERE  referenced_name LIKE '%CLIENT%'
ORDER  BY owner, name, referenced_name;

/* ------------- FIN DEL SPOOL ------------- */
SPOOL OFF
SET TERMOUT ON
PROMPT === Inventario completo creado en  C:\SPOOLTEST\client_references.lst  ===
