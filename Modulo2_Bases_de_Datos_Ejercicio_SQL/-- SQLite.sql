-- SQLite

SELECT codigo_de_producto, SUM(subtotal) AS total_comprado
    FROM detalle_factura
    GROUP BY codigo_de_producto;


