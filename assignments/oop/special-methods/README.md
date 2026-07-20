# Special methods

Create `Money(amount, currency)` with `__str__`, `__eq__`, and `__add__`. String form is `USD 12.50`. Equal objects have the same amount and currency. Addition returns new Money and raises `ValueError` when currencies differ.

Run from this assignment folder or the project root:

```bash
python3 -m learnlab check oop/special-methods
```
