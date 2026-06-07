from master.Repository.OrderRepo import OrderRepo


class OrderService:

    def __init__(self):

        self.repo = OrderRepo()

    def addOrder(self, uid, fullname, phone, address, total):

        return self.repo.addOrder(uid, fullname, phone, address, total)

    def addOrderItem(self, order_id, product_id, quantity, price):

        self.repo.addOrderItem(order_id, product_id, quantity, price)

    def getAllOrders(self):

        return self.repo.getAllOrders()
    
    def updateStatus(self, order_id, status):

        self.repo.updateStatus(order_id, status)