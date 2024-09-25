import random
import time
from datetime import datetime

class SensorEmulator:
    def __init__(self, interval, metric_name, unit):
        self.interval = interval
        self.metric_name = metric_name
        self.unit = unit
        self.values = []
        self.start_time = datetime.now()

    def generate_value(self):
        return random.uniform(self.interval[0], self.interval[1])

    def save_to_file(self, value):
        with open(f"{self.metric_name}_data.csv", "a") as file:
            file.write(f"{datetime.now()},{self.metric_name},{value},{self.unit}\n")

    def run(self):
        while True:
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

if __name__ == "__main__":
    # Пример использования
    interval = (20, 30)  # Интервал значений (например, температура от 20 до 30 градусов)
    metric_name = "temperature"  # Название метрики
    unit = "Celsius"  # Единица измерения

    sensor = SensorEmulator(interval, metric_name, unit)
    sensor.run()


