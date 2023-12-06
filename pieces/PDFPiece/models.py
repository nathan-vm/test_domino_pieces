from pydantic import BaseModel, Field

class InputModel(BaseModel):
    pdf_title: str = Field(
        description="description"
    )


class OutputModel(BaseModel):
    pdf: str = Field(
        description="PDF result"
    )
