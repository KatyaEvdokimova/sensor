import random
import time
from datetime import datetime, timedelta
import sys

class SensorEmulator:
    def __init__(self, interval, metric_name, unit, duration_minutes):
        self.interval = interval
        self.metric_name = metric_name
        self.unit = unit
        self.duration_minutes = duration_minutes
        self.values = []
        self.start_time = datetime.now()

    def generate_value(self):
        return random.uniform(self.interval[0], self.interval[1])

    def save_to_file(self, value):
        try:
            with open(f"{self.metric_name}_data.csv", "a") as file:
                file.write(f"{datetime.now()},{self.metric_name},{value},{self.unit}\n")
        except IOError as e:
            print(f"Ошибка при записи в файл: {e}")

    def run(self):
        end_time = self.start_time + timedelta(minutes=self.duration_minutes)
        while datetime.now() < end_time:
            current_time = datetime.now()
            value = self.generate_value()
            self.values.append(value)

            # Если прошла минута с момента начала записи
            if (current_time - self.start_time).total_seconds() >= 60:
                average_value = sum(self.values) / len(self.values)
                self.save_to_file(average_value)
                self.values = []
                self.start_time = current_time

            time.sleep(1)


        if self.values:
            final_average_value = sum(self.values) / len(self.values)
            self.save_to_file(final_average_value)

if __name__ == "__main__":
    try:
        interval_min = float(input("Введите минимальное значение интервала: "))
        interval_max = float(input("Введите максимальное значение интервала: "))
        metric_name = input("Введите название метрики: ")
        unit = input("Введите единицу измерения: ")
        duration_minutes = int(input("Введите количество минут работы программы: "))
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        sys.exit(1)

    interval = (interval_min, interval_max)
    sensor = SensorEmulator(interval, metric_name, unit, duration_minutes)
    sensor.run()
