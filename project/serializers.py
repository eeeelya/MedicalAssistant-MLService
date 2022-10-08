from pydantic import BaseModel


class RequestSerializer(BaseModel):
    option: str
    model: str
    image_name: str
