from flask import Flask, request, jsonify
import json

app = Flask(__name__)

FILE_PATH = "tasks.json"
VALID_STATES = ["Por Hacer", "En Progreso", "Completada"]



def read_tasks():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def write_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    try:
        tasks = read_tasks()
        estado = request.args.get("estado")

        if estado:
            tasks = [task for task in tasks if task["estado"] == estado]

        return jsonify(tasks), 200

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/tasks", methods=["POST"])
def create_task():
    try:
        raw_data = request.data.decode("utf-8")

        if not raw_data:
            raise ValueError("request body is empty")

        try:
            data = json.loads(raw_data)
        except json.JSONDecodeError:
            raise ValueError("request body must be valid JSON")

        tasks = read_tasks()

        if "id" not in data:
            raise ValueError("id is required")
        if "titulo" not in data:
            raise ValueError("title is required")
        if "descripcion" not in data:
            raise ValueError("description is required")
        if "estado" not in data:
            raise ValueError("state is required")
        if data["estado"] not in VALID_STATES:
            raise ValueError("invalid state")

        for task in tasks:
            if task["id"] == data["id"]:
                raise ValueError("task id already exists")

        tasks.append(data)
        write_tasks(tasks)

        return jsonify(data), 201

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500



@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        raw_data = request.data.decode("utf-8")

        if not raw_data:
            raise ValueError("request body is empty")

        try:
            data = json.loads(raw_data)
        except json.JSONDecodeError:
            raise ValueError("request body must be valid JSON")

        tasks = read_tasks()

        for task in tasks:
            if task["id"] == task_id:
                if "titulo" in data:
                    task["titulo"] = data["titulo"]
                if "descripcion" in data:
                    task["descripcion"] = data["descripcion"]
                if "estado" in data:
                    if data["estado"] not in VALID_STATES:
                        raise ValueError("invalid state")
                    task["estado"] = data["estado"]

                write_tasks(tasks)
                return jsonify(task), 200

        raise ValueError("task not found")

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        tasks = read_tasks()
        new_tasks = [task for task in tasks if task["id"] != task_id]

        if len(new_tasks) == len(tasks):
            raise ValueError("task not found")

        write_tasks(new_tasks)
        return jsonify(message="task deleted"), 200

    except ValueError as ex:
        return jsonify(error=str(ex)), 400

    except Exception as ex:
        return jsonify(error=str(ex)), 500


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
