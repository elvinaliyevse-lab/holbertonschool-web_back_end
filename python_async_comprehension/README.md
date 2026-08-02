# Python - Async Comprehension

Asynchronous generators and async comprehensions.

| File | Task |
| --- | --- |
| `0-async_generator.py` | `async_generator()` yields 10 random floats, one per second |
| `1-async_comprehension.py` | `async_comprehension()` collects them with `async for` |
| `2-measure_runtime.py` | `measure_runtime()` times four parallel comprehensions |

## Why task 2 takes ~10 seconds and not ~40

Each `async_comprehension()` call consumes the generator's ten yields, and
each yield is preceded by `await asyncio.sleep(1)` — so one comprehension
takes about 10 seconds, and those 10 seconds are sequential *within* that
call.

`asyncio.gather` starts all four comprehensions on the same event loop.
Every `await asyncio.sleep(1)` hands control back to the loop, which runs the
other three while that one waits. The four sets of sleeps therefore overlap
almost perfectly, and the total is the length of one comprehension rather
than the sum of all four.
