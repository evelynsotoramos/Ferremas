from pydantic import BaseModel
from typing import Optional

class boleta_factura(BaseModel):
    id: Optional[int]=None
    usuario_id: int
    sucursal_id: int
    fecha_venta: str
    monto_total: float
    
    
#Creación de tabla 
#CREATE TABLE `boleta_factura` (
  #`boleta_factura_id` integer PRIMARY KEY,
  #`usuario_id` integer,
  #`sucursal_id` integer,
  #`fecha_venta` varchar(255),
  #`monto_total` float
#);    