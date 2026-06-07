from django.db import connection


class UserRepo:

    def saveProfile(self, profile):

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO user_profile
                (
                    user_id,
                    contact,
                    security_question,
                    security_answer
                )
                VALUES(%s,%s,%s,%s)
                """,
                [
                    profile.user_id,
                    profile.contact,
                    profile.security_question,
                    profile.security_answer
                ]
            )

        connection.commit()