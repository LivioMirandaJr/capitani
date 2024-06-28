from datetime import datetime

from msgspec import Struct
from piccolo.columns import Text, Integer, Float, Date
from piccolo.table import Table

from piccolo_conf import DB


class ProductDb(Table, db=DB, tablename="product"):
    product_id: str = Text()
    name: str = Text()
    description: str = Text()
    amount: str = Float()
    currency: str = Text()
    quantity: str = Integer()
    timestamp: str = Date()
    category: str = Text()


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
