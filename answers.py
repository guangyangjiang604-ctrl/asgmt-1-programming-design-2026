def is_return_necessary_for_assignments() -> bool:
    return True
def calculate_movie_minutes(hours: int, mins: int) -> int:
    return (hours * 60) + mins
def say_hello_to_anyone(anyone: str) -> str:
    return f"Hello {anyone}"
def format_number_of_assignments_exams_bonuses(n_assignments: int, n_exams: int, n_bonuses: int) -> str:
    return f"{n_assignments} assignments {n_exams} examinations {n_bonuses} bonuses."
def repeat_n_times(str_to_repeat: str, n: int) -> str:
    return str_to_repeat * n
def format_temperature_degrees(celsius: int) -> str:
    fahrenheit = celsius * 9 / 5 + 32
    return f"{fahrenheit} degrees Fahrenheit"
def format_integer_with_dollar_sign_and_commas(x: int) -> str:
    return f"${x:,}"
def is_positive(x: int) -> bool:
    return x > 0
def is_even(x: int) -> bool:
    return x % 2 == 0
def are_vowels_contained(x: str) -> bool:
    vowels = "aeiou"
    return any(char in vowels for char in x.lower())
