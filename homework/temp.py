import models

milk = models.Product("Молоко", 40, "Молочко отличное", 2)
beer = models.Product("Пиво",70,"Пивко ого-го",2)
bread = models.Product("Хлеб",30,"ХЛЕП",2)

cart_1 = models.Cart()
cart_2 = models.Cart()

cart_1.add_product(beer,1)
cart_1.add_product(milk,2)
cart_1.add_product(bread,1)


print(cart_1.buy())

# print(cart_1.get_total_price())

# for product, quantity in cart_1.products.items():
#     print(f"ДО удаления {product.name} кол-во: {quantity}")
# cart_1.clear()
# for product, quantity in cart_1.products.items():
#     print(f"После удаления {product.name} стало: {quantity}")



