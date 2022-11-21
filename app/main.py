from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.client import customer, supplier, customerAddress, location, resource
from .routers.client import material, product, inventory, variant, batch, taxRate, webhook
from .routers.client import salesOrder, salesOrderRow, salesOrderAddress, purchaseOrder, mfgOrder, stocktake

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API for version v1
v1 = FastAPI()

v1.include_router(customer.router)
v1.include_router(customerAddress.router)
v1.include_router(location.router)
v1.include_router(material.router)
v1.include_router(product.router)
v1.include_router(taxRate.router)
v1.include_router(variant.router)
v1.include_router(inventory.router)
v1.include_router(batch.router)
v1.include_router(supplier.router)
v1.include_router(salesOrder.router)
v1.include_router(salesOrderRow.router)
v1.include_router(salesOrderAddress.router)
v1.include_router(mfgOrder.router)

v1.include_router(purchaseOrder.router)






app.mount("/api/v1", v1)
