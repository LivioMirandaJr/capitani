from datetime import datetime

from msgspec import Struct, field


class Pricing(Struct):
    amount: float
    currency: str


class Availability(Struct):
    quantity: int
    timestamp: datetime


class Product(Struct):
    id: str
    name: str
    description: str
    pricing: Pricing
    availability: Availability
    category: str
