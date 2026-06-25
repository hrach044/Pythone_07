from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool: ...

    @abstractmethod
    def ingest(self, data: Any) -> None: ...

    def output(self) -> tuple[int, str]:
        rank = self._total_processed - len(self._storage)
        value = self._storage.pop(0)
        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(str(item))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for x in data:
                if not isinstance(x, str):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(item)
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(f"{item['log_level']}: {item['log_message']}")
            self._total_processed += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===", end="\n\n")

    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest('foo')
    except ValueError as e:
        print(f" Got exception: {e}")
    num.ingest([1, 2, 3, 4, 5])
    print(" Processing data: [1, 2, 3, 4, 5]")
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f" Trying to validate input '42': {txt.validate(42)}")
    txt.ingest(['Hello', 'Nexus', 'World'])
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    print(" Extracting 1 value...")
    rank, value = txt.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    log.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    print(" Processing data : "
          "[{'log_level': 'NOTICE', 'log_message': 'Connection to server'},"
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")
