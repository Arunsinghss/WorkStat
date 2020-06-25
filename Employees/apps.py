from django.apps import AppConfig

class EmployeesConfig(AppConfig):
    name = 'Employees'

    def ready(self):
        import Employees.signals
