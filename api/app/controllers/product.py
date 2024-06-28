import msgspec.json
from litestar import Controller, post

from app.domain.product import Product, ProductDb
from app.lib.kafka import Producer


class ProductController(Controller):
    path = "products"
    tags = ["products"]

    @post()
    async def create_product(self, data: Product) -> dict:
        product = ProductDb()
        product.product_id = data.id
        product.name = data.name
        product.category = data.category
        product.amount = data.pricing.amount
        product.description = data.description
        product.currency = data.pricing.currency
        product.timestamp = data.availability.timestamp
        product.quantity = data.availability.quantity
        async with Producer() as producer:
            await product.save()
            await producer.produce(msgspec.json.encode(data))
        return {"detail": "created"}
