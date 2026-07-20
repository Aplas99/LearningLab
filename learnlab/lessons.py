from .guidance import GUIDANCE
from .paths import ASSIGNMENTS_DIR


CATEGORIES = [
    {"id": "python", "title": "Python", "description": "Language fundamentals"},
    {"id": "oop", "title": "OOP", "description": "Objects and program design"},
    {"id": "math", "title": "Math", "description": "Math translated into code"},
]


def lesson(
    lesson_id,
    category,
    order,
    title,
    summary,
    explanation,
    example,
    assignment,
    starter,
    tests,
    *,
    eli10=None,
    concepts=(),
):
    return {
        "id": lesson_id,
        "category": category,
        "order": order,
        "title": title,
        "summary": summary,
        "explanation": explanation,
        "example": example,
        "assignment": assignment,
        "starter": starter,
        "tests": tests,
        "eli10": eli10,
        "concepts": list(concepts),
    }


LESSONS = [
    lesson(
        "python/variables",
        "python",
        2,
        "Variables and expressions",
        "Store values, name them clearly, and combine them with operators.",
        "A variable is a name bound to a value. Python evaluates the expression on the right side of `=` first, then binds the result to the name on the left. Names let later code express intent instead of repeating raw values.",
        """item_price = 12.50
quantity = 4
subtotal = item_price * quantity
print(subtotal)  # 50.0""",
        "The starter file describes one cafe order using named values. Replace the `0` assigned to `order_total` with an expression that multiplies each price by its quantity and adds both results.",
        """sandwich_price = 8.75
drink_price = 2.25
sandwiches = 2
drinks = 3

# Replace 0 with an expression using the variables above.
order_total = 0""",
        """import unittest
import solution

class OrderTotalTests(unittest.TestCase):
    def test_order_total(self):
        self.assertAlmostEqual(solution.order_total, 24.25)

    def test_total_is_numeric(self):
        self.assertIsInstance(solution.order_total, (int, float))

if __name__ == "__main__":
    unittest.main()""",
        concepts=("names", "numbers", "operators", "return values"),
    ),
    lesson(
        "python/conditionals",
        "python",
        8,
        "Conditionals",
        "Choose which code runs by asking boolean questions.",
        "An `if` statement evaluates a condition. Exactly one matching branch in an `if`/`elif`/`else` chain runs. Order matters: put narrower cases before broader ones when they overlap.",
        """temperature = 68
if temperature < 50:
    label = "cold"
elif temperature < 75:
    label = "comfortable"
else:
    label = "hot""",
        "A movie theater charges $8 for children under 13, $12 for ages 13-64, and $9 for ages 65 and above. Implement `ticket_price(age)` using an `if`/`elif`/`else` chain. Assume the supplied age is valid.",
        """def ticket_price(age):
    # Return the correct price for the supplied age.
    pass""",
        """import unittest
from solution import ticket_price

class TicketPriceTests(unittest.TestCase):
    def test_boundary_ages(self):
        self.assertEqual(ticket_price(12), 8)
        self.assertEqual(ticket_price(13), 12)
        self.assertEqual(ticket_price(64), 12)
        self.assertEqual(ticket_price(65), 9)

if __name__ == "__main__":
    unittest.main()""",
        concepts=("booleans", "if/elif/else", "comparisons", "errors"),
    ),
    lesson(
        "python/loops",
        "python",
        9,
        "For loops and range",
        "Repeat work over a sequence without duplicating code.",
        "A `for` loop takes one item at a time from an iterable. An accumulator is a variable updated during each pass. Prefer direct iteration (`for score in scores`) when you need values rather than indexes.",
        """scores = [8, 10, 7]
total = 0
for score in scores:
    total += score
average = total / len(scores)""",
        "A delivery driver records trip distances. Implement `long_trip_total(distances, minimum)` to return the sum of only distances greater than or equal to `minimum`.",
        """def long_trip_total(distances, minimum):
    total = 0
    # Add qualifying distances to total.
    return total""",
        """import unittest
from solution import long_trip_total

class LongTripTests(unittest.TestCase):
    def test_filters_and_sums(self):
        self.assertEqual(long_trip_total([3, 12, 8, 20], 10), 32)

    def test_boundary_counts(self):
        self.assertEqual(long_trip_total([5, 5, 4], 5), 10)

    def test_empty_input(self):
        self.assertEqual(long_trip_total([], 10), 0)

if __name__ == "__main__":
    unittest.main()""",
        concepts=("iteration", "accumulators", "filtering"),
    ),
    lesson(
        "python/functions",
        "python",
        3,
        "Functions",
        "Package a calculation behind a name, inputs, and a return value.",
        "A function creates a reusable unit of behavior. The names inside the parentheses in a `def` line are parameters: when another line calls the function, its argument values are assigned to those names. `return` sends the calculated result back to the caller. In LearnLab starters, keep the `def` line and replace `pass` with the requested calculation.",
        """def rectangle_area(width, height):
    return width * height

wall_area = rectangle_area(12, 8)""",
        "Implement `rectangle_perimeter(length, width)`. The two parameter names receive the rectangle dimensions. Return the sum of all four sides.",
        """def rectangle_perimeter(length, width):
    # Replace pass with a return statement using length and width.
    pass""",
        """import unittest
from solution import rectangle_perimeter

class RectanglePerimeterTests(unittest.TestCase):
    def test_typical_rectangle(self):
        self.assertEqual(rectangle_perimeter(8, 3), 22)

    def test_square(self):
        self.assertEqual(rectangle_perimeter(5, 5), 20)

    def test_uses_supplied_arguments(self):
        self.assertEqual(rectangle_perimeter(2.5, 4), 13)

if __name__ == "__main__":
    unittest.main()""",
        eli10="The `def` line builds a little machine. Parameters are its labeled input slots. A function call puts values into those slots, and `return` sends the machine's answer back out.",
        concepts=("def", "parameters", "arguments", "return"),
    ),
    lesson(
        "python/collections",
        "python",
        6,
        "Lists and dictionaries",
        "Use lists for ordered values and dictionaries for key-value relationships.",
        "Collections let one name hold many related values. Lists are ordered and accessed by position. Dictionaries map unique keys to values. Choose based on how the data will be looked up, not merely how it arrives.",
        """inventory = {"apples": 4, "pears": 2}
inventory["apples"] += 3

colors = ["red", "green", "blue"]
first_color = colors[0]""",
        "Implement `build_profile(name, skills)`. Return a dictionary with three keys: `name` stores the supplied name, `first_skill` stores `skills[0]`, and `skill_count` stores `len(skills)`. Assume the skills list is not empty.",
        """def build_profile(name, skills):
    # Build and return the profile dictionary.
    pass""",
        """import unittest
from solution import build_profile

class BuildProfileTests(unittest.TestCase):
    def test_profile_fields(self):
        self.assertEqual(
            build_profile("Ada", ["math", "python"]),
            {"name": "Ada", "first_skill": "math", "skill_count": 2},
        )

    def test_uses_supplied_values(self):
        self.assertEqual(
            build_profile("Lin", ["design"]),
            {"name": "Lin", "first_skill": "design", "skill_count": 1},
        )

if __name__ == "__main__":
    unittest.main()""",
        eli10="A list is like a numbered row of cubbies. A dictionary is like a set of labeled cubbies: instead of asking for cubby 0, you ask for the one labeled `apples`.",
        concepts=("lists", "dictionaries", "membership", "counting"),
    ),
    lesson(
        "oop/classes",
        "oop",
        1,
        "Classes and objects",
        "Define a reusable blueprint, then create independent objects from it.",
        "A class defines data and behavior that belong together. Calling the class creates an object (an instance). `self` is the particular object receiving a method call, so each instance can keep its own state.",
        """class Lamp:
    def __init__(self, color):
        self.color = color
        self.is_on = False

    def switch_on(self):
        self.is_on = True""",
        "Create a `BankAccount` class initialized with `owner` and an optional `balance` (default 0). Add `deposit(amount)` that increases the balance and returns the new balance. Reject non-positive deposits with `ValueError`.",
        """class BankAccount:
    def __init__(self, owner, balance=0):
        pass

    def deposit(self, amount):
        pass""",
        """import unittest
from solution import BankAccount

class BankAccountTests(unittest.TestCase):
    def test_initial_state(self):
        account = BankAccount("Ada", 25)
        self.assertEqual(account.owner, "Ada")
        self.assertEqual(account.balance, 25)

    def test_deposit(self):
        account = BankAccount("Lin")
        self.assertEqual(account.deposit(10), 10)
        self.assertEqual(account.deposit(2.5), 12.5)

    def test_rejects_invalid_deposit(self):
        with self.assertRaises(ValueError):
            BankAccount("Sam").deposit(0)

if __name__ == "__main__":
    unittest.main()""",
        eli10="A class is a recipe card; an object is one actual meal made from it. The recipe can make many meals, and changing one plate does not magically change the others.",
        concepts=("classes", "instances", "self", "methods"),
    ),
    lesson(
        "oop/encapsulation",
        "oop",
        2,
        "Encapsulation and properties",
        "Protect an object’s rules by controlling how its state changes.",
        "Encapsulation keeps state changes behind methods or properties that enforce valid values. A property can expose method logic through attribute syntax. In Python, a leading underscore signals that an attribute is an internal implementation detail.",
        """class Thermostat:
    def __init__(self):
        self._temperature = 68

    @property
    def temperature(self):
        return self._temperature""",
        "Create a `Product` with `name` and a price property. The initial price and every later assignment to `price` must be zero or greater; otherwise raise `ValueError`.",
        """class Product:
    def __init__(self, name, price):
        pass

    @property
    def price(self):
        pass

    @price.setter
    def price(self, value):
        pass""",
        """import unittest
from solution import Product

class ProductTests(unittest.TestCase):
    def test_reads_and_updates_price(self):
        product = Product("Notebook", 4.5)
        self.assertEqual(product.name, "Notebook")
        self.assertEqual(product.price, 4.5)
        product.price = 6
        self.assertEqual(product.price, 6)

    def test_rejects_negative_initial_price(self):
        with self.assertRaises(ValueError):
            Product("Notebook", -1)

    def test_rejects_negative_update(self):
        product = Product("Notebook", 2)
        with self.assertRaises(ValueError):
            product.price = -0.01

if __name__ == "__main__":
    unittest.main()""",
        eli10="Think of the object as a vending machine. You use its buttons instead of reaching inside, because the buttons can stop impossible choices before they mess up the machine.",
        concepts=("invariants", "private convention", "property", "setter"),
    ),
    lesson(
        "oop/inheritance",
        "oop",
        4,
        "Inheritance and polymorphism",
        "Share an interface while allowing subclasses to provide specialized behavior.",
        "Inheritance describes an is-a relationship. A subclass receives behavior from its parent and may override methods. Polymorphism means calling the same method on different object types can produce type-specific results.",
        """class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2""",
        "Create an `Employee` class with `name` and `weekly_pay()`. Then create `HourlyEmployee(name, hours, rate)` and `SalariedEmployee(name, annual_salary)` subclasses. Hourly weekly pay is hours times rate; salaried weekly pay is annual salary divided by 52.",
        """class Employee:
    def __init__(self, name):
        self.name = name

    def weekly_pay(self):
        raise NotImplementedError


class HourlyEmployee(Employee):
    pass


class SalariedEmployee(Employee):
    pass""",
        """import unittest
from solution import Employee, HourlyEmployee, SalariedEmployee

class EmployeeTests(unittest.TestCase):
    def test_hourly_employee(self):
        employee = HourlyEmployee("Mina", 30, 20)
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.name, "Mina")
        self.assertEqual(employee.weekly_pay(), 600)

    def test_salaried_employee(self):
        employee = SalariedEmployee("Noah", 52000)
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.weekly_pay(), 1000)

if __name__ == "__main__":
    unittest.main()""",
        eli10="A parent class is a basic game character template. Subclasses keep the shared controls but can replace a move: pressing the same attack button gives the wizard a spell and the knight a sword swing.",
        concepts=("inheritance", "overriding", "polymorphism", "abstract behavior"),
    ),
    lesson(
        "oop/composition",
        "oop",
        5,
        "Composition",
        "Build capable objects by giving them other objects to work with.",
        "Composition describes a has-a relationship. Instead of inheriting behavior, one object delegates work to another object it contains. This usually keeps components smaller and makes them easier to replace or test independently.",
        """class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()""",
        "Create a `Playlist` class that stores a name and a list of `Song` objects. A `Song` has `title` and `seconds`. Add `add(song)` and `duration()` methods; duration returns the total seconds of all songs.",
        """class Song:
    def __init__(self, title, seconds):
        pass


class Playlist:
    def __init__(self, name):
        pass

    def add(self, song):
        pass

    def duration(self):
        pass""",
        """import unittest
from solution import Playlist, Song

class PlaylistTests(unittest.TestCase):
    def test_empty_playlist(self):
        playlist = Playlist("Focus")
        self.assertEqual(playlist.name, "Focus")
        self.assertEqual(playlist.duration(), 0)

    def test_adds_songs_and_totals_duration(self):
        playlist = Playlist("Focus")
        first = Song("Alpha", 120)
        second = Song("Beta", 75)
        playlist.add(first)
        playlist.add(second)
        self.assertEqual(playlist.songs, [first, second])
        self.assertEqual(playlist.duration(), 195)

if __name__ == "__main__":
    unittest.main()""",
        eli10="Composition is building with blocks. A playlist is not a kind of song; it has songs. Each block does its own job, and you connect them into something larger.",
        concepts=("has-a relationships", "delegation", "object collaboration"),
    ),
    lesson(
        "math/unit-conversion",
        "math",
        2,
        "Ratios and unit conversion",
        "Translate between units by multiplying by conversion ratios.",
        "A conversion factor is a ratio equal to one, such as 100 centimeters per meter. Multiplying by it changes the unit label without changing the underlying quantity. Track units alongside numbers to catch inverted ratios.",
        """kilometers = 5
miles_per_kilometer = 0.621371
miles = kilometers * miles_per_kilometer""",
        "A recipe uses milliliters, but a measuring cup shows US cups. Implement `ml_to_cups(milliliters)` using 236.588 milliliters per cup. Return the result rounded to three decimals and reject negative input.",
        """def ml_to_cups(milliliters):
    pass""",
        """import unittest
from solution import ml_to_cups

class ConversionTests(unittest.TestCase):
    def test_one_cup(self):
        self.assertEqual(ml_to_cups(236.588), 1.0)

    def test_partial_cup(self):
        self.assertEqual(ml_to_cups(500), 2.113)

    def test_rejects_negative_input(self):
        with self.assertRaises(ValueError):
            ml_to_cups(-1)

if __name__ == "__main__":
    unittest.main()""",
        concepts=("ratios", "units", "rounding"),
    ),
    lesson(
        "math/linear-equations",
        "math",
        3,
        "Linear equations",
        "Turn a line’s slope and starting value into a reusable function.",
        "A linear relationship has a constant rate of change. In `y = mx + b`, `m` is the slope (change in y per unit x), and `b` is the y-intercept (the value when x is zero). Code maps naturally to this formula.",
        """def line_value(x, slope, intercept):
    return slope * x + intercept""",
        "A taxi fare has a $3.50 base charge plus $2.20 per mile. Implement `taxi_fare(miles)` using a linear equation, rounded to two decimals. Reject negative distances.",
        """def taxi_fare(miles):
    pass""",
        """import unittest
from solution import taxi_fare

class TaxiFareTests(unittest.TestCase):
    def test_zero_miles_is_base_fare(self):
        self.assertEqual(taxi_fare(0), 3.5)

    def test_typical_trip(self):
        self.assertEqual(taxi_fare(7.25), 19.45)

    def test_rejects_negative_distance(self):
        with self.assertRaises(ValueError):
            taxi_fare(-0.1)

if __name__ == "__main__":
    unittest.main()""",
        eli10="Imagine a taxi meter. It starts at $3.50 before the car moves, then clicks up by the same amount for every mile. The starting amount is `b`; each click-rate is `m`.",
        concepts=("slope", "intercept", "modeling"),
    ),
    lesson(
        "math/distance",
        "math",
        4,
        "Coordinate distance",
        "Use the Pythagorean theorem to measure the straight-line gap between points.",
        "The horizontal and vertical differences between two points form the legs of a right triangle. The straight-line distance is its hypotenuse: `sqrt((x2 - x1)^2 + (y2 - y1)^2)`. Python’s `math.hypot` performs this calculation accurately.",
        """from math import hypot

dx = 7 - 3
dy = 5 - 2
distance = hypot(dx, dy)""",
        "A robot moves on a coordinate grid. Implement `distance_between(point_a, point_b)` where each point is an `(x, y)` tuple. Return the straight-line distance rounded to two decimals.",
        """def distance_between(point_a, point_b):
    pass""",
        """import unittest
from solution import distance_between

class DistanceTests(unittest.TestCase):
    def test_three_four_five_triangle(self):
        self.assertEqual(distance_between((0, 0), (3, 4)), 5.0)

    def test_negative_coordinates(self):
        self.assertEqual(distance_between((-2, 1), (2, -2)), 5.0)

    def test_decimal_result(self):
        self.assertEqual(distance_between((1, 1), (2, 2)), 1.41)

if __name__ == "__main__":
    unittest.main()""",
        eli10="Walk sideways from one point until you line up with the other, then walk up. Those two walks make two sides of a right triangle. The distance formula finds the diagonal shortcut.",
        concepts=("coordinates", "Pythagorean theorem", "square roots"),
    ),
    lesson(
        "math/statistics",
        "math",
        5,
        "Mean and median",
        "Summarize a dataset while understanding what each summary hides.",
        "The mean is the sum divided by the count and reacts strongly to extreme values. The median is the middle sorted value, or the mean of the two middle values. A useful program handles odd, even, and empty datasets explicitly.",
        """values = [2, 9, 4]
mean = sum(values) / len(values)
ordered = sorted(values)
median = ordered[len(ordered) // 2]""",
        "Implement `summarize(values)` to return a dictionary with `mean` and `median`, each rounded to two decimals. Raise `ValueError` for an empty list. Do not modify the original list.",
        """def summarize(values):
    pass""",
        """import unittest
from solution import summarize

class SummaryTests(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(summarize([9, 2, 4]), {"mean": 5.0, "median": 4})

    def test_even_count(self):
        self.assertEqual(summarize([1, 4, 2, 9]), {"mean": 4.0, "median": 3.0})

    def test_does_not_mutate_input(self):
        values = [3, 1, 2]
        summarize(values)
        self.assertEqual(values, [3, 1, 2])

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            summarize([])

if __name__ == "__main__":
    unittest.main()""",
        eli10="The mean shares all the points evenly among everyone. The median lines everyone up and asks who stands in the middle. One giant outlier can steal the mean’s attention, while the median mostly shrugs.",
        concepts=("mean", "median", "sorting", "edge cases"),
    ),
    lesson(
        "math/compound-interest",
        "math",
        8,
        "Exponents and compound interest",
        "Model repeated percentage growth with exponential formulas.",
        "Compounding applies growth to the updated balance, not only the original principal. With principal `P`, annual rate `r`, `n` compounds per year, and `t` years, the balance is `P(1 + r/n)^(nt)`.",
        """principal = 1000
annual_rate = 0.05
years = 3
balance = principal * (1 + annual_rate) ** years""",
        "Implement `future_value(principal, annual_rate, years, compounds_per_year=12)`. Return the compounded balance rounded to two decimals. Reject any negative input and reject a compounds-per-year value below 1.",
        """def future_value(principal, annual_rate, years, compounds_per_year=12):
    pass""",
        """import unittest
from solution import future_value

class FutureValueTests(unittest.TestCase):
    def test_monthly_compounding(self):
        self.assertEqual(future_value(1000, 0.06, 5), 1348.85)

    def test_annual_compounding(self):
        self.assertEqual(future_value(500, 0.1, 2, 1), 605.0)

    def test_zero_years(self):
        self.assertEqual(future_value(750, 0.08, 0), 750.0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            future_value(-1, 0.1, 2)
        with self.assertRaises(ValueError):
            future_value(100, 0.1, 2, 0)

if __name__ == "__main__":
    unittest.main()""",
        eli10="Each growth step adds a little money. The next step grows both your original money and the earlier growth, like a snowball picking up more snow each time it rolls.",
        concepts=("exponents", "percentages", "compound growth", "validation"),
    ),
]


