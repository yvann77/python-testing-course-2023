class Menu:
    def __init__(self):
        self.menu = {}

    def add_menu_item(self, restaurant, item_name, description, price):
        if not restaurant in self.menu:
            self.menu[restaurant] = []

        self.menu[restaurant].append({
            'item_name': item_name,
            'description': description,
            'price': price
        })
        return f"Menu item added for {restaurant}."

    def get_menu(self, restaurant):
        if restaurant not in self.menu:
            return "Menu not found."

        return self.menu[restaurant]

    def update_menu_item(self, restaurant, item_name, new_description, new_price):
        if restaurant not in self.menu:
            return "Menu not found."

        for menu_item in self.menu[restaurant]:
            if menu_item['item_name'] == item_name:
                menu_item['description'] = new_description
                menu_item['price'] = new_price
                return f"Menu item updated for {restaurant}."

        return "Menu item not found."

    def delete_menu_item(self, restaurant, item_name):
        if restaurant not in self.menu:
            return "Menu not found."

        for i, menu_item in enumerate(self.menu[restaurant]):
            if menu_item['item_name'] == item_name:
                del self.menu[restaurant][i]
                return f"Menu item deleted for {restaurant}."

        return "Menu item not found."
