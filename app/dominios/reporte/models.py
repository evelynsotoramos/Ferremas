from sqlalchemy import Column, Integer, String, Float
from ...database import Base

class Reporte(Base):
    __tablename__= 'reporte'
    id=Column(Integer, primary_key=True)
    sucursal_id=Column(Integer)
    fecha_reporte=Column(String)
    total_ventas=Column(Float)
    total_montos=Column(Float)
    usuario_id=Column(Integer)




#CREATE TABLE `reporte` (
#  `reporte_id` integer PRIMARY KEY,
#  `sucursal_id` integer,
#  `fecha_reporte` varchar(255),
#  `total_ventas` float,
#  `total_montos` float,
#  `username` varchar(255)
#);

#ALTER TABLE `reporte` ADD FOREIGN KEY (`reporte_id`) REFERENCES `boleta_factura` (`boleta_factura_id`);