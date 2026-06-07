from django.db import connection

class OrderRepo:

    def addOrder(self, uid, fullname, phone, address, total):

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO orders
                (
                    uid,
                    fullname,
                    phone,
                    address,
                    total
                )
                VALUES
                (%s,%s,%s,%s,%s)
                """,
                [uid, fullname, phone, address, total],
            )

            connection.commit()

            return cursor.lastrowid

    def addOrderItem(self, order_id, product_id, quantity, price):

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO order_items
                (
                    order_id,
                    product_id,
                    quantity,
                    price
                )
                VALUES
                (%s,%s,%s,%s)
                """,
                [order_id, product_id, quantity, price],
            )

            connection.commit()

    def getAllOrders(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM orders ORDER BY id DESC""")
            return cursor.fetchall()
        
    def updateStatus(self, order_id, status):
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE orders SET status=%s WHERE id=%s""",[status, order_id])
        connection.commit()