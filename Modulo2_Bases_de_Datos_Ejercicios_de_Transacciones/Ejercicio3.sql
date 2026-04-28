DO $$
DECLARE
    v_exists INTEGER;
    v_product_id VARCHAR(50);
    v_quantity INTEGER;
BEGIN

    SELECT COUNT(*) INTO v_exists
    FROM invoices
    WHERE invoice_id = 'F001';

    IF v_exists = 0 THEN
        RAISE EXCEPTION 'La factura no existe';
    END IF;

FOR product_id, quantity IN 
    SELECT v_product_id, v_quantity
    FROM invoice_items
    WHERE invoice_id = 'F001'
LOOP

    UPDATE products
    SET stock = stock + v_quantity
    WHERE product_id = v_product_id;

END LOOP;

    UPDATE invoices
    SET status = 'RETURNED'
    WHERE invoice_id = 'F001';

    RAISE NOTICE 'Retorno procesado correctamente';

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error en el retorno';
        RAISE;
END $$;