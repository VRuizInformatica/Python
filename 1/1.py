/*  ▸ Actualiza 50 filas aleatorias en CONTRACTS
    ▸ Asigna fechas consecutivas 01-feb-25 → 22-mar-25
    ▸ Mantiene la parte hora (si existiese)
    ▸ Incluye SAVEPOINT para poder ROLLBACK
*/
DECLARE
    v_base_date   DATE := TO_DATE('01/02/25', 'DD/MM/YY');   -- primer día de la serie
    SAVEPOINT sp_before_update;

    CURSOR c IS
        SELECT rowid                      AS rid,
               data_cut_off_date          AS old_dt,
               ROW_NUMBER() OVER (ORDER BY DBMS_RANDOM.VALUE) AS rn
        FROM   contracts
        WHERE  ROWNUM <= 50;  -- 50 filas al azar (sin orden definido)
BEGIN
    FOR rec IN c LOOP
        UPDATE contracts
           SET data_cut_off_date =
                 /* parte fecha nueva */ (v_base_date + rec.rn-1)
                 /* + parte hora original (si la hubiese) */
                 + (rec.old_dt - TRUNC(rec.old_dt))
         WHERE rowid = rec.rid;
    END LOOP;

    --*** REVISAR RESULTADOS ANTES DE CONFIRMAR ***--
    -- COMMIT;                 -- ← quita el comentario cuando estés seguro
    -- ROLLBACK TO sp_before_update;  -- ← o usa esto para deshacer
END;
/
