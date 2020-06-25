from django.apps import AppConfig

class EmployeesAppConfig(AppConfig):
    name = 'Employees'

    def ready(self):
        import employees.signals
