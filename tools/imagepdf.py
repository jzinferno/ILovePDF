from ..ilovepdf import ILovePDF

class ImagePDF(ILovePDF):
    def __init__(self, public_key):
        super().__init__(public_key)
    
    async def run(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.params = {'orientation': 'portrait', 'pagesize': 'fit',  'margin': 0}
        self.tool = 'imagepdf'

        await self.execute()
