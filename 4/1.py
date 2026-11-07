from dataclasses import dataclass

@dataclass
class DataHandler:
    start: str | None = None
    end: str | None = None

    def set_value(self, key: str, value: str):
        if key == "start":
            self.start = value
        elif key == "end":
            self.end = value
        else:
            raise ValueError("Ne poryadok..")

    def __str__(self) -> str:
        return f"{self.start} | {self.end}"

a = DataHandler()
a.set_value("start", "Hello")
print(a)
