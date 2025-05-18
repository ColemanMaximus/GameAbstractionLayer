from uuid import uuid4

from models.account import Account
from models.currency import Currency
from models.items import InventoryItem, Item
from models.shop import Shop, ShopItem

if __name__ == "__main__":
    # Creates a user account with an example email.
    # This will be replaced in the near future to a proper auth service.
    account = Account(email="example@email.com")
    char = account.create_character(name="Frexel")

    # Create items which can be used in inventories.
    sword_item = Item(
        id=1,
        name="Warrior Sword",
        description="Sword for a warrior!"
    )
    # Converts an item into one which can be used in inventory objects.
    inventory_item = InventoryItem(inv_id=1, item=sword_item)

    # Example of a shop, with an inventory and items for sale.
    # Creating a currency which the shop uses to handle item purchases.
    shop_currency = Currency("Gold", "g")
    shop = Shop(id=str(uuid4()), name="Weapon Shop")
    # Converts an inventory item into a shop item, with a
    # defined currency and price.
    shop_item = ShopItem(
        item=inventory_item,
        currency=shop_currency,
        price=150
    )

    # Adds a ShopItem to the shop's inventory
    shop.inventory.add(shop_item)
    shop.buy_item(char, shop_item)
