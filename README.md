# Mobizon Client

#### [Ссылка на официальную документацию](https://mobizon.kz/help/api-docs/sms-api)

## Примеры:

### Асинхронный клиент

```python
import asyncio
from mobizon_client import AsyncMobizonClient


async def main():
    url = 'https://api.mobizon.kz'
    api_key = 'xisNSPPFj05WTVyH5oALU86VVuH7SocEUiitN0Og'
    client = AsyncMobizonClient(url=url, api_key=api_key)
    result = await client.send_message(recipient='77071234567', text='Test message', sender_signature=None)
    await asyncio.sleep(3)
    result = await client.get_message_status([result.message_id])
    assert result[0].status == 'DELIVRD'
    await client.close()


if __name__ == '__main__':
    asyncio.run(main())
```

### Синхронный клиент

```python
from time import sleep
from mobizon_client import MobizonClient


def main():
    url = 'https://api.mobizon.kz'
    api_key = 'xisNSPPFj05WTVyH5oALU86VVuH7SocEUiitN0Og'
    client = MobizonClient(url=url, api_key=api_key)
    result = client.send_message(recipient='77071234567', text='Test message', sender_signature=None)
    sleep(3)
    result = client.get_message_status([result.message_id])
    assert result[0].status == 'DELIVRD'
    client.close()


if __name__ == '__main__':
    main()
```