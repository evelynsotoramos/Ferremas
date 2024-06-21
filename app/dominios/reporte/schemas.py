from pydantic import BaseModel
from typing import Optional

class reporte(BaseModel):
    id: Optional[int]= None
    sucursal_id: int
    fecha_reporte: str
    total_ventas: float
    total_montos: float
    usuario_id: int


#CREATE TABLE `reporte` (
#  `reporte_id` integer PRIMARY KEY,
#  `sucursal_id` integer,
#  `fecha_reporte` varchar(255),
#  `total_ventas` float,
#  `total_montos` float,
#  `username` varchar(255)
#);

#ALTER TABLE `reporte` ADD FOREIGN KEY (`reporte_id`)