# These lessons fill the major foundation gaps in the initial curriculum. They are
# defined separately so existing lesson IDs and assignment folders remain stable.
LESSONS.extend(
    [
        lesson(
            "python/syntax-output",
            "python",
            1,
            "Syntax, output, and comments",
            "Read Python's structure and produce clear text output.",
            "Python runs a file from top to bottom. `print()` displays a value in the terminal, while comments beginning with `#` explain intent to human readers and are ignored by Python. An f-string starts with `f` and replaces names inside braces, such as `{name}`, with their current values.",
            """name = "Maya"
lessons = 3
# The names inside braces are replaced before printing.
print(f"{name} finished {lessons} lessons")""",
            "The starter file already defines `name`, `completed`, and `total`. Add one `print()` call with an f-string so running `python3 solution.py` displays exactly `Maya: 3/5 lessons complete`.",
            """name = "Maya"
completed = 3
total = 5

# Add one print call below. Use the three names above in an f-string.
""",
            """import subprocess
import sys
import unittest
from pathlib import Path

SOLUTION = Path(__file__).with_name("solution.py")

class StatusMessageTests(unittest.TestCase):
    def test_script_prints_expected_message(self):
        result = subprocess.run(
            [sys.executable, str(SOLUTION)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Maya: 3/5 lessons complete")

if __name__ == "__main__":
    unittest.main()""",
            concepts=("indentation", "statements", "comments", "f-strings"),
        ),
        lesson(
            "python/types-casting",
            "python",
            4,
            "Data types and casting",
            "Recognize common value types and deliberately convert between them.",
            "Python values have types such as `str`, `int`, `float`, and `bool`. Casting functions like `int()` and `float()` create converted values when the input is valid. Conversion may fail, so code should decide what inputs it accepts instead of hoping Python guesses correctly.",
            """quantity_text = "12"
quantity = int(quantity_text)
price = float("4.50")
total = quantity * price""",
            "Implement `celsius_to_fahrenheit(celsius_text)`. Convert the supplied text to a float, apply `celsius * 9 / 5 + 32`, and return the result rounded to one decimal place.",
            """def celsius_to_fahrenheit(celsius_text):
    # Convert the input before doing arithmetic.
    pass""",
            """import unittest
from solution import celsius_to_fahrenheit

class TemperatureCastingTests(unittest.TestCase):
    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit("0"), 32.0)

    def test_decimal_text(self):
        self.assertEqual(celsius_to_fahrenheit("37.5"), 99.5)

    def test_negative_text(self):
        self.assertEqual(celsius_to_fahrenheit("-40"), -40.0)

if __name__ == "__main__":
    unittest.main()""",
            concepts=("str", "int", "float", "casting", "round"),
        ),
        lesson(
            "python/strings",
            "python",
            5,
            "Strings and text processing",
            "Slice, clean, search, and combine text without changing the original string.",
            "Strings are immutable sequences of characters. Indexing selects one character, slicing selects a range, and methods such as `strip()`, `lower()`, and `replace()` return new strings. Chaining methods creates a small text-processing pipeline.",
            """raw_name = "  Ada Lovelace  "
clean_name = raw_name.strip().lower()
username = clean_name.replace(" ", ".")
# "ada.lovelace""",
            'Implement `make_slug(title)`. Remove surrounding whitespace, convert to lowercase, split on any whitespace, and join the words with hyphens. For example, `"  Learn Python Today "` becomes `"learn-python-today"`.',
            """def make_slug(title):
    pass""",
            """import unittest
from solution import make_slug

class MakeSlugTests(unittest.TestCase):
    def test_regular_title(self):
        self.assertEqual(make_slug("Learn Python Today"), "learn-python-today")

    def test_mixed_case_and_space(self):
        self.assertEqual(make_slug("  Clean   DATA  "), "clean-data")

    def test_empty_text(self):
        self.assertEqual(make_slug("   "), "")

if __name__ == "__main__":
    unittest.main()""",
            concepts=("immutability", "indexing", "slicing", "string methods"),
        ),
        lesson(
            "python/tuples-sets",
            "python",
            7,
            "Tuples and sets",
            "Represent fixed records with tuples and unique membership with sets.",
            "A tuple is an ordered sequence that cannot be changed after creation, which suits fixed records. A set stores unique values and supports mathematical operations such as union and intersection. Set order is not a stable presentation order, so sort results when order matters.",
            """point = (4, 7)
x, y = point

team_a = {"music", "chess"}
team_b = {"chess", "hiking"}
shared = team_a & team_b  # {"chess"}""",
            "Implement `shared_interests(first, second)`. Accept any two iterables of interest names and return a tuple containing their unique shared interests in alphabetical order.",
            """def shared_interests(first, second):
    pass""",
            """import unittest
from solution import shared_interests

class SharedInterestTests(unittest.TestCase):
    def test_intersection_is_sorted_tuple(self):
        result = shared_interests(["music", "chess", "music"], ["hiking", "chess", "music"])
        self.assertEqual(result, ("chess", "music"))

    def test_no_overlap(self):
        self.assertEqual(shared_interests(["a"], ["b"]), ())

    def test_accepts_sets(self):
        self.assertEqual(shared_interests({"z", "a"}, {"a"}), ("a",))

if __name__ == "__main__":
    unittest.main()""",
            eli10="A tuple is a sealed row of labeled facts: once packed, it stays put. A set is a guest list that refuses duplicate names and can quickly tell you who appears on two lists.",
            concepts=("tuples", "unpacking", "sets", "intersection"),
        ),
        lesson(
            "python/while-loops",
            "python",
            10,
            "While loops",
            "Repeat until a condition changes, with an explicit path to stopping.",
            "A `while` loop repeats while its condition is true. It works best when the number of repetitions is not known in advance. Something inside the loop must move the condition toward false; otherwise the loop never ends.",
            """attempts = 0
while attempts < 3:
    attempts += 1
print("Finished")""",
            "Implement `months_to_goal(balance, monthly_deposit, goal)`. Starting with `balance`, add the positive deposit once per month until the balance reaches or exceeds the goal, then return the month count. Assume the deposit is positive.",
            """def months_to_goal(balance, monthly_deposit, goal):
    pass""",
            """import unittest
from solution import months_to_goal

class MonthsToGoalTests(unittest.TestCase):
    def test_counts_months(self):
        self.assertEqual(months_to_goal(100, 30, 205), 4)

    def test_already_at_goal(self):
        self.assertEqual(months_to_goal(250, 20, 200), 0)

if __name__ == "__main__":
    unittest.main()""",
            concepts=("conditions", "state updates", "termination", "guard clauses"),
        ),
        lesson(
            "python/arguments-scope",
            "python",
            11,
            "Arguments and scope",
            "Design flexible function inputs while keeping names local and predictable.",
            "Positional arguments are matched by position, keyword arguments by name, and default values make inputs optional. `*args` gathers extra positional values. Names created inside a function are local, preventing one function's temporary work from leaking into another part of the program.",
            """def total_with_tax(*prices, tax_rate=0.0):
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)

total_with_tax(10, 5, tax_rate=0.08)""",
            "Implement `invoice_total(*prices, tax_rate=0, discount=0)`. Apply the discount percentage to the subtotal, then apply tax, and return the result rounded to two decimals. Assume both rates are between 0 and 1.",
            """def invoice_total(*prices, tax_rate=0, discount=0):
    pass""",
            """import unittest
from solution import invoice_total

class InvoiceTotalTests(unittest.TestCase):
    def test_multiple_prices(self):
        self.assertEqual(invoice_total(20, 30, tax_rate=0.1, discount=0.2), 44.0)

    def test_defaults(self):
        self.assertEqual(invoice_total(4.25, 5.75), 10.0)

if __name__ == "__main__":
    unittest.main()""",
            eli10="A function is a small room with its own labeled shelves. Arguments bring supplies into the room, local variables stay inside, and the return value is what comes back out the door.",
            concepts=("positional arguments", "keyword arguments", "*args", "local scope"),
        ),
        lesson(
            "python/comprehensions",
            "python",
            12,
            "Comprehensions",
            "Build transformed collections with a compact expression.",
            "A comprehension describes a new collection as a transformation over existing items, optionally with a filter. It is ideal for one clear mapping or filter. Once the expression needs several branches or side effects, a regular loop is easier to read.",
            """scores = [52, 91, 78]
passing = [score for score in scores if score >= 70]
squares = {number: number ** 2 for number in range(4)}""",
            "Implement `passing_names(records)` where each record is a `(name, score)` tuple. Return a lowercase list of names scoring at least 70, sorted alphabetically, using a comprehension.",
            """def passing_names(records):
    pass""",
            """import unittest
from solution import passing_names

class PassingNamesTests(unittest.TestCase):
    def test_filters_normalizes_and_sorts(self):
        records = [("Zoe", 70), ("BEN", 69), ("Ana", 94)]
        self.assertEqual(passing_names(records), ["ana", "zoe"])

    def test_empty_records(self):
        self.assertEqual(passing_names([]), [])

if __name__ == "__main__":
    unittest.main()""",
            eli10="A comprehension is a one-line assembly belt: take each item, optionally reject it at the gate, transform the accepted items, and place them in a new collection.",
            concepts=("mapping", "filtering", "list comprehensions", "dictionary comprehensions"),
        ),
        lesson(
            "python/modules-json",
            "python",
            13,
            "Modules and JSON",
            "Import reusable tools and translate structured data to and from text.",
            "A module is a Python file whose names can be imported elsewhere. The standard-library `json` module converts between JSON text and Python dictionaries, lists, strings, numbers, booleans, and `None`. Parsing is the boundary where text becomes structured data.",
            """import json

payload = '{"name": "Ada", "active": true}'
record = json.loads(payload)
record["active"] = False
updated = json.dumps(record)""",
            "Implement `total_from_json(payload)`. The JSON text contains an `items` list; each item has `price` and `quantity`. Return the total rounded to two decimals. Invalid JSON should naturally raise `json.JSONDecodeError`.",
            """import json


def total_from_json(payload):
    pass""",
            """import json
import unittest
from solution import total_from_json

class JsonTotalTests(unittest.TestCase):
    def test_totals_items(self):
        payload = json.dumps({"items": [{"price": 2.5, "quantity": 3}, {"price": 4, "quantity": 1}]})
        self.assertEqual(total_from_json(payload), 11.5)

    def test_empty_items(self):
        self.assertEqual(total_from_json('{"items": []}'), 0)

    def test_invalid_json(self):
        with self.assertRaises(json.JSONDecodeError):
            total_from_json("not json")

if __name__ == "__main__":
    unittest.main()""",
            eli10="JSON is a shipping label for data: it is plain text that many programs can read. The `json` module unpacks that label into Python collections and can pack them back into text.",
            concepts=("imports", "standard library", "JSON", "serialization"),
        ),
        lesson(
            "python/exceptions",
            "python",
            14,
            "Exceptions",
            "Handle expected failures without hiding programming mistakes.",
            "Exceptions interrupt normal execution and carry information about a failure. Use `try` around the smallest operation expected to fail, catch specific exception types, and raise a clearer exception when callers need a better contract. A broad bare `except` can conceal real bugs.",
            """def parse_count(text):
    try:
        count = int(text)
    except ValueError as error:
        raise ValueError("count must be a whole number") from error
    return count""",
            'Implement `average_from_text(values)`. Convert every value to a float and return their average rounded to two decimals. Raise `ValueError("values must be numeric")` when conversion fails and `ValueError("values cannot be empty")` for an empty input.',
            """def average_from_text(values):
    pass""",
            """import unittest
from solution import average_from_text

class AverageTextTests(unittest.TestCase):
    def test_numeric_values(self):
        self.assertEqual(average_from_text(["2", "3.5", 6]), 3.83)

    def test_bad_value_message(self):
        with self.assertRaisesRegex(ValueError, "values must be numeric"):
            average_from_text(["2", "nope"])

    def test_empty_message(self):
        with self.assertRaisesRegex(ValueError, "values cannot be empty"):
            average_from_text([])

if __name__ == "__main__":
    unittest.main()""",
            eli10="An exception is a fire alarm for a function. It stops the normal routine and reports what went wrong. Catch only the alarm you know how to handle; covering every alarm with a pillow is, technically, a strategy, just a terrible one.",
            concepts=("try/except", "specific exceptions", "raise", "error messages"),
        ),
        lesson(
            "python/file-handling",
            "python",
            15,
            "File handling",
            "Read local files safely with context managers and clear text assumptions.",
            "Opening a file creates a resource that must be closed. A `with` block closes it automatically, including when an error occurs. Specify text encoding explicitly, and use `pathlib.Path` when you need readable path operations.",
            """from pathlib import Path

notes_path = Path("notes.txt")
with notes_path.open(encoding="utf-8") as handle:
    lines = handle.readlines()""",
            'Implement `summarize_log(path)`. Read a UTF-8 text file and return `{"lines": n, "errors": e}`. Ignore blank lines in the line count, and count a nonblank line as an error when it contains `ERROR` in any letter case.',
            """def summarize_log(path):
    pass""",
            """import tempfile
import unittest
from pathlib import Path
from solution import summarize_log

class LogSummaryTests(unittest.TestCase):
    def test_counts_nonblank_lines_and_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "app.log"
            path.write_text("Started\\n\\nERROR: disk\\nerror: network\\nDone\\n", encoding="utf-8")
            self.assertEqual(summarize_log(path), {"lines": 4, "errors": 2})

    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.log"
            path.write_text("", encoding="utf-8")
            self.assertEqual(summarize_log(path), {"lines": 0, "errors": 0})

if __name__ == "__main__":
    unittest.main()""",
            eli10="A context manager is a responsible librarian. You ask for a file, use it inside the `with` block, and the librarian closes and returns it even if your code trips over a chair halfway through.",
            concepts=("open", "with", "encoding", "pathlib", "resource cleanup"),
        ),
        lesson(
            "oop/class-methods",
            "oop",
            3,
            "Class and static methods",
            "Put alternate constructors and class-wide utilities on the class they belong to.",
            "An instance method receives `self`. A class method receives `cls` and can construct or modify the class itself, which makes it useful for alternate constructors. A static method receives neither and groups a related utility with the class namespace.",
            """class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, value):
        return cls((value - 32) * 5 / 9)""",
            "Create a `TimeSpan` class storing `seconds`. Add `from_minutes(cls, minutes)` as an alternate constructor and `is_valid(value)` as a static method returning true only for numeric, non-negative values. Both constructors must reject invalid values with `ValueError`.",
            """class TimeSpan:
    def __init__(self, seconds):
        pass

    @classmethod
    def from_minutes(cls, minutes):
        pass

    @staticmethod
    def is_valid(value):
        pass""",
            """import unittest
from solution import TimeSpan

class TimeSpanTests(unittest.TestCase):
    def test_regular_constructor(self):
        self.assertEqual(TimeSpan(45).seconds, 45)

    def test_alternate_constructor(self):
        self.assertEqual(TimeSpan.from_minutes(2.5).seconds, 150)

    def test_validation(self):
        self.assertTrue(TimeSpan.is_valid(0))
        self.assertFalse(TimeSpan.is_valid(-1))
        self.assertFalse(TimeSpan.is_valid("5"))
        with self.assertRaises(ValueError):
            TimeSpan(-2)

if __name__ == "__main__":
    unittest.main()""",
            eli10="Instance methods help one particular object. Class methods are factory controls for making objects in another way. Static methods are tools stored in the same toolbox because they belong with the topic.",
            concepts=("instance methods", "@classmethod", "@staticmethod", "alternate constructors"),
        ),
        lesson(
            "oop/special-methods",
            "oop",
            6,
            "Special methods",
            "Make custom objects participate naturally in Python operations.",
            "Special methods such as `__str__`, `__eq__`, and `__add__` define how an object behaves with built-in syntax. Python calls them through operations like `str(value)`, `==`, and `+`. Return `NotImplemented` when an operation does not know how to handle the other type.",
            """class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)""",
            "Create `Money(amount, currency)` with `__str__`, `__eq__`, and `__add__`. String form is `USD 12.50`. Equal objects have the same amount and currency. Addition returns new Money and raises `ValueError` when currencies differ.",
            """class Money:
    def __init__(self, amount, currency):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def __add__(self, other):
        pass""",
            """import unittest
from solution import Money

class MoneyTests(unittest.TestCase):
    def test_string_format(self):
        self.assertEqual(str(Money(12.5, "USD")), "USD 12.50")

    def test_equality(self):
        self.assertEqual(Money(5, "USD"), Money(5, "USD"))
        self.assertNotEqual(Money(5, "USD"), Money(5, "EUR"))

    def test_addition(self):
        self.assertEqual(Money(2.5, "USD") + Money(4, "USD"), Money(6.5, "USD"))

    def test_currency_mismatch(self):
        with self.assertRaises(ValueError):
            Money(2, "USD") + Money(2, "EUR")

if __name__ == "__main__":
    unittest.main()""",
            eli10="Special methods teach your object Python's common gestures. You define what your object means when Python asks it to introduce itself, compare with another object, or respond to a plus sign.",
            concepts=("data model", "__str__", "__eq__", "operator overloading"),
        ),
        lesson(
            "math/numeric-precision",
            "math",
            1,
            "Numeric precision and rounding",
            "Choose number representations that match the guarantees a problem needs.",
            "Binary floating-point cannot represent every decimal fraction exactly, so values such as `0.1 + 0.2` may have a tiny error. Rounding is suitable for display, while money calculations often use integer cents or `decimal.Decimal` to preserve decimal rules.",
            """from decimal import Decimal

price = Decimal("10.25")
tax = Decimal("0.82")
total = price + tax  # Decimal('11.07')""",
            "Implement `split_bill(total, people)`. Split a dollar amount fairly into a list of per-person dollar amounts with exactly two-decimal precision. Earlier people receive any leftover cents. For example, $10 among 3 people is `[3.34, 3.33, 3.33]`. Reject fewer than one person or negative totals.",
            """from decimal import Decimal


def split_bill(total, people):
    pass""",
            """import unittest
from solution import split_bill

class SplitBillTests(unittest.TestCase):
    def test_distributes_leftover_cents(self):
        self.assertEqual(split_bill("10.00", 3), [3.34, 3.33, 3.33])

    def test_even_split(self):
        self.assertEqual(split_bill(12, 4), [3.0, 3.0, 3.0, 3.0])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            split_bill(10, 0)
        with self.assertRaises(ValueError):
            split_bill(-1, 2)

if __name__ == "__main__":
    unittest.main()""",
            eli10="A computer stores many decimals as close approximations, like measuring with a ruler that has extremely tiny gaps. For money, count exact pennies first and turn them back into dollars at the end.",
            concepts=("floating-point", "Decimal", "rounding", "integer cents"),
        ),
        lesson(
            "math/spread",
            "math",
            6,
            "Variance and standard deviation",
            "Measure how tightly or widely values cluster around their mean.",
            "Variance averages the squared distance from each value to the mean. Squaring prevents positive and negative differences from canceling. Standard deviation is the square root of variance, returning the spread to the original unit.",
            """values = [2, 4, 6]
mean = sum(values) / len(values)
variance = sum((x - mean) ** 2 for x in values) / len(values)
standard_deviation = variance ** 0.5""",
            "Implement `population_spread(values)` returning a dictionary with population `variance` and `standard_deviation`, each rounded to two decimals. Raise `ValueError` for empty input.",
            """def population_spread(values):
    pass""",
            """import unittest
from solution import population_spread

class PopulationSpreadTests(unittest.TestCase):
    def test_known_population(self):
        self.assertEqual(population_spread([2, 4, 6]), {"variance": 2.67, "standard_deviation": 1.63})

    def test_no_spread(self):
        self.assertEqual(population_spread([5, 5, 5]), {"variance": 0.0, "standard_deviation": 0.0})

    def test_empty_population(self):
        with self.assertRaises(ValueError):
            population_spread([])

if __name__ == "__main__":
    unittest.main()""",
            eli10="Imagine every number standing some distance from the average. Standard deviation gives one typical distance. A small answer means a tight group; a large answer means the numbers are scattered.",
            concepts=("deviation", "variance", "standard deviation", "population"),
        ),
        lesson(
            "math/linear-regression",
            "math",
            7,
            "Linear regression",
            "Find the straight line that best summarizes paired observations.",
            "Simple linear regression chooses a slope and intercept that minimize squared vertical errors. The slope is covariance divided by x variance; the intercept places the line through the point formed by both means. A model is a summary of a pattern, not proof that x causes y.",
            """# For points (x, y), predict with:
predicted_y = slope * x + intercept
error = actual_y - predicted_y""",
            "Implement `fit_line(points)` for `(x, y)` pairs. Return `(slope, intercept)` rounded to two decimals using least squares. Require at least two points and raise `ValueError` when all x values are equal.",
            """def fit_line(points):
    pass""",
            """import unittest
from solution import fit_line

class FitLineTests(unittest.TestCase):
    def test_exact_line(self):
        self.assertEqual(fit_line([(1, 3), (2, 5), (3, 7)]), (2.0, 1.0))

    def test_best_fit_line(self):
        self.assertEqual(fit_line([(1, 2), (2, 3), (3, 5), (4, 4)]), (0.8, 1.5))

    def test_invalid_points(self):
        with self.assertRaises(ValueError):
            fit_line([(1, 2)])
        with self.assertRaises(ValueError):
            fit_line([(2, 1), (2, 4)])

if __name__ == "__main__":
    unittest.main()""",
            eli10="Scatter the points on paper, then lay down a ruler so the misses above and below balance as well as possible. Regression calculates that ruler's tilt and where it crosses the side.",
            concepts=("least squares", "covariance", "slope", "intercept", "prediction"),
        ),
    ]
)


_CATEGORY_ORDER = {category["id"]: index for index, category in enumerate(CATEGORIES)}
LESSONS.sort(key=lambda item: (_CATEGORY_ORDER[item["category"]], item["order"]))

for _lesson in LESSONS:
    _lesson.update(GUIDANCE[_lesson["id"]])


LESSONS_BY_ID = {item["id"]: item for item in LESSONS}


def get_lesson(lesson_id: str) -> dict:
    try:
        return LESSONS_BY_ID[lesson_id]
    except KeyError as error:
        raise KeyError(f"Unknown lesson: {lesson_id}") from error


def lesson_directory(item: dict):
    return ASSIGNMENTS_DIR / item["category"] / item["id"].split("/", 1)[1]
