from sqlalchemy import Column, Integer, String, Float
from ...database import Base

class Boleta_Factura(Base):
    __tablename__= 'boleta_factura'
    id=Column(Integer, primary_key=True)
    usuario_id=Column(Integer)
    sucursal_id=Column(Integer)
    fecha_venta=Column(String)
    monto_total=Column(Float)