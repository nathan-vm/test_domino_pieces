from pydantic import BaseModel, Field

class InputModel(BaseModel):
    pdf_title: str = Field(
        description="description"
    )


class OutputModel(BaseModel):
    base64_content: str = Field(
        description="PDF result"
    )
    file_type: str = Field(
        description="PDF result"
    )
