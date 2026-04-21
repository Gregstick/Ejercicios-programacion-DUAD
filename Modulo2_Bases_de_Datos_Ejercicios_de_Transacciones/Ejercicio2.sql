DO $$
DECLARE
    stock INTEGER;
    user_exist INTEGER;
    price INTEGER;
    quantity INTEGER := 1;
BEGIN

    SELECT COUNT(*) INTO user_exist
    FROM users
    WHERE user_id = 'U001';

    IF user_exist = 0 THEN
        RAISE EXCEPTION 'El usuario no existe';
    END IF;

    SELECT stock, price INTO stock, price
    FROM products
    WHERE product_id = 'P001';

    IF stock IS NULL OR stock < quantity THEN
        RAISE EXCEPTION 'Stock insuficiente';
    END IF;

    INSERT INTO invoices (invoice_id, user_id, status)
    VALUES ('F001', 'U001', 'COMPLETED');

    INSERT INTO invoice_items (invoice_id, product_id, quantity, subtotal)
    VALUES ('F001', 'P001', quantity, price * quantity);

    UPDATE products
    SET stock = stock - quantity
    WHERE product_id = 'P001';

    RAISE NOTICE 'Compra realizada correctamente';

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error en la compra';
END $$;

