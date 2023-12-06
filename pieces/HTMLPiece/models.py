from pydantic import BaseModel, Field
class InputModel(BaseModel):
    html_title: str = Field(
        description="title for html"
    )

class OutputModel(BaseModel):
    base64_content: str = Field(
        description="HTML result"
    )
    file_type: str = Field(
        description="HTML result"
    )
