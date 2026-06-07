from django.db import connection


class productRepo:

    def addProduct(self, product):

        data = [
            product.pname,
            product.description,
            product.price,
            product.image,
            product.cid,
            product.plant_size,
            product.plant_weight,
            product.soil_type,
        ]

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO product
                (
                    pname,
                    description,
                    price,
                    image,
                    cid,
                    plant_size,
                    plant_weight,
                    soil_type
                )
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                data,
            )

        connection.commit()

        return f"{product.pname} added successfully"

    def getAllProducts(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT id, pname, description, price, image, cid, plant_size, plant_weight, soil_type FROM product """
            )
            products = cursor.fetchall()
        return products

    def getProductById(self, id):

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT id,pname,description,price,image,cid,plant_size,plant_weight,soil_type FROM product WHERE id=%s""",
                [id],
            )
            product = cursor.fetchone()
        return product

    def updateProduct(self, product):

        data = [product.pname, product.description, product.price, product.id]

        with connection.cursor() as cursor:
            cursor.execute(
                """UPDATE product SET pname=%s, description=%s ,price=%s WHERE id=%s""",
                data,
            )

        connection.commit()

        return "Product Updated Successfully"

    def deleteProduct(self, id):

        with connection.cursor() as cursor:

            cursor.execute("""DELETE FROM product WHERE id=%s """, [id])
        connection.commit()
        return "Deleted Successfully"

    def getAllProducts(self):

        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT *
                FROM product
            """)

            return cursor.fetchall()

    def getProductsByIds(self, ids):
        if len(ids) == 0:
            return []
        placeholders = ",".join(["%s"] * len(ids))
        query = f""" SELECT * FROM product WHERE id IN ({placeholders})"""
        with connection.cursor() as cursor:
            cursor.execute(query, ids)
            return cursor.fetchall()

    def searchProducts(self, keyword):

        return self.repo.searchProducts(keyword)

    def searchProducts(self, keyword):
        query = """SELECT * FROM product WHERE pname LIKE %s """
        with connection.cursor() as cursor:
            cursor.execute(query, ["%" + keyword + "%"])
            return cursor.fetchall()

    def getProductsByCategory(self, category_id):
        query = """SELECT * FROM product WHERE cid = %s"""
        with connection.cursor() as cursor:
            cursor.execute(query, [category_id])
            return cursor.fetchall()

    def searchProductsByCategory(self, keyword, category):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM product WHERE pname LIKE %s AND cid = %s""",['%' + keyword + '%', category])
            return cursor.fetchall()