import logging

from src.dify.base import BaseClient

logger = logging.getLogger(__name__)


class Dify(BaseClient):
    def __init__(self, api_key: str, **kwargs):
        self.api_key = api_key
        self.base_url = "https://api.dify.ai"
        super().__init__(base_url=self.base_url)

    async def send_chat_message(
            self,
            message: str,
            user_id: int,
            conversation_id: str = None
    ) -> tuple[int, dict[str, str]]:
        response = await self._make_request(
            'post',
            '/v1/chat-messages',
            json={
                "query": message,
                "response_mode": 'blocking',
                "conversation_id": conversation_id if conversation_id else '',
                "user": user_id,
                "inputs": {}
            },
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        session = await self._get_session()
        await session.close()
        return response

