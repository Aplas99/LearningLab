"""Assignment scaffolding kept separate from the core lesson prose."""


GUIDANCE = {
    "python/syntax-output": {
        "assignment_steps": [
            "Leave the three starter assignments unchanged; they give names to the values you need.",
            "Write `print(f\"...\")` beneath them and place each variable name inside braces where its value belongs.",
            "Run `python3 solution.py` and compare every space and punctuation mark with the requested output.",
        ],
        "hint": "Your f-string needs `{name}`, `{completed}`, and `{total}`. Text outside the braces is printed literally.",
    },
    "python/variables": {
        "assignment_steps": [
            "Calculate the sandwich subtotal from `sandwich_price` and `sandwiches`.",
            "Calculate the drink subtotal the same way.",
            "Add both subtotals and assign that expression to `order_total`.",
        ],
        "hint": "The shape is `(price * quantity) + (price * quantity)`, using the four provided names.",
    },
    "python/functions": {
        "assignment_steps": [
            "Keep the `def rectangle_perimeter(length, width):` line; the two names receive values when tests call the function.",
            "Build an expression for two lengths plus two widths.",
            "Replace `pass` with a `return` statement containing that expression.",
        ],
        "hint": "Calling `rectangle_perimeter(8, 3)` makes `length` equal 8 and `width` equal 3 for that call.",
    },
    "python/types-casting": {
        "assignment_steps": [
            "Convert `celsius_text` with `float()` and store the result in a local variable.",
            "Apply the supplied temperature formula to the converted number.",
            "Return `round(result, 1)`.",
        ],
        "hint": "Arithmetic with the original text will fail; conversion must happen before multiplication or addition.",
    },
    "python/strings": {
        "assignment_steps": [
            "Call `strip()` and `lower()` on the title.",
            "Call `split()` with no argument so repeated whitespace becomes word boundaries.",
            "Join those words with `\"-\".join(...)` and return the result.",
        ],
        "hint": "A useful pipeline is clean text -> list of words -> one hyphenated string.",
    },
    "python/collections": {
        "assignment_steps": [
            "Create a dictionary literal with the three exact keys named in the assignment.",
            "Use `name` for the name value and index 0 for the first skill.",
            "Use `len(skills)` for the count, then return the dictionary.",
        ],
        "hint": "Dictionary entries have the form `\"key\": value`; only the keys are fixed text here.",
    },
    "python/tuples-sets": {
        "assignment_steps": [
            "Convert both supplied iterables to sets.",
            "Use set intersection to keep only values found in both.",
            "Sort the shared values, convert that result to a tuple, and return it.",
        ],
        "hint": "`set(first) & set(second)` produces the unique overlap.",
    },
    "python/conditionals": {
        "assignment_steps": [
            "Check the under-13 case first and return 8.",
            "Use `elif` for ages below 65; reaching it already means the age is at least 13.",
            "Use `else` for every remaining age and return 9.",
        ],
        "hint": "Boundary tests matter: age 12, 13, 64, and 65 should land in the intended branches.",
    },
    "python/loops": {
        "assignment_steps": [
            "Keep `total = 0` as the accumulator before the loop.",
            "Loop directly over each value in `distances` and use an `if` to test it against `minimum`.",
            "Add qualifying values to `total`, then return after the loop ends.",
        ],
        "hint": "Indent the addition inside the `if`; keep `return total` outside the loop so every distance is considered.",
    },
    "python/while-loops": {
        "assignment_steps": [
            "Start a `months` counter at zero.",
            "While the balance is below the goal, add one deposit and increment the counter.",
            "Return the counter after the condition becomes false.",
        ],
        "hint": "If the starting balance already meets the goal, the loop should run zero times.",
    },
    "python/arguments-scope": {
        "assignment_steps": [
            "Use `sum(prices)` to calculate the local subtotal gathered by `*prices`.",
            "Multiply the subtotal by `1 - discount`, then multiply that result by `1 + tax_rate`.",
            "Return the final value rounded to two decimals.",
        ],
        "hint": "Discount comes first in this contract; tax applies to the discounted subtotal.",
    },
    "python/comprehensions": {
        "assignment_steps": [
            "Unpack each record as `name, score` inside a list comprehension.",
            "Filter with `if score >= 70` and produce `name.lower()` for accepted records.",
            "Pass the resulting list to `sorted()` and return it.",
        ],
        "hint": "Build the unsorted comprehension first; wrap it in `sorted(...)` only after the filter works.",
    },
    "python/modules-json": {
        "assignment_steps": [
            "Parse `payload` with `json.loads()` and retrieve its `items` list.",
            "For each item, multiply its `price` by its `quantity` and add that to a running total.",
            "Return the total rounded to two decimals; do not catch JSON parsing errors in this lesson.",
        ],
        "hint": "After parsing, each item is a dictionary, so its fields use `item[\"price\"]` syntax.",
    },
    "python/exceptions": {
        "assignment_steps": [
            "Check for an empty input and raise the required empty-values error before dividing.",
            "Inside a small `try` block, create a list of floats from the supplied values.",
            "Catch only `TypeError` and `ValueError`, raise the requested numeric-values error, then average and round the converted list.",
        ],
        "hint": "Use `raise ValueError(...) from error` inside the `except` block to preserve the original cause.",
    },
    "python/file-handling": {
        "assignment_steps": [
            "Open the supplied path with a `with` block and UTF-8 encoding.",
            "Loop over the file, strip each line, and skip it when the stripped text is empty.",
            "Count every remaining line and separately count lines whose lowercase text contains `error`.",
        ],
        "hint": "Maintain two integer counters and return them using the exact dictionary keys in the assignment.",
    },
    "oop/classes": {
        "assignment_steps": [
            "In `__init__`, assign the supplied owner and balance to `self.owner` and `self.balance`.",
            "In `deposit`, reject amounts at or below zero with `ValueError`.",
            "Add the amount to this object's balance and return the updated balance.",
        ],
        "hint": "Every account keeps separate state because assignments use `self`, not standalone variable names.",
    },
    "oop/encapsulation": {
        "assignment_steps": [
            "Store `name` in `__init__`, then assign the initial value through `self.price` so the setter validates it.",
            "Have the property getter return the internal `_price` value.",
            "In the setter, reject negatives and otherwise assign to `_price`.",
        ],
        "hint": "Do not assign `self.price = value` inside the price setter; that would call the same setter forever.",
    },
    "oop/class-methods": {
        "assignment_steps": [
            "Make `is_valid` return true only when the value is an int or float and is at least zero.",
            "Use that static method in `__init__`; raise `ValueError` before storing an invalid value.",
            "In `from_minutes`, validate the input and return `cls(minutes * 60)`.",
        ],
        "hint": "The class method should construct through `cls(...)`, not hard-code `TimeSpan(...)`.",
    },
    "oop/inheritance": {
        "assignment_steps": [
            "Give each subclass an `__init__` that calls `super().__init__(name)` and stores its additional values.",
            "Override `weekly_pay` in `HourlyEmployee` with hours times rate.",
            "Override it in `SalariedEmployee` with annual salary divided by 52.",
        ],
        "hint": "The base class owns the shared `name`; subclasses own only the data unique to their pay calculation.",
    },
    "oop/composition": {
        "assignment_steps": [
            "Store title and seconds on each `Song` instance.",
            "Store the playlist name and initialize `self.songs` as an empty list.",
            "Append in `add`; in `duration`, loop over song objects and total each `song.seconds`.",
        ],
        "hint": "The playlist has Song objects, so access their duration through an attribute rather than treating them as numbers.",
    },
    "oop/special-methods": {
        "assignment_steps": [
            "Store amount and currency, then format `__str__` with the amount at two decimal places.",
            "In `__eq__`, compare both fields when the other value is a `Money` object.",
            "In `__add__`, reject different currencies and otherwise return a new `Money` with the summed amount.",
        ],
        "hint": "Addition should not mutate either original object; construct and return a third object.",
    },
    "math/numeric-precision": {
        "assignment_steps": [
            "Convert the total to `Decimal` from its string form, then convert dollars to an integer number of cents.",
            "Use integer division and remainder to find the base share and leftover cents.",
            "Build one result per person, adding one cent to the earliest shares while leftovers remain, then convert cents back to dollars.",
        ],
        "hint": "`divmod(total_cents, people)` returns both the base cents and the number of people who receive one extra cent.",
    },
    "math/unit-conversion": {
        "assignment_steps": [
            "Reject a negative milliliter value with `ValueError`.",
            "Divide milliliters by 236.588 because that many milliliters make one cup.",
            "Return the result rounded to three decimals.",
        ],
        "hint": "Check the ratio direction with one full cup: 236.588 milliliters must become 1.0.",
    },
    "math/linear-equations": {
        "assignment_steps": [
            "Reject a negative distance with `ValueError`.",
            "Model the fare as intercept plus slope times miles: base charge plus per-mile charge.",
            "Return the fare rounded to two decimals.",
        ],
        "hint": "In `y = mx + b`, miles is `x`, 2.20 is `m`, and 3.50 is `b`.",
    },
    "math/distance": {
        "assignment_steps": [
            "Unpack both `(x, y)` tuples into separate coordinate names.",
            "Calculate the horizontal and vertical differences.",
            "Use `math.hypot(dx, dy)` or the square-root formula, then round to two decimals.",
        ],
        "hint": "Distances may use negative coordinate differences, but squaring or `hypot` makes direction irrelevant.",
    },
    "math/statistics": {
        "assignment_steps": [
            "Reject an empty list, then create a sorted copy so the input is not changed.",
            "Compute the mean from the original values.",
            "Choose the middle sorted value for odd counts or average the two middle values for even counts.",
        ],
        "hint": "For an even count `n`, the middle indexes are `n // 2 - 1` and `n // 2`.",
    },
    "math/spread": {
        "assignment_steps": [
            "Reject empty input and calculate the mean.",
            "For every value, square `value - mean`; sum those squares and divide by the population size for variance.",
            "Take the square root for standard deviation and round both returned values.",
        ],
        "hint": "This lesson asks for population variance, so divide by `len(values)`, not `len(values) - 1`.",
    },
    "math/linear-regression": {
        "assignment_steps": [
            "Validate the point count, separate x and y values, and calculate both means.",
            "Compute `sum((x - x_mean) * (y - y_mean))` and divide it by `sum((x - x_mean) ** 2)` for the slope.",
            "Reject a zero denominator, calculate `intercept = y_mean - slope * x_mean`, and return both rounded values.",
        ],
        "hint": "A zero x denominator means every x value is equal, so no unique non-vertical regression line exists.",
    },
    "math/compound-interest": {
        "assignment_steps": [
            "Validate principal, rate, and years as non-negative and compounds per year as at least one.",
            "Calculate the periodic rate `annual_rate / compounds_per_year` and total period count `compounds_per_year * years`.",
            "Apply `principal * (1 + periodic_rate) ** period_count` and return two decimals.",
        ],
        "hint": "Keep the annual rate as a decimal: six percent is `0.06`, not `6`.",
    },
}
