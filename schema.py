from pydantic import BaseModel, Field

class MoodResponse(BaseModel):
    mood_summary: str = Field(..., description="Reflection on how user feels")
    suggestion: str = Field(..., description="Coping tip based on user's mood")
    log_status: str = Field(..., description="Confirmation of log entry")
