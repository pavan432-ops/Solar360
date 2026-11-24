
from fastapi import FastAPI
from customer_routes import router as customer_router
from lead_routes import router as lead_router

app = FastAPI(
    title="Solar360 API",
    description="Customer and Installation Management Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Solar360 API",
        "project": "Solar360",
        "status": "Running"
    }


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Solar360 API is working successfully"
    }


# Register API routers
app.include_router(customer_router)
app.include_router(lead_router)
