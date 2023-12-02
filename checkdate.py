from datetime import datetime, timedelta

class DateChecker:
    @staticmethod
    def checkdate(date_str):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            today = datetime.now()
            # Verificar que la fecha no sea mayor que la fecha de hoy
            if date <= today:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def checkdateEntidad(date_str):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            today = datetime.now()
            # Verificar que la fecha no sea menor que la fecha de hoy
            if date >= today:
                return True
            else:
                return False
        except ValueError:
            return False