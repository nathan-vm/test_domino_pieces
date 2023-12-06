from pydantic import BaseModel, Field
class InputModel(BaseModel):
    html_title: str = Field(
        description="title for html"
    )

class OutputModel(BaseModel):
    html: str = Field(
        description="HTML result"
    )
