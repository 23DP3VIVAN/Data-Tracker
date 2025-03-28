from main import StepTracker

tracker = StepTracker()

print("test")

# Pievieno soļus
tracker.add_steps(5000)
tracker.add_steps(7000, '2025-03-27')

# Atjaunina soļus
tracker.update_steps(8000, '2025-03-27')

# Dzēš soļus
tracker.delete_steps('2025-03-26')

# Aprēķina vidējo soļu skaitu par nedēļu
avg_steps_week = tracker.calculate_average_steps('week')
print(f"Vidējais soļu skaits nedēļā: {avg_steps_week}")

# Eksportē datus
tracker.export_data('steps_data.json')

# Importē datus
tracker.import_data('steps_data.json')

# Ģenerē pārskatu
tracker.generate_report('month')
