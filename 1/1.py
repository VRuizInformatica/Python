/* ==== DROP de las tablas indicadas ==== */
BEGIN
   -- >>> PON AQUÍ TU LISTA <<< 
   FOR t IN (
       SELECT 'OPERATIVE_MOVEMENT' AS nombre FROM dual  UNION ALL
       SELECT 'OTRA_TABLA'                       FROM dual
       -- UNION ALL SELECT 'MAS_TABLAS'         FROM dual
   ) LOOP
      BEGIN
         EXECUTE IMMEDIATE
            'DROP TABLE ' || t.nombre || ' CASCADE CONSTRAINTS PURGE';
      EXCEPTION
         WHEN OTHERS THEN
            IF SQLCODE <> -942 THEN  -- -942 = tabla no existe
               RAISE;                -- muestra el error si es otro
            END IF;
      END;
   END LOOP;
END;
/
