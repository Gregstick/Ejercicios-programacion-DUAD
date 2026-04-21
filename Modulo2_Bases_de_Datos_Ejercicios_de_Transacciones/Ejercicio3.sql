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

    SELECT product_id, quantity INTO v_product_id, v_quantity
    FROM invoice_items
    WHERE invoice_id = 'F001'
    LIMIT 1;

    UPDATE products
    SET stock = stock + v_quantity
    WHERE product_id = v_product_id;

    UPDATE invoices
    SET status = 'RETURNED'
    WHERE invoice_id = 'F001';

    RAISE NOTICE 'Retorno procesado correctamente';

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error en el retorno';
END $$;