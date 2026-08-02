# Python - Async Function

Asynchronous programming with `async`/`await`, coroutines and `asyncio.Task`.

| File | Task |
| --- | --- |
| `0-basic_async_syntax.py` | `wait_random(max_delay: int = 10) -> float` |
| `1-concurrent_coroutines.py` | `wait_n(n, max_delay) -> List[float]`, ascending without `sort()` |
| `2-measure_runtime.py` | `measure_time(n, max_delay) -> float` |
| `3-tasks.py` | `task_wait_random(max_delay) -> asyncio.Task` |
| `4-tasks.py` | `task_wait_n(n, max_delay) -> List[float]` |

The ascending order in `wait_n` and `task_wait_n` comes from
`asyncio.as_completed`, which yields each awaitable as it finishes — the
shortest delay completes first, so appending in completion order is already
sorted.
