import psycopg

class PgManager():
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection()
        if self.connection:
            self.cursor = self.connection_cursor()
            print("Connection created successfully")


    def create_connection(self):
        try:
            connection=psycopg.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None


    def connection_cursor(self):
        return self.connection.cursor()



    def close_connection(self):
        if self.cursor:
            self.cursor_close()
        if self.connection:
            self.connection_close()
        print("Connection closed")


    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)

        if self.cursor.description:
            return self.cursor.fetchall()

        self.connection.commit()
        return None


    def add_user(self, add_user):
        query = "INSERT INTO lyfter_car_rental.users(user_name, email, username, password, date_of_birth, account_status) VALUES(%s, %s, %s, %s, %s, %s)"

        values = (
            add_user["user_name"],
            add_user["email"],
            add_user["username"],
            add_user["password"],
            add_user["date_of_birth"],
            add_user["account_status"]
        )
    
        self.execute_query(query, values)


    def add_car(self, add_car):
        query = "INSERT INTO lyfter_car_rental.cars(make, model, manufacturing_year, car_status) VALUES(%s, %s, %s, %s)"

        values = (
            add_car["make"],
            add_car["model"],
            add_car["manufacturing_year"],
            add_car["car_status"]
        )

        self.execute_query(query, values)



    def add_rental(self, add_rental):
        query = "INSERT INTO lyfter_car_rental.cars_rented(users_id, cars_id, rent_status) VALUES(%s, %s, %s)"

        values = (
            add_rental["users_id"],
            add_rental["cars_id"],
            add_rental["rent_status"]
        )

        self.execute_query(query, values)



    def change_car_status(self, car_id, new_status):
        query = """
            UPDATE lyfter_car_rental.cars
            SET car_status = %s
            WHERE id = %s
        """

        self.execute_query(query, (new_status, car_id))



    def change_user_status(self, user_id, new_status):
        query = """
            UPDATE lyfter_car_rental.users
            SET account_status = %s
            WHERE id = %s
        """

        self.execute_query(query, (new_status, user_id))



    def complete_rental(self, rent_id):
        get_car_query = """
            SELECT cars_id
            FROM lyfter_car_rental.cars_rented
            WHERE id = %s
        """
        self.cursor.execute(get_car_query, (rent_id,))
        car_id = self.cursor.fetchone()[0]

        update_rent_query = """
            UPDATE lyfter_car_rental.cars_rented
            SET rent_status = 'Completed'
            WHERE id = %s
        """
        self.cursor.execute(update_rent_query, (rent_id,))

        update_car_query = """
            UPDATE lyfter_car_rental.cars
            SET car_status = 'Not Rented'
            WHERE id = %s
        """
        self.cursor.execute(update_car_query, (car_id,))

        self.connection.commit()


    def change_rent_status(self, rent_id, new_status):
        change_rent_status_query = """
            UPDATE lyfter_car_rental.cars_rented
            SET rent_status = %s
            WHERE id = %s
    """

        self.execute_query(change_rent_status_query, (new_status, rent_id))


    def flag_user_as_delinquent(self, user_id):
        flag_user_query = """
            UPDATE lyfter_car_rental.users
            SET account_status = 'Delinquent'
            WHERE id = %s
    """

        self.execute_query(flag_user_query, (user_id,))


    def list_users(self, filters=None):

        base_query = "SELECT * FROM lyfter_car_rental.users"
        params = []

        if filters:
            conditions = []
            for key, value in filters.items():
                conditions.append(f"{key} = %s")
                params.append(value)

            base_query += " WHERE " + " AND ".join(conditions)

        self.cursor.execute(base_query, tuple(params))
        return self.cursor.fetchall()


    def list_cars(self, filters=None):

        base_query = "SELECT * FROM lyfter_car_rental.cars"
        params = []

        if filters:
            conditions = []
            for key, value in filters.items():
                conditions.append(f"{key} = %s")
                params.append(value)

            base_query += " WHERE " + " AND ".join(conditions)

        self.cursor.execute(base_query, tuple(params))
        return self.cursor.fetchall()


    def list_rents(self, filters=None):

        base_query = "SELECT * FROM lyfter_car_rental.cars_rented"
        params = []

        if filters:
            conditions = []
            for key, value in filters.items():
                conditions.append(f"{key} = %s")
                params.append(value)

            base_query += " WHERE " + " AND ".join(conditions)

        self.cursor.execute(base_query, tuple(params))
        return self.cursor.fetchall()

    def user_exists(self, user_id):
        query = "SELECT id FROM lyfter_car_rental.users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone() is not None


    def car_exists(self, car_id):
        query = "SELECT id FROM lyfter_car_rental.cars WHERE id = %s"
        self.cursor.execute(query, (car_id,))
        return self.cursor.fetchone() is not None


    def rental_exists(self, rental_id):
        query = "SELECT id FROM lyfter_car_rental.cars_rented WHERE id = %s"
        self.cursor.execute(query, (rental_id,))
        return self.cursor.fetchone() is not None