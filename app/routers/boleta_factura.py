from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from ..dependencias import get_db
from ..database import SessionLocal
from ..dominios.boleta_factura import models, schemas
from fastapi.responses import JSONResponse


routerBoletaFactura=APIRouter(
    tags=["Boleta_Factura"],
    prefix='/boleta_factura'
)

@routerBoletaFactura.get('/')
async def get_boletas_facturas(db: Session = Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Boleta_Factura).all()
    return data

@routerBoletaFactura.get('/{id}')
async def get_boleta_factura(id:int, db: Session= Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Boleta_Factura).filter(models.Boleta_Factura.id==id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message': 'boleta o factura no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerBoletaFactura.post('/')
async def create_boleta_factura(boleta_factura: schemas.boleta_factura, db: Session=Depends(get_db)):
    db= SessionLocal()
    nueva_boleta_factura=models.Boleta_Factura(**boleta_factura.model_dump())
    db.add(nueva_boleta_factura)
    db.commit()
    return JSONResponse (status_code=201, content={'message':'Se ha creado una boleta o factura', 'boleta_factura': boleta_factura.model_dump()})

@routerBoletaFactura.put('/{id}')
async def update_boleta_factura(id:int, boleta_factura: schemas.boleta_factura, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Boleta_Factura).filter(models.Boleta_Factura.id == id).first()
    if not data: 
        return JSONResponse(status_code=404, content={'message': 'No se encontró la boleta o factura'})
    data.usuario_id = boleta_factura.usuario_id
    data.sucursal_id = boleta_factura.sucursal_id
    data.fecha_venta = boleta_factura.fecha_venta
    data.monto_total = boleta_factura.monto_total
    db.commit()
    return JSONResponse(status_code=200, content={'message':'Se modificó la boleta o factura'})

@routerBoletaFactura.delete('/{id}')
async def delete_boleta_factura(id: int, db: Session= Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Boleta_Factura).filter(models.Boleta_Factura.id == id).first()
    if not data: 
        return JSONResponse(status_code=404, content={'message': 'No se encontré la boleta o factura'})
    db.delete(data)
    db.commit()
    return JSONResponse(content={'message': 'Se ha eliminado la boleta o factura', 'boleta_factura': jsonable_encoder(data)})