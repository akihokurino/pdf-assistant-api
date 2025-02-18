import asyncio
from datetime import datetime, timezone, timedelta
from typing import Final

from adapter.adapter import OpenAIAdapter, AssistantRepository, AssistantFSRepository
from di.di import container
from domain.document import Status


async def _main() -> None:
    openai_adapter: OpenAIAdapter = container.openai_adapter()
    assistant_repository: AssistantRepository = container.assistant_repository()
    assistant_fs_repository: AssistantFSRepository = container.assistant_fs_repository()

    now: Final[datetime] = datetime.now(timezone.utc)
    target: Final[datetime] = now - timedelta(hours=3)

    results: Final = await assistant_repository.find_past(target)
    for result in results:
        assistant, document = result

        document.update_status(Status.PREPARE_ASSISTANT, now)
        await openai_adapter.delete_assistant(assistant.id)
        await assistant_repository.delete_with_update_document(document.id, document)
        await assistant_fs_repository.delete(assistant.id)


if __name__ == "__main__":
    asyncio.run(_main())
