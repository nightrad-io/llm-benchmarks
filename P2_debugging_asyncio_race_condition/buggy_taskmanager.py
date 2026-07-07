"""
P2 fixture: TaskManager with a genuine dict-mutation-during-iteration race
condition. cancel_all() iterates self._tasks directly while worker()'s
finally block deletes from that same dict on completion -- under the right
timing this raises:
    RuntimeError: dictionary changed size during iteration
"""
import asyncio
import random

random.seed(7)


class TaskManager:
    def __init__(self):
        self._tasks: dict[str, asyncio.Task] = {}

    def spawn(self, task_id: str, coro):
        task = asyncio.ensure_future(coro)
        self._tasks[task_id] = task
        return task

    async def cancel_all(self):
        """BUGGY: iterates the live dict while worker()'s finally block
        may concurrently delete entries from it."""
        for task_id, task in self._tasks.items():   # <-- mutated during iteration
            if not task.done():
                task.cancel()
            await asyncio.sleep(0)  # yield control, allowing other tasks'
                                     # finally blocks to run mid-iteration


async def worker(task_id: str, manager: "TaskManager", delay: float):
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError:
        pass
    finally:
        # Cleans up after itself -- but if this runs WHILE cancel_all() is
        # mid-iteration over manager._tasks, boom.
        manager._tasks.pop(task_id, None)


async def reproduce():
    manager = TaskManager()
    for i in range(40):
        delay = random.uniform(0, 0.01)
        manager.spawn(f"task_{i}", worker(f"task_{i}", manager, delay))
    await asyncio.sleep(0.002)  # let some tasks start finishing
    await manager.cancel_all()
    await asyncio.sleep(0.02)
    print("Run completed without crashing this time (race is intermittent).")


if __name__ == "__main__":
    # Run several times -- the RuntimeError is intermittent/timing-dependent,
    # consistent with the original benchmark's description of the bug.
    for attempt in range(20):
        try:
            asyncio.run(reproduce())
        except RuntimeError as e:
            print(f"Attempt {attempt}: REPRODUCED -> {e}")
            break
    else:
        print("Bug did not reproduce in 20 attempts on this run -- "
              "increase task count or sleep variance if needed.")
