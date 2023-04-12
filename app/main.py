from fastapi import FastAPI
from api.product.views import router_product
from api.users.views import router_user
from api.employee.views import router_employee
from api.manufacturer.views import router_manufacturer

import uvicorn

app = FastAPI()
app.include_router(router_product)
app.include_router(router_user)
app.include_router(router_employee)
app.include_router(router_manufacturer)


@app.get("/")
def root():
    return {"message": "Hello FAST_API"}


uvicorn.run(app, host="0.0.0.0", port=80)
