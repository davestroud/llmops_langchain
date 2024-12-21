import functools
import logging
from typing import Callable, Any, Type, Union, Tuple

logger = logging.getLogger(__name__)

class RetryableError(Exception):
    pass

def retry_on_error(
    retries: int = 3,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = RetryableError,
    delay: float = 1.0
):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(retries):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(
                        f"Attempt {attempt + 1}/{retries} failed: {str(e)}"
                    )
                    if attempt < retries - 1:
                        await asyncio.sleep(delay * (attempt + 1))
            
            raise last_exception
        
        return wrapper
    return decorator 