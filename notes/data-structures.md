# Python Data Structures: Lists, Tuples, Dictionaries and Comprehensions

A reference guide with the essentials for everyday use and real projects.

---

## Contents

1. [Overview: which one to choose?](#1-overview-which-one-to-choose)
2. [Lists (`list`)](#2-lists-list)
3. [Tuples (`tuple`)](#3-tuples-tuple)
4. [Dictionaries (`dict`)](#4-dictionaries-dict)
5. [Sets (`set`): bonus](#5-sets-set-bonus)
6. [Comprehensions](#6-comprehensions)
7. [Common pitfalls](#7-common-pitfalls)
8. [Performance](#8-performance)
9. [Full example: bank statement](#9-full-example-bank-statement)
10. [Exercises](#10-exercises)
11. [Cheat sheet](#11-cheat-sheet)

---

## 1. Overview: which one to choose?

| | List | Tuple | Dictionary | Set |
|---|---|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{"a": 1}` | `{1, 2, 3}` |
| Access by | index | index | key | no direct access |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Ordered | ✅ | ✅ | ✅ (insertion order) | ❌ |
| Duplicates | ✅ | ✅ | unique keys | ❌ |
| Can be a dict key | ❌ | ✅ (if its contents are immutable) | ❌ | ❌ |

**Questions to help you decide:**

- Will I look things up by **name/identifier**? → **dictionary**
- Will I access by **position**, and will the collection **change**? → **list**
- Is it a **fixed group** of values where each position has a meaning? → **tuple**
- Do I only care whether something **exists**, and want to **remove duplicates**? → **set**

---

## 2. Lists (`list`)

An **ordered**, **mutable** collection.

### 2.1 Creating

```python
empty = []
empty = list()
numbers = [1, 2, 3, 4, 5]
mixed = [1, "text", 3.5, True, None]   # possible, but avoid it
letters = list("abc")                  # ['a', 'b', 'c']
span = list(range(5))                  # [0, 1, 2, 3, 4]
zeros = [0] * 5                        # [0, 0, 0, 0, 0]
```

### 2.2 Accessing

Indexes start at **0**. Negative indexes count from the end.

```python
fruits = ["apple", "pear", "banana", "kiwi", "grape"]

fruits[0]      # 'apple'
fruits[2]      # 'banana'
fruits[-1]     # 'grape'   (last)
fruits[-2]     # 'kiwi'    (second to last)
fruits[10]     # IndexError
len(fruits)    # 5
```

### 2.3 Slicing

Syntax: `list[start:stop:step]`. The `stop` index is **not included**.

```python
fruits[1:3]    # ['pear', 'banana']
fruits[:2]     # ['apple', 'pear']
fruits[2:]     # ['banana', 'kiwi', 'grape']
fruits[-2:]    # ['kiwi', 'grape']            (last 2)
fruits[::2]    # ['apple', 'banana', 'grape'] (every 2nd)
fruits[::-1]   # ['grape', 'kiwi', 'banana', 'pear', 'apple'] (reversed)
fruits[:]      # (shallow) copy of the list
```

Slices **never raise an error** for out-of-range indexes: `fruits[2:100]` returns whatever exists.

### 2.4 Adding

```python
nums = [1, 2, 3]
nums.append(4)          # [1, 2, 3, 4]          one element at the end
nums.insert(0, 0)       # [0, 1, 2, 3, 4]       at a given position
nums.extend([5, 6])     # [0, 1, 2, 3, 4, 5, 6] several elements
nums += [7]             # same as extend
joined = [1, 2] + [3]   # creates a NEW list: [1, 2, 3]
```

Careful: `append` with a list adds the whole list as **one** element.

```python
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]
a = [1, 2]
a.extend([3, 4])   # [1, 2, 3, 4]
```

### 2.5 Removing

```python
nums = [10, 20, 30, 20, 40]
nums.remove(20)     # removes the 1st occurrence of the VALUE → [10, 30, 20, 40]
x = nums.pop()      # removes and returns the last one → x = 40
y = nums.pop(0)     # removes and returns by INDEX → y = 10
del nums[0]         # deletes by index, returns nothing
nums.clear()        # empties it → []
```

`remove` raises `ValueError` if the value doesn't exist; `pop` raises `IndexError` if the list is empty.

### 2.6 Changing

```python
nums = [1, 2, 3, 4, 5]
nums[0] = 100          # [100, 2, 3, 4, 5]
nums[1:3] = [20, 30]   # [100, 20, 30, 4, 5]
```

### 2.7 Searching

```python
fruits = ["apple", "pear", "banana", "pear"]
"pear" in fruits        # True
"kiwi" not in fruits    # True
fruits.index("pear")    # 1   (1st occurrence; ValueError if missing)
fruits.count("pear")    # 2
```

### 2.8 Sorting

```python
nums = [3, 1, 4, 1, 5]

nums.sort()                     # sorts the list IN PLACE, returns None
nums.sort(reverse=True)         # descending
ordered = sorted(nums)          # returns a NEW list, original untouched

words = ["banana", "Kiwi", "apple"]
sorted(words, key=len)              # by length
sorted(words, key=str.lower)        # ignoring case

people = [{"name": "Ana", "age": 30}, {"name": "Rui", "age": 25}]
sorted(people, key=lambda p: p["age"])   # by a dictionary field
```

Classic mistake:

```python
nums = nums.sort()   # nums becomes None!
```

### 2.9 Useful functions

```python
nums = [4, 8, 15, 16, 23, 42]
sum(nums)         # 108
min(nums)         # 4
max(nums)         # 42
len(nums)         # 6
any(n > 40 for n in nums)   # True  (at least one)
all(n > 0 for n in nums)    # True  (all of them)
list(reversed(nums))        # reversed (copy)
```

### 2.10 Looping

```python
fruits = ["apple", "pear", "banana"]

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):           # with index
    print(i, fruit)

for i, fruit in enumerate(fruits, start=1):  # index starting at 1
    print(f"{i}. {fruit}")

prices = [1.0, 0.8, 0.5]
for fruit, price in zip(fruits, prices):     # two lists side by side
    print(fruit, price)
```

### 2.11 Copying

```python
a = [1, 2, 3]
b = a           # NOT a copy: both variables point to the same list
b.append(4)
print(a)        # [1, 2, 3, 4]  ← a changed too!

c = a.copy()    # shallow copy (also: a[:] or list(a))
c.append(5)
print(a)        # [1, 2, 3, 4]  ← a did not change
```

For lists inside lists, a shallow copy isn't enough:

```python
import copy

matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()
shallow[0].append(99)
print(matrix)   # [[1, 2, 99], [3, 4]]  ← changed!

deep = copy.deepcopy(matrix)   # copies everything, at every level
```

---

## 3. Tuples (`tuple`)

An **ordered**, **immutable** collection.

### 3.1 Creating

```python
empty = ()
point = (3, 4)
point = 3, 4              # parentheses are optional
single = (5,)             # the COMMA is what makes it a tuple
not_a_tuple = (5)         # this is just the number 5
from_list = tuple([1, 2, 3])
```

### 3.2 Accessing

Same as lists: indexes, negative indexes and slices.

```python
date = (2026, 11, 15)
date[0]     # 2026
date[-1]    # 15
date[:2]    # (2026, 11)
len(date)   # 3
```

### 3.3 Immutability

```python
date[0] = 2027        # TypeError
date.append(16)       # AttributeError
```

To "change" it, you build a new tuple:

```python
new_date = (2027,) + date[1:]   # (2027, 11, 15)
```

Note: the tuple is immutable, but a mutable object **inside** it can still change.

```python
t = (1, [2, 3])
t[1].append(4)   # works → (1, [2, 3, 4])
```

### 3.4 Unpacking

This is where tuples shine.

```python
lat, lon = (38.68, -9.16)

year, month, day = (2026, 11, 15)

first, *rest = (1, 2, 3, 4)      # first=1, rest=[2, 3, 4]
*start, last = (1, 2, 3, 4)      # start=[1, 2, 3], last=4
a, _, c = (1, 2, 3)              # _ = "I don't care about this one"

# Swap variables without a temporary variable
x, y = 1, 2
x, y = y, x      # x=2, y=1
```

### 3.5 Returning multiple values from a function

```python
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lowest, highest, average = stats([4, 8, 15])
```

### 3.6 Methods

There are only two, because a tuple can't be changed:

```python
t = (1, 2, 2, 3)
t.count(2)   # 2
t.index(3)   # 3
```

### 3.7 Tuples as dictionary keys

```python
distances = {
    ("Lisbon", "Porto"): 313,
    ("Lisbon", "Faro"): 278,
}
distances[("Lisbon", "Porto")]   # 313
```

A list can't be a key (`TypeError: unhashable type: 'list'`).

### 3.8 `namedtuple`: tuples with names

When a tuple has many fields, `t[3]` stops being readable.

```python
from collections import namedtuple

Expense = namedtuple("Expense", ["date", "category", "amount"])

e = Expense("2026-11-03", "Groceries", 42.30)
e.category     # 'Groceries'  (access by name)
e[2]           # 42.3         (index access still works)
```

### 3.9 When to use a tuple instead of a list?

- The data **shouldn't change** (coordinates, dates, fixed settings).
- Each position has its **own meaning** (a record), rather than being "many of the same thing".
- You need it as a **dictionary key** or a set element.
- Returning **multiple values** from a function.

---

## 4. Dictionaries (`dict`)

**Key → value** pairs. Keys are unique and immutable (strings, numbers, tuples).

### 4.1 Creating

```python
empty = {}                                   # {} is a dict, NOT a set
empty = dict()
person = {"name": "Ana", "age": 30}
person = dict(name="Ana", age=30)            # keys must be valid identifiers
from_pairs = dict([("a", 1), ("b", 2)])
from_lists = dict(zip(["a", "b"], [1, 2]))   # {'a': 1, 'b': 2}
with_default = dict.fromkeys(["a", "b"], 0)  # {'a': 0, 'b': 0}
```

### 4.2 Accessing

```python
person = {"name": "Ana", "age": 30}

person["name"]                  # 'Ana'
person["email"]                 # KeyError
person.get("email")             # None (no error)
person.get("email", "no email") # 'no email'
"name" in person                # True  (checks KEYS, not values)
"Ana" in person.values()        # True
person[0]                       # KeyError: there are no indexes in a dict
```

**Rule:** use `[]` when the key **must** exist (failing early is good); use `.get()` when it **might** be missing.

### 4.3 Adding and changing

```python
person["age"] = 31               # changes (key exists)
person["email"] = "ana@x.pt"     # adds (key doesn't exist)

person.update({"city": "Lisbon", "age": 32})   # several at once

person.setdefault("country", "PT")   # only sets it if it doesn't exist yet
```

### 4.4 Removing

```python
email = person.pop("email")            # removes and returns
person.pop("phone", None)              # no error if missing
del person["city"]                     # removes (KeyError if missing)
last = person.popitem()                # removes the last inserted pair
person.clear()                         # empties it
```

### 4.5 Merging dictionaries

```python
defaults = {"theme": "light", "language": "pt"}
user = {"theme": "dark"}

merged = defaults | user       # {'theme': 'dark', 'language': 'pt'}  (Python 3.9+)
merged = {**defaults, **user}  # same result, works in older versions
defaults |= user               # updates defaults in place
```

When a key is repeated, **the one on the right wins**.

### 4.6 Looping

```python
prices = {"bread": 1.20, "milk": 0.95, "coffee": 4.50}

for product in prices:                 # keys
    print(product)

for price in prices.values():          # values
    print(price)

for product, price in prices.items():  # pairs (the most common)
    print(f"{product}: {price:.2f}€")

for product in sorted(prices):         # keys in alphabetical order
    print(product)

# Sort by value
for product, price in sorted(prices.items(), key=lambda pair: pair[1]):
    print(product, price)
```

Don't change a dictionary's size while looping over it:

```python
for k in prices:
    if prices[k] < 1:
        del prices[k]      # RuntimeError: dictionary changed size during iteration

for k in list(prices):     # looping over a COPY of the keys fixes it
    if prices[k] < 1:
        del prices[k]
```

### 4.7 Counting and grouping

Three ways to count occurrences, from most manual to most idiomatic:

```python
words = ["apple", "pear", "apple", "kiwi", "apple"]

# 1. Manually with get
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

# 2. defaultdict
from collections import defaultdict
counts = defaultdict(int)          # new keys start at 0
for w in words:
    counts[w] += 1

# 3. Counter (the best for counting)
from collections import Counter
counts = Counter(words)            # Counter({'apple': 3, 'pear': 1, 'kiwi': 1})
counts.most_common(1)              # [('apple', 3)]
```

Grouping items by a key:

```python
from collections import defaultdict

expenses = [("Groceries", 42.3), ("Restaurants", 18.0), ("Groceries", 12.5)]

by_category = defaultdict(list)    # new keys start as []
for category, amount in expenses:
    by_category[category].append(amount)

# {'Groceries': [42.3, 12.5], 'Restaurants': [18.0]}
```

### 4.8 Nested dictionaries

Very common when reading JSON or API responses.

```python
user = {
    "name": "Ana",
    "address": {"city": "Almada", "postcode": "2800-000"},
    "accounts": [
        {"bank": "A", "balance": 1200},
        {"bank": "B", "balance": 300},
    ],
}

user["address"]["city"]          # 'Almada'
user["accounts"][1]["bank"]      # 'B'

# Safe access when a level might be missing
user.get("job", {}).get("company", "unknown")   # 'unknown'
```

Read it left to right: each `[...]` goes one level deeper.

### 4.9 Valid keys

```python
ok = {1: "a", "x": "b", (1, 2): "c", None: "d", True: "e"}
bad = {[1, 2]: "a"}      # TypeError: unhashable type: 'list'
```

Fun fact: `True == 1`, so `{1: "a", True: "b"}` results in `{1: 'b'}`.

---

## 5. Sets (`set`): bonus

An **unordered** collection with **no duplicates**. Useful for removing repeats and for fast membership checks.

```python
empty = set()                    # {} creates a dict, not a set!
s = {1, 2, 3, 3, 2}              # {1, 2, 3}
unique = set([1, 1, 2, 3, 3])    # {1, 2, 3}

s.add(4)
s.discard(10)     # removes it if present, no error (remove() raises one)
3 in s            # True, and very fast

a = {1, 2, 3}
b = {2, 3, 4}
a | b    # {1, 2, 3, 4}  union
a & b    # {2, 3}        intersection
a - b    # {1}           difference
a ^ b    # {1, 4}        symmetric difference
```

Removing duplicates **while keeping the order** (a `set` loses the order):

```python
names = ["Ana", "Rui", "Ana", "Marta", "Rui"]
unique = list(dict.fromkeys(names))   # ['Ana', 'Rui', 'Marta']
```

---

## 6. Comprehensions

A compact way to **build a new collection from an iterable**.

### 6.1 The four kinds

```python
nums = [1, 2, 3, 4]

[n * 2 for n in nums]           # list:      [2, 4, 6, 8]
{n * 2 for n in nums}           # set:       {8, 2, 4, 6}
{n: n * 2 for n in nums}        # dict:      {1: 2, 2: 4, 3: 6, 4: 8}
(n * 2 for n in nums)           # generator: <generator object ...>
tuple(n * 2 for n in nums)      # tuple:     (2, 4, 6, 8)
```

**There is no tuple comprehension.** Parentheses create a generator.

What separates a *set* from a *dict* comprehension is the colon in `key: value`.

### 6.2 General structure

```
[ EXPRESSION   for VARIABLE in ITERABLE   if CONDITION ]
  └─ what's kept   └─ where it comes from    └─ filter (optional)
```

Equivalent loop:

```python
result = []
for VARIABLE in ITERABLE:
    if CONDITION:
        result.append(EXPRESSION)
```

### 6.3 List comprehension

```python
# Transform
squares = [n ** 2 for n in range(1, 6)]            # [1, 4, 9, 16, 25]
upper = [s.upper() for s in ["a", "b"]]            # ['A', 'B']
cleaned = [s.strip() for s in ["  ana ", "rui  "]] # ['ana', 'rui']

# Filter (if at the END)
evens = [n for n in range(10) if n % 2 == 0]       # [0, 2, 4, 6, 8]

# Transform conditionally (if/else BEFORE the for)
labels = ["even" if n % 2 == 0 else "odd" for n in range(4)]
# ['even', 'odd', 'even', 'odd']

# Both at the same time
[n * 10 if n > 2 else n for n in range(6) if n != 4]
# [0, 1, 2, 30, 50]
```

**Key difference:**

| Position | Purpose | Example |
|---|---|---|
| `if` at the **end** | **filters**: decides whether it goes in | `[x for x in l if x > 0]` |
| `if/else` **before the `for`** | **transforms**: decides the value | `[x if x > 0 else 0 for x in l]` |

`[x for x in l if x > 0 else 0]` → **SyntaxError**. There's no `else` at the end.

### 6.4 Dict comprehension

```python
# From an iterable
squares = {n: n ** 2 for n in range(1, 5)}          # {1: 1, 2: 4, 3: 9, 4: 16}
lengths = {w: len(w) for w in ["ana", "marta"]}     # {'ana': 3, 'marta': 5}

# From another dictionary (.items()!)
prices = {"bread": 1.20, "milk": 0.95, "coffee": 4.50}

with_vat = {p: round(v * 1.23, 2) for p, v in prices.items()}
expensive = {p: v for p, v in prices.items() if v > 1}   # {'bread': 1.2, 'coffee': 4.5}
inverted = {v: p for p, v in prices.items()}             # values become keys

# From two lists
names = ["Ana", "Rui"]
ages = [30, 25]
people = {n: a for n, a in zip(names, ages)}        # {'Ana': 30, 'Rui': 25}

# Index a list of records by a field
users = [{"id": 1, "name": "Ana"}, {"id": 2, "name": "Rui"}]
by_id = {u["id"]: u for u in users}
by_id[2]["name"]    # 'Rui', direct lookup without scanning the list
```

If two items produce the same key, **the last one wins**.

### 6.5 List vs dict comprehension: when to use each

```python
prices = {"bread": 1.20, "milk": 0.95, "coffee": 4.50}

[p for p, v in prices.items() if v > 1]        # ['bread', 'coffee']             → just the names
{p: v for p, v in prices.items() if v > 1}     # {'bread': 1.2, 'coffee': 4.5}   → name AND price
```

- You need a **sequence of values** → *list comprehension*.
- You need to **associate** each value with a key to look it up later → *dict comprehension*.

### 6.6 Nested comprehensions

The order of the `for` clauses is **the same as in regular nested loops**.

```python
# Flatten a list of lists
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]   # [1, 2, 3, 4, 5, 6]

# Equivalent to:
flat = []
for row in matrix:
    for n in row:
        flat.append(n)

# Build a matrix (a comprehension INSIDE a comprehension)
times_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# All combinations
[(c, s) for c in ["red", "blue"] for s in ["S", "M"]]
# [('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]
```

### 6.7 Generators: when you don't need the list

If you're only going to **aggregate** (`sum`, `max`, `any`, ...), use a generator. It doesn't build the list in memory.

```python
total = sum(n ** 2 for n in range(1_000_000))     # no extra brackets needed
has_negatives = any(v < 0 for v in [3, -1, 5])    # stops at the first True
```

### 6.8 When NOT to use comprehensions

```python
# ❌ For side effects: builds a useless list of None
[print(x) for x in nums]

# ✅ Use a loop
for x in nums:
    print(x)
```

```python
# ❌ Unreadable
r = {k: [x * 2 for x in v if x > 0] for k, v in d.items() if k.startswith("a") and len(v) > 2}

# ✅ Split it into steps or use a loop with clear names
```

Rule: if you can't read it in one go, or it needs `try/except`, use a `for` loop.

---

## 7. Common pitfalls

### 7.1 Assignment is not copying

```python
a = [1, 2]
b = a
b.append(3)
print(a)   # [1, 2, 3]
```

Use `a.copy()` or `copy.deepcopy(a)` (see 2.11).

### 7.2 Multiplied lists

```python
grid = [[0] * 3] * 3          # ❌ 3 references to the SAME list
grid[0][0] = 1
print(grid)                   # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

grid = [[0] * 3 for _ in range(3)]   # ✅ 3 independent lists
```

### 7.3 Mutable default arguments

```python
def add(x, items=[]):       # ❌ the same list is shared between calls
    items.append(x)
    return items

def add(x, items=None):     # ✅
    if items is None:
        items = []
    items.append(x)
    return items
```

### 7.4 Changing a collection while looping over it

```python
nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)          # ❌ skips elements

nums = [n for n in nums if n % 2 != 0]   # ✅ build a new one
```

### 7.5 `sort()` returns `None`

```python
nums = nums.sort()       # ❌ nums = None
nums.sort()              # ✅ sorts in place
nums = sorted(nums)      # ✅ builds a new one
```

### 7.6 Single-element tuple

```python
t = (5)     # int
t = (5,)    # tuple
```

### 7.7 `{}` is a dictionary

```python
s = {}          # dict
s = set()       # empty set
```

### 7.8 `in` on a dictionary checks keys

```python
d = {"a": 1}
1 in d             # False
1 in d.values()    # True
```

---

## 8. Performance

| Operation | List | Dictionary / Set |
|---|---|---|
| Access by index / key | O(1) | O(1) |
| `x in collection` | **O(n)**: scans everything | **O(1)**: instant |
| Append at the end | O(1) | O(1) |
| Insert/remove at the start | O(n) | — |

In practice: if you'll do **many `in` checks**, convert to a `set` or `dict` first.

```python
valid_ids = [...]          # 100,000 elements
# ❌ Slow: every `in` scans the list
found = [x for x in requests if x in valid_ids]

# ✅ Fast
valid_ids = set(valid_ids)
found = [x for x in requests if x in valid_ids]
```

To add/remove frequently at the **start**, use `collections.deque`.

---

## 9. Full example: bank statement

Puts it all together: a list of records, dictionaries, tuples, comprehensions, `defaultdict` and `Counter`.

```python
from collections import defaultdict, Counter

# A list (grows over time) of dictionaries (named fields)
transactions = [
    {"date": (2026, 11, 2), "description": "Continente", "category": "Groceries",     "amount": -42.30},
    {"date": (2026, 11, 3), "description": "Salary",     "category": "Income",        "amount": 1800.00},
    {"date": (2026, 11, 5), "description": "Pingo Doce", "category": "Groceries",     "amount": -18.75},
    {"date": (2026, 11, 7), "description": "Tasca",      "category": "Restaurants",   "amount": -24.00},
    {"date": (2026, 11, 9), "description": "Netflix",    "category": "Subscriptions", "amount": -13.99},
    {"date": (2026, 11, 9), "description": "Lidl",       "category": "Groceries",     "amount": -31.10},
]

# 1. Expenses only (list comprehension with a filter)
expenses = [t for t in transactions if t["amount"] < 0]

# 2. Total spent (generator inside sum)
total_spent = sum(-t["amount"] for t in expenses)
print(f"Total spent: {total_spent:.2f}€")             # 130.14€

# 3. Unique categories (set comprehension)
categories = {t["category"] for t in expenses}

# 4. Total per category (defaultdict)
by_category = defaultdict(float)
for t in expenses:
    by_category[t["category"]] += -t["amount"]

# 5. Percentage per category (dict comprehension)
percentages = {
    cat: round(amount / total_spent * 100, 1)
    for cat, amount in by_category.items()
}

# 6. Sort categories from most to least expensive
for cat, amount in sorted(by_category.items(), key=lambda pair: pair[1], reverse=True):
    print(f"{cat:<14} {amount:>8.2f}€  ({percentages[cat]}%)")
# Groceries         92.15€  (70.8%)
# Restaurants       24.00€  (18.4%)
# Subscriptions     13.99€  (10.7%)

# 7. Where I shop most often (Counter)
frequency = Counter(t["description"] for t in expenses)
print(frequency.most_common(2))

# 8. Group by day (the date tuple as a key)
by_day = defaultdict(list)
for t in transactions:
    by_day[t["date"]].append(t["description"])
print(by_day[(2026, 11, 9)])     # ['Netflix', 'Lidl']

# 9. Unpack the date tuple
for t in expenses:
    year, month, day = t["date"]
    print(f"{day:02d}/{month:02d}/{year}  {t['description']}")
```

---

## 10. Exercises

One per topic. Try to solve them before looking for help.

**Lists.** Given a list of daily temperatures, return a new list with the 3-day moving average (the average of each day and the two before it).
*Hint:* which slice gives you "the three elements ending at index `i`"? From which index does that slice always have three elements?

**Tuples.** Write a function that takes a list of `(x, y)` points and returns a tuple with the point closest to and the point farthest from the origin.
*Hint:* `min` and `max` accept `key=`. What's the distance from `(x, y)` to the origin? Do you really need the square root just to compare?

**Dictionaries.** Given a text, build a dictionary where each key is a first letter and the value is the list of words starting with it, with no repeats and in alphabetical order.
*Hint:* which structure from section 4.7 creates empty lists on its own? When do you remove duplicates: while inserting, or at the end?

**Comprehensions.** Starting from `transactions` (section 9), build a `{description: amount}` dictionary in a single dict comprehension, containing only expenses above 20€, with the amount as a positive number.
*Hint:* where does the filter go, and where does the transformation go? Does "above 20€" apply to the original amount or to the positive one?

---

## 11. Cheat sheet

```python
# LIST ───────────────────────────────────────────────
l = [1, 2, 3]
l[0], l[-1], l[1:3], l[::-1]
l.append(x); l.extend([..]); l.insert(i, x)
l.pop(); l.pop(i); l.remove(x); del l[i]
l.sort(); sorted(l, key=..., reverse=True)
x in l; l.index(x); l.count(x); len(l)
l.copy()

# TUPLE ──────────────────────────────────────────────
t = (1, 2, 3); t = (1,)
t[0], t[-1], t[1:]
a, b, c = t; first, *rest = t
t.count(x); t.index(x)

# DICTIONARY ─────────────────────────────────────────
d = {"a": 1}
d["a"]; d.get("z", default); "a" in d
d["b"] = 2; d.update({...}); d.setdefault(k, v)
d.pop(k); d.pop(k, None); del d[k]
d.keys(); d.values(); d.items()
d1 | d2; {**d1, **d2}

# SET ────────────────────────────────────────────────
s = set(); s = {1, 2}
s.add(x); s.discard(x); x in s
a | b; a & b; a - b

# COMPREHENSIONS ─────────────────────────────────────
[expr for x in it if cond]               # list
{k: v for x in it if cond}               # dictionary
{expr for x in it}                       # set
(expr for x in it)                       # generator
[a if c else b for x in it]              # if/else transforms (before the for)
[x for sub in lst for x in sub]          # flatten

# COLLECTIONS ────────────────────────────────────────
from collections import defaultdict, Counter, namedtuple, deque
defaultdict(list); defaultdict(int)
Counter(it).most_common(n)
namedtuple("Name", ["field1", "field2"])
```
