"""
基于618 大促打折的项目需求，使用策略模式开发该功能

"""

from collections import namedtuple

Customer = namedtuple('Customer','name is_88vip')
Product = namedtuple('Product','name price')

def vip_discount(order):
    """淘宝88vip 客户95折扣"""

    return order.total() *0.05 if order.customer.is_88vip else 0 

def full_credit_discount(order):
    """没满300 减 40"""

    total = 0
    for item in order.cart:
        total += item.price
    discount = (total //300) * 40
    return discount

def free_one_discount(order):
    """满3件商品，免单最便宜的哪一件"""
    if len(order.cart) >= 3:
        return min([item.price for item in order.cart])
    return 0

class Order:
    def __init__(self,customer,cart,promotion=None):
        """
        订单类
        :param customer (Customer): 订单的顾客
        :param cart (list of Product): 购物车列表
        :param promotion (function,optional): 该订单折扣的计算方法
        """
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        """
        订单优惠前的总金额
        """
        if not hasattr(self,'__total'):
            self.__total = sum(item.price for item in self.cart)
        return self.__total

    def due(self):
        """
        订单优惠后的总金额
        """
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        
        return self.total() - discount

    def __repr__(self):
        fmt = '<订单 总价: {:.2f} 实付: {:.2f}>'
        return fmt.format(self.total(), self.due())


if __name__ == "__main__":
    joe = Customer('John Doe', True)

    cart_A = [Product('banana', 4),
            Product('apple', 10),
            Product('watermellon', 5)]

    print('策略一：为88vip顾客提供5%折扣')
    print(Order(joe, cart_A, vip_discount))

    cart_B = [Product('banana', 630),
            Product('apple', 410)]

    print('策略二：每满300减40活动')
    print(Order(joe, cart_B, full_credit_discount))

    cart_C = [Product('banana', 630),
            Product('apple', 410),
            Product('watermellon', 210)]

    print('策略三：满3件免单最便宜的一件')
    print(Order(joe, cart_C, free_one_discount))