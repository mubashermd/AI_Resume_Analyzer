from pydantic import BaseModel, Field

class ResumeSchema(BaseModel):
    name: str | None = Field(default=None, description="Candidate full name")
    email: str | None = Field(default=None, description="Email address")
    phone: str | None = Field(default=None, description="Phone number")
    skills: list[str] | None = Field(default=None, description="List of skills")
    summary: str | None = Field(default=None, description="Experience summary")
    linkedin: str | None = Field(default=None, description="LinkedIn profile link")
    github: str | None = Field(default=None, description="GitHub profile link")
    filename:str | None = Field(default=None, description="Extract File Name")

    # 🔥 Compatibility fix for LangChain
    @classmethod
    def schema(cls):
        return cls.model_json_schema()
