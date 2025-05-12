/* ----- formato de salida ----- */
SET TERMOUT OFF
SET HEADING ON
SET PAGESIZE 500
SET LINESIZE 200

/* ----- inicia spool ----- */
SPOOL C:/SPOOLTEST/client_inventory_DELASSMVP.lst

/* columnas que contienen CLIENT */
PROMPT === COLUMNAS ==============================================
SELECT owner, table_name, column_name
FROM   all_tab_columns
WHERE  owner = 'DELASSMVP'
  AND  column_name LIKE '%CLIENT%';

/* constraints */
PROMPT === CONSTRAINTS ===========================================
SELECT owner, constraint_name, table_name, constraint_type
FROM   all_constraints
WHERE  owner = 'DELASSMVP'
  AND ( constraint_name LIKE '%CLIENT%' OR r_constraint_name LIKE '%CLIENT%' );

/* índices */
PROMPT === ÍNDICES ===============================================
SELECT owner, index_name, table_name
FROM   all_indexes
WHERE  owner = 'DELASSMVP'
  AND  index_name LIKE '%CLIENT%';

/* secuencias */
PROMPT === SECUENCIAS ============================================
SELECT sequence_owner AS owner, sequence_name
FROM   all_sequences
WHERE  sequence_owner = 'DELASSMVP'
  AND  sequence_name   LIKE '%CLIENT%';

/* triggers */
PROMPT === TRIGGERS ==============================================
SELECT owner, trigger_name, table_name
FROM   all_triggers
WHERE  owner = 'DELASSMVP'
  AND ( trigger_name LIKE '%CLIENT%' OR table_name LIKE '%CLIENT%' );

/* dependencias de código */
PROMPT === DEPENDENCIAS (vistas / PL-SQL) ========================
SELECT owner, name, type, referenced_name, referenced_type
FROM   all_dependencies
WHERE  referenced_owner = 'DELASSMVP'
  AND   referenced_name LIKE '%CLIENT%';

/* ----- cierra spool ----- */
SPOOL OFF
SET TERMOUT ON
PROMPT === Inventario creado en  C:\SPOOLTEST\client_inventory_DELASSMVP.lst  ===
