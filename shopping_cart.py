class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=0):
        self._items = []
        self._employee_discount = employee_discount
        self._total = 0
       
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, items):
        self._items = items
    @property
    def employee_discount(self):
        return self._employee_discount
    @employee_discount.setter
    def employee_discount(self, employee_discount):
        self._employee_discount = employee_discount
    @property
    def total(self):
        return self._total 
    @total.setter
    def total(self, total):
        self._total = total
        
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price, "quantity": quantity})
            self.total += price * quantity
            return self.total
    
    def mean_item_price(self):
        total_quantity = sum(i['quantity'] for i in self.items)
        mean = self.total/total_quantity
        return mean
    

    
    def median_item_price(self):
        sorted_items = sorted(self.items, key = lambda x: x['price'])
        length = len(self.items)
        if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (sorted_items[mid_one] + sorted_items[mid_two])/2
            return median
        mid = int(length/2)
        return sorted_items[mid]['price']
    
    def apply_discount(self):
        if self.employee_discount > 0:
            self.total -= (self.employee_discount/100)*self.total
            return self.total
        else:
            return print("Sorry, there is no discount to apply to your cart :(")
   

    def get_attr(self, item, attr):
        return item[attr]

    def item_names(self):
        names = [self.get_attr(item, "name") for item in self.items]
        return names

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']
            

            
            
        
