from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool: ...

    @abstractmethod
    def ingest(self, data: typing.Any) -> None: ...

    def output(self) -> tuple[int, str]:
        rank = self._total_processed - len(self._storage)
        value = self._storage.pop(0)
        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for x in data:
                if not isinstance(x, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(str(item))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for x in data:
                if not isinstance(x, str):
                    return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(item)
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return False
            return True
        if isinstance(data, list):
            for x in data:
                for k, v in x.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(f"{item['log_level']}: {item['log_message']}")
            self._total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            check = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    check = True
                    break
            if not check:
                print(f"DataStream error - Can't"
                      f" process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            total = proc._total_processed
            remaining = len(proc._storage)
            print(f"{name}: total {total} items processed,"
                  f" remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    ds.register_processor(NumericProcessor())
    batch = ["Hello world", [3.14, -1, 2.71], [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
            ], 42, ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nConsume some elements from the "
          "data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        ds._processors[0].output()
    for _ in range(2):
        ds._processors[1].output()
    ds._processors[2].output()
    ds.print_processors_stats()
