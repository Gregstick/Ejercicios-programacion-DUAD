class Person:
    def set_name(self, name):
        self.name = name

    def show_name(self):
        print("Nombre:", self.name)


class Worker:
    def set_job(self, job):
        self.job = job

    def show_job(self):
        print("Trabajo:", self.job)


class Student:
    def set_career(self, career):
        self.career = career

    def show_career(self):
        print("Carrera:", self.career)

class WorkingStudent(Person, Worker, Student):
    def show_info(self):
        print("Información del estudiante trabajador:")
        self.show_name()
        self.show_job()
        self.show_career()


person1 = WorkingStudent()
person1.set_name("Greg")
person1.set_job("Desarrollador")
person1.set_career("Ingeniería en Sistemas")

person1.show_info()