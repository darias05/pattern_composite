from abc import ABC, abstractmethod

# Subclase abstracta de la clase ABC
class Product(ABC):
    # Toma dos argumentos en su constructor (name, price)
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    # El decorador @property permite definir los captadores para
    # los campos nombre y precio
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    # El decorador @abstractmethod permite definir un metodo abstracto en una
    # clase abstracta la cual no tiene implementacion,
    # pero debe ser implementada por cualquier clase
    # que herede de la clase abstracta Product

    @abstractmethod
    def display(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass

# Se define la clase Package de la clase abstracta Product
class Package(Product):
    # Toma el argumento name del constructor, el price se define en 0
    # y se le agregan el atributo items
    def __init__(self, name):
        super().__init__(name, 0)
        self._items = []
        
    # Se crea el metodo que permite añadir items a los Package
    def add_item(self, item):
        self._items.append(item)
    
    # Se crea el metodo abstracto definido en la clase abstracta Product 
    # para poder listar los items que estan dentro del Package
    def display(self):
        print(f"Package: {self.name}")
        for item in self._items:
            item.display()
    
    # Se crea el metodo abstracto definido en la clase abstracta Product 
    # para poder obtener la suma de todos los precios de los items
    # que estan dentro del Package
    def get_price(self):
        return sum(item.get_price() for item in self._items)
    
# Se define la clase SingleItem de la clase abstracta Product
class SingleItem(Product):
    # Toma el argumento name y price del constructor
    # para imprimir el producto con el metodo abstracto display
    # definido por la clase abstracta Product
    def display(self):
        print(f"Product: {self.name} - ${self.price}")
        
    # Retorna el precio del SingleItem por medio de la clase abstracta
    # get_price definida por la clase abstracta Product
    def get_price(self):
        return self.price

hammer = SingleItem("Hammer", 15000)
package1 = Package("Package 1")
package1.add_item(hammer)

cellPhone = SingleItem("Cell phone", 4600000)
headphones = SingleItem("Headphones", 500000)
package2 = Package("Package 2")
package2.add_item(cellPhone)
package2.add_item(headphones)

phoneCharger = SingleItem("Phone charger", 110000)
package3 = Package("Package 3")
package3.add_item(phoneCharger)

package4 = Package("Package 4")
package4.add_item(package2)
package4.add_item(package3)

bill = SingleItem("Bill", 0)

shipping_package = Package("Fedex")
shipping_package.add_item(package1)
shipping_package.add_item(package4)
shipping_package.add_item(bill)

print("\nshipping_package.display()\n")
shipping_package.display()
print("\nshipping_package.get_price()\n")
print(f'Valor total en articulos del envio = ${shipping_package.get_price()}')