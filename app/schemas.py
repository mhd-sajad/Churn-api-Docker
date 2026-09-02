from pydantic import BaseModel, Field


class CustomerInput(BaseModel):
    age: int = Field(..., gt=17, description="Customer age (must be > 17)")
    tenure: int = Field(..., ge=0, description="Months the customer has been with the company")
    monthly_charges: float = Field(..., gt=0, description="Monthly billing amount in USD")
    num_products: int = Field(..., ge=1, le=10, description="Number of products subscribed (1–10)")
    has_internet: int = Field(..., ge=0, le=1, description="1 = Has internet service, 0 = Does not")
