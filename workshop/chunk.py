from pydantic import BaseModel

class Chunk(BaseModel):
    page_number: int
    content: str
