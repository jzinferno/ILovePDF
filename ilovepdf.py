from httpx import AsyncClient
import aiofiles

class ILovePDF(object):
    def __init__(self, public_key):
        self.public_key = public_key
        self.api_version = 'v1'
        self.api_server = 'api.ilovepdf.com'
        self.url = ''
        self.token = ''
        self.task = ''
        self.tool = ''
        self.headers = None
        self.params = None
        self.input_file = ''
        self.output_file = ''
        self.server_filename = ''
        self.status = ''

    def _set_url(self):
        self.url = 'https://' + self.api_server + '/' + self.api_version + '/'

    async def auth(self):
        self._set_url()
        async with AsyncClient() as client:
            response = await client.post(self.url + 'auth', data={'public_key': self.public_key})
        self.token = response.json()['token']
        self.headers = {'Authorization': 'Bearer ' + self.token}

    async def start(self):
        async with AsyncClient() as client:
            response = await client.get(self.url + 'start/' + self.tool, headers=self.headers)
        self.api_server = response.json()['server']
        self.task = response.json()['task']
        self._set_url()

    async def upload(self):
        async with aiofiles.open(self.input_file, mode='rb') as f:
            async with AsyncClient() as client:
                response = await client.post(self.url + 'upload', data={'task': self.task}, headers=self.headers, files={'file': f.raw})
        self.server_filename =  response.json()['server_filename']

    async def process(self):
        params = {'task': self.task, 'tool': self.tool, 'files[0][server_filename]': self.server_filename, 'files[0][filename]': self.input_file.split('/')[-1]}
        if self.params is not None:
            params.update(self.params)
        async with AsyncClient() as client:
            response = await client.post(self.url + 'process', data=params, headers=self.headers)
        self.status = response.json()['status']

    async def download(self):
        async with AsyncClient() as client:
            response = await client.get(self.url + 'download/' + self.task, headers=self.headers)
        async with aiofiles.open(self.output_file, mode='wb') as f:
            await f.write(response.content)

    async def delete_task(self):
        async with AsyncClient() as client:
            await client.post(self.url + 'task/' + self.task, headers=self.headers)

    async def execute(self):
        await self.auth()
        await self.start()
        await self.upload()
        await self.process()
        await self.download()
        await self.delete_task()
