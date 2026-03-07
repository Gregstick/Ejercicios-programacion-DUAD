from Ejercicio_de_SQL_en_Pyhton_db import PgManager
from flask import Flask, request, jsonify

app = Flask(__name__)

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="Luna19patch!",
    host="localhost"
)

@app.route("/", methods=["GET"])
def health():
    return jsonify(message="API running"), 200


@app.route("/users", methods=["POST"])
def add_new_user():
    try:
        data = request.get_json()

        if data is None:
            raise ValueError("Request body must be valid JSON")

        if "user_name" not in data or not data["user_name"].strip():
            raise ValueError("User name is required")
        if "email" not in data or not data["email"].strip():
            raise ValueError("Email is required")
        if "username" not in data or not data["username"].strip():
            raise ValueError("username is required")
        if "password" not in data or not data["password"].strip():
            raise ValueError("Password is required")
        if "date_of_birth" not in data or not data["date_of_birth"].strip():
            raise ValueError("Date of birth is required")
        if "account_status" not in data or not data["account_status"].strip():
            raise ValueError("Account status is required")

        db_manager.add_user(data)

        return jsonify(data), 201

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500



@app.route("/cars", methods=["POST"])
def add_car():
    try:
        data = request.get_json()

        if data is None:
            raise ValueError("Request body must be valid JSON")

        if "make" not in data or not data["make"].strip():
            raise ValueError("Make is required")
        if "model" not in data or not data["model"].strip():
            raise ValueError("Model is required")
        if "manufacturing_year" not in data or not data["manufacturing_year"].strip():
            raise ValueError("Manufacturing year is required")
        if "car_status" not in data or not data["car_status"].strip:
            raise ValueError("Car status is required")

        db_manager.add_car(data)

        return jsonify(data), 201

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/rentals", methods=["POST"])
def add_rental():
    try:
        data = request.get_json()

        if data is None:
            raise ValueError("Request body must be valid JSON")
        
        if "users_id" not in data or not data["users_id"]:
            raise ValueError("User Id is required")
        if "cars_id" not in data or not data["cars_id"]:
            raise ValueError("Cars Id is required")
        if "rent_status" not in data or not data["rent_status"]:
            raise ValueError("Rent status is required")
        
        if not db_manager.user_exists(data["users_id"]):
            raise ValueError("User does not exist")

        if not db_manager.car_exists(data["cars_id"]):
            raise ValueError("Car does not exist")
        
        db_manager.add_rental(data)

        return jsonify(data), 201

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/change_car_status", methods=["PUT"])
def change_car_status():
    try:
        data = request.get_json()

        if data is None:
            raise ValueError("Request body must be valid JSON")
        
        if "car_status" not in data or not data["car_status"]:
            raise ValueError("Car status is required")
        if "id" not in data:
            raise ValueError("Car Id is required")
        
        car_id = data["id"]
        new_status = data["car_status"]

        db_manager.change_car_status(car_id, new_status)

        return jsonify(data), 200

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/change_user_status", methods=["PUT"])
def change_user_status():
    data = request.get_json()
    try:

        if data is None:
            raise ValueError("Request must be valid JSON")

        if "id" not in data:
            raise ValueError("Id is required")
        if "account_status" not in data:
            raise ValueError("Account status is required")

        user_id = data["id"]
        new_status = data["account_status"]

        db_manager.change_user_status(user_id, new_status)

        return jsonify(data), 200

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/complete_rental", methods=["PUT"])
def complete_rental():
    try:
        data = request.get_json()

        if data is None:
            raise ValueError("Request body must be valid JSON")

        if "cars_id" not in data:
            raise ValueError("Cars id is required")

        cars_id = data["cars_id"]

        db_manager.complete_rental(cars_id)

        return jsonify(
            message="Rental completed successfully",
            cars_id=cars_id,
            car_status="Completed"
        ), 200

    except ValueError as ex:
        return jsonify(error=str(ex)), 400
    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/change_rented_car_status", methods=["PUT"])
def change_rented_car_status():
    data = request.get_json()
    try:

        if data is None:
            raise ValueError("Request must be valid JSON")
        if "id" not in data:
            raise ValueError("Id is required")
        if "rent_status" not in data or not data["rent_status"]:
            raise ValueError("Rent status is required")

        rent_id = data["id"]
        new_status = data["rent_status"]

        db_manager.change_rent_status(rent_id, new_status)

        return jsonify(data), 200
    
    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500

@app.route("/flag_user_as_delinquent", methods=["PUT"])
def flag_user():
    data = request.get_json()
    try:

        if data is None:
            raise ValueError("Request must to a valid JSON")
        if "id" not in data:
            raise ValueError("Id is required")
        
        user_id = data["id"]

        db_manager.flag_user_as_delinquent(user_id)

        return jsonify(data), 200

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/users", methods=["GET"])
def get_users():

    filters = request.args 

    users = db_manager.list_users(filters)

    return jsonify(users), 200


@app.route("/cars", methods=["GET"])
def get_cars():

    filters = request.args.to_dict()

    cars = db_manager.list_cars(filters)

    return jsonify(cars), 200


@app.route("/rentals", methods=["GET"])
def get_rents():

    filters = request.args.to_dict()

    rents = db_manager.list_rents(filters)

    return jsonify(rents), 200



if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)