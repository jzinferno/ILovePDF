### ILovePDF python/httpx

https://developer.ilovepdf.com/docs/api-reference

### Installation

```bash
git clone --depth=1 https://github.com/jzinferno/ILovePDF.git
pip install --upgrade httpx
```

### Usage

```python
from ILovePDF import CompressPDF
import asyncio

project_public = 'project_public_...'

async def main():
    await CompressPDF(project_public).run('input.pdf', 'output.pdf')

asyncio.run(main())
```