from dataclasses import dataclass

@dataclass
class DataHandler:
    start: str | None = None
    end: str | None = None

    def set_start(self, value: str):
        self.start = value

    def set_end(self, value: str):
        self.end = value

    def __str__(self) -> str:
        return f"{self.start} | {self.end}"

a = DataHandler()
a.set_start("Hello")
print(a)
