/* =========================================================
   SCRIPT #1 — INVENTARIO  (NO modifica la base de datos)
   Crea:  C:\SPOOLTEST\client_inventory_DELASSMVP.lst
   ========================================================= */
DEFINE SCHEMA = DELASSMVP
DEFINE OUTDIR = C:\SPOOLTEST               -- carpeta ya probada

SET TERMOUT OFF
SET HEADING ON
SET PAGESIZE 500
SET LINESIZE 200

SPOOL &OUTDIR\client_inventory_&SCHEMA.lst

PROMPT === COLUMNAS ===================================================
SELECT owner, table_name, column_name
FROM   all_tab_columns
WHERE  owner = '&SCHEMA'
  AND  column_name LIKE '%CLIENT%';

PROMPT === CONSTRAINTS ================================================
SELECT owner, constraint_name, table_name, constraint_type
FROM   all_constraints
WHERE  owner = '&SCHEMA'
  AND ( constraint_name LIKE '%CLIENT%' OR r_constraint_name LIKE '%CLIENT%' );

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
PROMPT === Inventario generado: &OUTDIR\client_inventory_&SCHEMA.lst ===



/* =========================================================
   SCRIPT #2 — GENERADOR DE RENAMES  (NO ejecuta cambios)
   Crea:  C:\SPOOLTEST\rename_to_borrower_DELASSMVP.sql
   ========================================================= */
DEFINE SCHEMA = DELASSMVP
DEFINE OUTDIR = C:\SPOOLTEST

SET TERMOUT OFF
SET HEADING OFF
SET FEEDBACK OFF
SET PAGESIZE 0
SET LINESIZE 200

SPOOL &OUTDIR\rename_to_borrower_&SCHEMA.sql

PROMPT -- ========= RENAME CLIENT → BORROWER ==========================
SELECT 'ALTER TABLE &SCHEMA..CLIENT RENAME TO BORROWER;' FROM dual;
PROMPT

SELECT DISTINCT
       'ALTER TABLE '||owner||'.'||table_name||
       ' RENAME COLUMN '||column_name||
       ' TO '||REPLACE(column_name,'CLIENT','BORROWER')||';'
FROM   all_tab_columns
WHERE  owner = '&SCHEMA'
  AND  column_name LIKE '%CLIENT%';
PROMPT

SELECT DISTINCT
       'ALTER INDEX '||owner||'.'||index_name||
       ' RENAME TO '||REPLACE(index_name,'CLIENT','BORROWER')||';'
FROM   all_indexes
WHERE  owner = '&SCHEMA'
  AND  index_name LIKE '%CLIENT%';
PROMPT

SELECT DISTINCT
       'ALTER TABLE '||owner||'.'||table_name||
       ' RENAME CONSTRAINT '||constraint_name||
       ' TO '||REPLACE(constraint_name,'CLIENT','BORROWER')||';'
FROM   all_constraints
WHERE  owner = '&SCHEMA'
  AND  constraint_name LIKE '%CLIENT%';
PROMPT

SELECT DISTINCT
       'RENAME '||sequence_name||
       ' TO '||REPLACE(sequence_name,'CLIENT','BORROWER')||';'
FROM   all_sequences
WHERE  sequence_owner = '&SCHEMA'
  AND  sequence_name   LIKE '%CLIENT%';
PROMPT

SELECT 'BEGIN DBMS_UTILITY.compile_schema(schema=>'''||'&SCHEMA'||'''); END; /'
FROM   dual;

SPOOL OFF
SET TERMOUT ON
PROMPT === Guion generado: &OUTDIR\rename_to_borrower_&SCHEMA.sql ===
