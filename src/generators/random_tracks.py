from abc \
    import (
        ABC,
        abstractmethod
    )

from random \
    import SystemRandom


class RandomTracks(
    ABC
):
    def __init__(
        self
    ):
        super().__init__()
        self.random_generator = SystemRandom()

    @abstractmethod
    def compute(
        self
    ) -> chr:
        raise NotImplementedError

    def get_generator(
        self
    ) -> SystemRandom:
        return self.random_generator

    def set_generator(
        self,
        value: SystemRandom
    ) -> None:
        self.random_generator = value
    