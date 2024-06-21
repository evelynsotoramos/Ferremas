from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..dependencias import get_db
from ..dominios.reporte import models, schemas
from fastapi.responses import JSONResponse

routerReporte=APIRouter(
    tags=["Reporte"],
    prefix='/reporte'
)

@routerReporte.get('/')
async def get_reportes(db: Session= Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Reporte).all()
    return data

@routerReporte.get('/{id}')
async def get_reporte(id:int, db: Session= Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Reporte).filter(models.Reporte.id==id).first()
    if not data:
        return JSONResponse(status_code=404, content={'message':'Reporte no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))

@routerReporte.post('/')
async def create_reporte(reporte: schemas.reporte, db: Session=Depends(get_db)):
    db= SessionLocal()
    nuevo_reporte=models.Reporte(**reporte.model_dump())
    db.add(nuevo_reporte)
    db.commit()
    return JSONResponse(status_code=201, content={'message': 'Reporte creado existosamente', 'reporte': reporte.model_dump()})

@routerReporte.put('/{id}')
async def update_reporte(id:int, reporte: schemas.reporte, db: Session=Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Reporte).filter(models.Reporte.id==id).first()
    if not data: 
        return JSONResponse (status_code=404, content={'message': 'Reporte no encontrado'})
    data.sucursal_id = reporte.sucursal_id
    data.fecha_reporte = reporte.fecha_reporte
    data.total_ventas = reporte.total_ventas
    data.total_montos = reporte.total_montos
    data.usuario_id = reporte.usuario_id
    db.commit()
    return JSONResponse(status_code=200, content={'message': 'Reporte modificado'})

@routerReporte.delete('/{id}')
async def delete_reporte(id: int, db: Session= Depends(get_db)):
    db=SessionLocal()
    data=db.query(models.Reporte).filter(models.Reporte.id==id).first()
    if not data: 
        return JSONResponse(status_code=404, content={'message': 'Reporte no encontrado'})
    db.delete(data)
    db.commit()
    return JSONResponse(content={'message': 'Se ha eliminado el reporte', 'reporte': jsonable_encoder(data)})