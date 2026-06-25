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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None: ...


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
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            total = proc._total_processed
            remaining = len(proc._storage)
            print(f"{name}: total {total} items processed,"
                  f" remaining {remaining} on processor")
        print("")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(min(nb, len(proc._storage))):
                collected.append(proc.output())
            if collected:
                plugin.process_output(collected)


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for _, value in data:
            values.append(value)
        print("CSV Output:")
        print(",".join(values))


class JsonExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for rank, value in data:
            values.append(str(f'"item_{rank}": "{value}"'))
        print("JSON Output:")
        print("{" + ", ".join(values) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch = ["Hello world", [3.14, -1, 2.71], [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
            ], 42, ["Hi", "five"],
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CsvExportPlugin())

    ds.print_processors_stats()

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                  [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                   {'log_level': 'NOTICE',
                    'log_message': 'Certificateexpires in 10 days'}],
                  [32, 42, 64, 84, 128, 168], 'World hello'
              ]
    print(f"Send another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a json plugin:")
    ds.output_pipeline(5, JsonExportPlugin())

    ds.print_processors_stats()
