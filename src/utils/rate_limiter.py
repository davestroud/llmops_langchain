import time
from functools import wraps
import asyncio

class RateLimiter:
    def __init__(self, calls_per_minute):
        self.calls_per_minute = calls_per_minute
        self.interval = 60.0 / calls_per_minute
        self.last_call = 0
    
    async def wait(self):
        elapsed = time.time() - self.last_call
        if elapsed < self.interval:
            await asyncio.sleep(self.interval - elapsed)
        self.last_call = time.time()
    
    def limit(self):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                await self.wait()
                return await func(*args, **kwargs)
            return wrapper
        return decorator 