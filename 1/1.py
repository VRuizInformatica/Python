/* ============ CONFIGURACIÓN ============
   Cambia la ruta de OUTDIR si lo necesitas
   ====================================== */
DEFINE  SCHEMA = DELASSMVP
DEFINE  OUTDIR = "C:\Users\TuUsuario\Documents\Titulizacion2025"

/* ---------- FORMATO DE SALIDA ---------- */
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

/* ---------- INVENTARIO COMPLETO ---------- */
SPOOL &OUTDIR\client_inventory_&SCHEMA.lst

PROMPT === COLUMNAS QUE CONTIENEN "CLIENT" ============================
SELECT owner, table_name, column_name
FROM   all_tab_columns
WHERE  owner = '&SCHEMA'
  AND  column_name LIKE '%CLIENT%'
ORDER  BY table_name, column_name;

PROMPT === CONSTRAINTS (PK, FK, CHECK…) ===============================
SELECT owner, constraint_name, table_name, constraint_type
FROM   all_constraints
WHERE  owner = '&SCHEMA'
  AND ( constraint_name LIKE '%CLIENT%'
     OR r_constraint_name LIKE '%CLIENT%' );

PROMPT === ÍNDICES ====================================================
SELECT owner, index_name, table_name
FROM   all_indexes
WHERE  owner = '&SCHEMA'
  AND  index_name LIKE '%CLIENT%';

PROMPT === SECUENCIAS =================================================
SELECT sequence_owner AS owner, sequence_name
FROM   all_sequences
WHERE  sequence_owner = '&SCHEMA'
  AND  sequence_name   LIKE '%CLIENT%';

PROMPT === TRIGGERS ===================================================
SELECT owner, trigger_name, table_name
FROM   all_triggers
WHERE  owner = '&SCHEMA'
  AND ( trigger_name LIKE '%CLIENT%' OR table_name LIKE '%CLIENT%' );

PROMPT === DEPENDENCIAS (VISTAS / PL-SQL) =============================
SELECT owner, name, type, referenced_name, referenced_type
FROM   all_dependencies
WHERE  referenced_owner = '&SCHEMA'
  AND   referenced_name LIKE '%CLIENT%';

SPOOL OFF
SET TERMOUT ON
PROMPT === Inventario creado: &OUTDIR\client_inventory_&SCHEMA.lst ===
