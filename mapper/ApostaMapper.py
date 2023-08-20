from datetime import datetime


class ApostaMapper():
    def to_entity(self, payload: list):
        return (
            int(payload.__getitem__(0)),
            self.convert_date(payload.__getitem__(1)),
            int(payload.__getitem__(2)),
            int(payload.__getitem__(3)),
            int(payload.__getitem__(4)),
            int(payload.__getitem__(5)),
            int(payload.__getitem__(6)),
            int(payload.__getitem__(7)),
            int(payload.__getitem__(8)),
            self.convert_number(payload.__getitem__(9))
        )

    def convert_date(self, value: str):
        date = value.split("/")
        return datetime(
            day=int(date[0]),
            month=int(date[1]),
            year=int(date[2])
        )

    def convert_number(self, value: str):
        value = value.replace(",", "")
        if value == "":
            value = 0
        return float(value)
