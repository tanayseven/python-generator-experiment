import itertools
from timeit import timeit

from eager_finder import locations_of_newline_characters as eager_locations_of_newline_characters
from lazy_finder import \
    locations_of_newline_characters_generator_function as lazy_locations_of_newline_characters_generator_function
from lazy_finder import \
    locations_of_newline_characters_generator_expression as lazy_locations_of_newline_characters_generator_expression

book_content = ''
REPETITIONS = 100
FIRST_N = 1000000000  # one billion


def time_eager_finder():
    time_taken = timeit(
        lambda: eager_locations_of_newline_characters(book_content),
        number=REPETITIONS,
    )
    print(f"Time taken for: time_eager_finder: {time_taken:.20f}sec")


def time_lazy_function_generator_finder():
    time_taken = timeit(
        lambda: lazy_locations_of_newline_characters_generator_function(book_content),
        number=REPETITIONS,
    )
    print(f"Time taken for: time_lazy_function_generator_finder: {time_taken:.20f}sec")


def time_lazy_generator_expression_finder():
    time_taken = timeit(
        lambda: lazy_locations_of_newline_characters_generator_expression(book_content),
        number=REPETITIONS,
    )
    print(f"Time taken for: time_lazy_generator_expression_finder: {time_taken:.20f}sec")


def time_eager_finder_first_n(n):
    time_taken = timeit(
        lambda: itertools.islice(eager_locations_of_newline_characters(book_content), n),
        number=REPETITIONS,
    )
    print(f"Time taken for: time_eager_finder_first_{n}: {time_taken:.20f}sec")


def time_lazy_function_generator_finder_first_n(n):
    time_taken = timeit(
        lambda: itertools.islice(lazy_locations_of_newline_characters_generator_function(book_content), n),
        number=REPETITIONS,
    )
    print(f"Time taken for: time_lazy_function_generator_finder_first_{n}: {time_taken:.20f}sec")


def time_lazy_generator_expression_finder_first_n(n):
    time_taken = timeit(
        lambda: itertools.islice(lazy_locations_of_newline_characters_generator_expression(book_content), n),
        number=REPETITIONS,
    )
    print(f"Time taken for: time_lazy_generator_expression_finder_first_{n}: {time_taken:.20f}sec")


def time_all():
    time_eager_finder()
    time_lazy_function_generator_finder()
    time_lazy_generator_expression_finder()
    time_eager_finder_first_n(FIRST_N)
    time_lazy_function_generator_finder_first_n(FIRST_N)
    time_lazy_generator_expression_finder_first_n(FIRST_N)


def load_book(book_path):
    global book_content
    with open(book_path) as f:
        book_content = f.read()


if __name__ == '__main__':
    load_book("sherlock.txt")
    time_all()
