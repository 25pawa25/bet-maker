from abc import ABC, abstractmethod


class AbstractEventRepository(ABC):
    @abstractmethod
    async def get_available_events(self):
        pass

    @abstractmethod
    async def check_if_event_exists(self, event_id: str) -> bool:
        pass
