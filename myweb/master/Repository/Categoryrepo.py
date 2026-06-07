from django.db import connection

class CategoryRepo:
    def getAll(self):
        with connection.cursor() as cursor:
            cursor.execute(
                "select id,cname from category"
            )
            return cursor.fetchall()