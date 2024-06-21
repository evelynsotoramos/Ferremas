CREATE TABLE `boleta_factura` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `sucursal_id` int(11) DEFAULT NULL,
  `fecha_venta` varchar(255) DEFAULT NULL,
  `monto_total` float DEFAULT NULL
);

CREATE TABLE `reporte` (
  `id` int(11) NOT NULL,
  `sucursal_id` int(11) DEFAULT NULL,
  `fecha_reporte` varchar(255) DEFAULT NULL,
  `total_ventas` float DEFAULT NULL,
  `total_montos` float DEFAULT NULL,
  `usuario_id` int(255) DEFAULT NULL
);

