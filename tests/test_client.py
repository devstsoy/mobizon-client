import pytest
import os
from mobizon_client import AsyncMobizonClient
from mobizon_client.objects import Balance, MessageStatus, MessageInfo


@pytest.fixture
def client():
    api_key = os.getenv('API_KEY')
    return AsyncMobizonClient(url='https://api.mobizon.kz', api_key=api_key)


def test_init():
    client = AsyncMobizonClient(url='api.mobizon.kz', api_key='123456')
    assert client._url == 'api.mobizon.kz'
    assert client._api_key == '123456'


@pytest.mark.asyncio
async def test_get_balance(client):
    result = await client.get_balance()
    assert isinstance(result, Balance)
    assert result.currency == 'KZT'


@pytest.mark.asyncio
async def test_send_message(client):
    result = await client.send_message('77074004737', 'Test')
    assert isinstance(result, MessageInfo)
    assert result.status == 2
    assert result.message_id
    assert result.campaign_id


@pytest.mark.asyncio
async def test_get_message_status(client):
    result = await client.get_message_status(['206936345'])
    assert isinstance(result, list)
    assert isinstance(result[0], MessageStatus)
    assert result[0].message_id == '206936345'
    assert result[0].segment_count == '1'
    assert result[0].status == 'DELIVRD'
