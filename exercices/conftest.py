import pytest
from menu import Menu

@pytest.fixture
def menu():
    menu_instance = Menu()

    # Pre-populate the menu with some sample data
    menu_instance.add_menu_item("Le Petit Bistro", "Coq au Vin", "A classic French dish of chicken braised in red wine", 19.95)
    menu_instance.add_menu_item("Le Petit Bistro", "Crêpes Suzette", "Delicious thin pancakes flambéed with orange liqueur and butter", 12.95)
    menu_instance.add_menu_item("La Cucina Italiana", "Pizza Margherita", "Traditional Neapolitan pizza with tomato sauce, mozzarella cheese, and basil", 14.95)
    menu_instance.add_menu_item("La Cucina Italiana", "Pasta al Limone", "Light and creamy pasta tossed with lemon juice, butter, and Parmesan cheese", 16.95)

    return menu_instance
