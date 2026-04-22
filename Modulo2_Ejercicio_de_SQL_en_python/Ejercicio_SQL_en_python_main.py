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
        if "car_status" not in data or not data["car_status"].strip():
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


@app.route("/cars/<int:car_id>", methods=["PUT"])
def change_car_status(car_id):
    try:
        data = request.get_json()

        if data is None:
            raise ValueError("Request body must be valid JSON")
        
        if "car_status" not in data or not data["car_status"].strip():
            raise ValueError("Car status is required")

        if not db_manager.car_exists(car_id):
            return jsonify(error="Car not found"), 404

        new_status = data["car_status"]

        db_manager.change_car_status(car_id, new_status)

        return jsonify(
            message="Car status updated successfully",
            car_id=car_id,
            car_status=new_status
        ), 200

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/users/<int:user_id>", methods=["PUT"])
def change_user_status(user_id):
    data = request.get_json()
    try:

        if data is None:
            raise ValueError("Request must be valid JSON")

        if "account_status" not in data:
            raise ValueError("Account status is required")

        if not db_manager.user_exists(user_id):
            return jsonify(error="User not found"), 404

        new_status = data["account_status"]

        db_manager.change_user_status(user_id, new_status)

        return jsonify(
            message="User status updated successfully",
            user_id=user_id,
            user_status=new_status
        ), 200

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/rentals/<int:rental_id>/complete", methods=["PUT"])
def complete_rental(rental_id):
    try:

        if not db_manager.rental_exists(rental_id):
            return jsonify(error="Rental not found"), 404

        db_manager.complete_rental(rental_id)

        return jsonify(
            message="Rental completed successfully",
            rental_id=rental_id,
            car_status="Completed"
        ), 200

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/rentals/<int:rental_id>", methods=["PUT"])
def change_rented_car_status(rental_id):
    data = request.get_json()
    try:

        if data is None:
            raise ValueError("Request must be valid JSON")
        if "rent_status" not in data or not data["rent_status"]:
            raise ValueError("Rent status is required")

        if not db_manager.rental_exists(rental_id):
            return jsonify(error="Rental not found"), 404

        new_status = data["rent_status"]

        db_manager.change_rent_status(rental_id, new_status)

        return jsonify(
            message="Rental status updated successfully",
            rental_id=rental_id,
            rent_status=new_status
        ), 200
    
    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500

@app.route("/users/<int:user_id>/delinquent", methods=["PUT"])
def flag_user(user_id):
    try:

        if not db_manager.user_exists(user_id):
            return jsonify(error="User no found"), 404

        db_manager.flag_user_as_delinquent(user_id)

        return jsonify(
            message="User flagged as delinquent",
            user_id=user_id
        ), 200

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