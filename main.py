import json
from datetime import datetime, timedelta
import statistics

class StepTracker:
    def __init__(self):
        self.data = {}

    def add_steps(self, steps, date=None):
        if date is None:
            date = datetime.today().strftime('%Y-%m-%d')
        self.data[date] = steps
        print(f"Soļi {steps} pievienoti datumam {date}.")

    def update_steps(self, steps, date):
        if date in self.data:
            self.data[date] = steps
            print(f"Soļu skaits datumā {date} ir atjaunināts uz {steps}.")
        else:
            print(f"Nav datu par šo datumu: {date}.")

    def delete_steps(self, date):
        if date in self.data:
            del self.data[date]
            print(f"Soļi no datuma {date} tika izdzēsti.")
        else:
            print(f"Nav datu par šo datumu: {date}.")

    def calculate_average_steps(self, period='day'):
        if period == 'day':
            return statistics.mean(self.data.values()) if self.data else 0
        elif period == 'week':
            week_data = [self.data[date] for date in self.data if datetime.strptime(date, '%Y-%m-%d') > datetime.today() - timedelta(weeks=1)]
            return statistics.mean(week_data) if week_data else 0
        elif period == 'month':
            month_data = [self.data[date] for date in self.data if datetime.strptime(date, '%Y-%m-%d') > datetime.today() - timedelta(days=30)]
            return statistics.mean(month_data) if month_data else 0
        elif period == 'year':
            year_data = [self.data[date] for date in self.data if datetime.strptime(date, '%Y-%m-%d') > datetime.today() - timedelta(days=365)]
            return statistics.mean(year_data) if year_data else 0

    def export_data(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f)
        print(f"Dati eksportēti uz {filename}.")

    def import_data(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)
        print(f"Dati importēti no {filename}.")
