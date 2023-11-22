from src.generators.random_range \
    import RandomRange

from random \
    import SystemRandom

alphabet_range = RandomRange("a", "z")
number_range = RandomRange("0", "9")

random_ranges = [alphabet_range, number_range]
length_of_random_ranges = len(random_ranges)
random_ranges_last_index: int = length_of_random_ranges - 1


def main(
    length_of_password: int = 12
) -> None:
    global random_ranges, random_ranges_last_index

    select_generator = SystemRandom()
    password = ""

    for idx in range(length_of_password):
        select = select_generator.randint(
            0,
            random_ranges_last_index
        )

        selected_value = str(
            random_ranges[
                select
            ].compute()
        )

        if bool(
            select_generator.randint(
                0,
                1
            )
        ):
            selected_value = selected_value.upper()

        password = password + selected_value

    print(password)


if __name__ == "__main__":
    main()
