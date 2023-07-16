from ..ilovepdf import ILovePDF

class OfficePDF(ILovePDF):
    def __init__(self, public_key):
        super().__init__(public_key)
    
    async def run(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.tool = 'officepdf'

        await self.execute()
