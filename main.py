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

    def calculate_average(self, steps_list):
        if steps_list:
            return statistics.mean(steps_list)
        return 0

    def get_steps_for_period(self, period):
        period_data = []
        today = datetime.today()
        if period == 'day':
            period_data = list(self.data.values())
        elif period == 'week':
            for date in self.data:
                if datetime.strptime(date, '%Y-%m-%d') > today - timedelta(weeks=1):
                    period_data.append(self.data[date])
        elif period == 'month':
            for date in self.data:
                if datetime.strptime(date, '%Y-%m-%d') > today - timedelta(days=30):
                    period_data.append(self.data[date])
        elif period == 'year':
            for date in self.data:
                if datetime.strptime(date, '%Y-%m-%d') > today - timedelta(days=365):
                    period_data.append(self.data[date])
        return period_data

    def calculate_average_steps(self, period='day'):
        period_data = self.get_steps_for_period(period)
        return self.calculate_average(period_data)

    def export_data(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f)
        print(f"Dati eksportēti uz {filename}.")

    def import_data(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)
        print(f"Dati importēti no {filename}.")

    def generate_report(self, period='day'):
        avg_steps = self.calculate_average_steps(period)
        print(f"Vidējais soļu skaits {period}: {avg_steps}")
