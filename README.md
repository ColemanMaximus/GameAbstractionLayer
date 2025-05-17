# RPG Game Abstraction Layer
Modules to handle game systems usually found in RPG games, such as player data, accounts, inventories, items, maps and entities. Follows an OOP approach to become extensible, and to create your own game wrappers.

### Components - (In Progress)
 - **Models**
	 - Account - Represents a user account containing a collection of characters.
	 - Character
	 - Item
		 - InventoryItem
			 - **ShopItem**
	 - NPC
       - **NpcData**
	 - Entity
		 - **Player**
		 - **NPC**
	 - Map
		 - **Map Cell**
	- Currency
		- **TradebleCurrency**
	

 - **Controllers**
	 - Instances
		 - **MapInstance**
		 - **MapCellInstance**
	- Interface
		- **Shop**
 - **Containers**
	 - Inventory
		 - **PlayerInventory**
		 - **ShopInventory**
