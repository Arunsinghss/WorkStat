from django.apps import AppConfig

class EmployeesAppConfig(AppConfig):
    name = 'employee'

    def ready(self):
        import employee.signals
