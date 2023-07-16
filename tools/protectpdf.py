from ..ilovepdf import ILovePDF

class ProtectPDF(ILovePDF):
    def __init__(self, public_key):
        super().__init__(public_key)
    
    async def run(self, input_file: str, output_file: str, password: str):
        self.input_file = input_file
        self.output_file = output_file
        self.params = {'password': password}
        self.tool = 'protect'

        await self.execute()
