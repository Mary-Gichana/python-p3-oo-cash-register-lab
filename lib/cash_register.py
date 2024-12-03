#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = {"items": [], "total": 0.0}

    def add_item(self, title, price, quantity=1):
        
        
        self.total += price * quantity
        
        
        self.items.extend([title] * quantity)

        
        self.last_transaction = {"items": [title] * quantity, "total": price * quantity}

    def apply_discount(self):
      
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        
        self.total -= self.last_transaction["total"]

        
        for item in self.last_transaction["items"]:
            if item in self.items:
                self.items.remove(item)

        
        self.last_transaction = {"items": [], "total": 0.0}

  
