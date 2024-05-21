from random import sample, choice


class ProcessDict:

    @staticmethod
    def transform_value_to_range(data: dict[str, str | range]) -> None:
        value = data['Значение']
        if isinstance(value, str):
            start_value, end_value = map(int, value.split('-'))
            data['Значение'] = range(start_value, end_value + 1)

    @staticmethod
    def get_random_dict(
            data: list[dict[str, str | range]], min_count: int = 3, max_count: int = 4
    ) -> list[dict[str, str | range]]:
        count = choice(range(min_count, max_count + 1))

        result_data = sample(data, count)

        return result_data


class ProcessRange:

    @staticmethod
    def get_random_value_from_range(num_range: range) -> int:
        nummer = choice(num_range)
        return nummer
