from src.generators \
    import RandomTracks


class RandomRange(
    RandomTracks
):
    def __init__(
        self,
        begin: str,
        end: str
    ):
        super().__init__()
        self.begin_range: int = ord(
            begin
        )

        self.end_range: int = ord(
            end
        )

    def compute(
        self
    ) -> chr:
        value = self.get_generator().randint(
            self.begin_range,
            self.end_range
        )

        return chr(
            value
        )

    def get_begin_range(
        self
    ) -> int:
        return self.begin_range

    def get_end_range(
        self
    ) -> int:
        return self.end_range

    def set_end_range(
        self,
        value
    ) -> None:
        if value is chr:
            self.end_range = ord(
                value
            )

        if value is int:
            self.end_range = value

    def set_begin_range(
        self,
        value
    ) -> None:
        if value is chr:
            self.begin_range = ord(
                value
            )

        if value is int:
            self.begin_range = value

