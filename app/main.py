from fastapi import FastAPI
from app.routers import boleta_factura, reporte
from .database import engine, Base

app=FastAPI(
    title='Ferremas',
    description='Api que presta servicios a una ferreteria',
    version='0.0.1'
)

Base.metadata.create_all(bind=engine)

app.include_router(boleta_factura.routerBoletaFactura)
app.include_router(reporte.routerReporte)

