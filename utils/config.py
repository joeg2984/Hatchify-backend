
from pydantic_settings import BaseSettings 
from pydantic import Field
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    google_maps_api_key: str = Field(..., env='GOOGLE_MAPS_API_KEY')
    google_cloud_secret: str = Field(..., env='GOOGLE_CLOUD_SECRET')
    openai_api_key: str = Field(..., env='OPENAI_API_KEY')
    database_url: str = Field(..., env='DATABASE_URL')
    api_ninjas_key: str = Field(..., env='API_NINJAS_KEY')
    exploding_topics_api_key: str = Field(..., env='EXPLODING_TOPICS_API_KEY')
    vite_openai_api_key: str = Field(..., env='VITE_OPENAI_API_KEY')

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = 'forbid'  
        


try:
    settings = Settings()
    logger.info("Configuration settings loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load settings: {e}")
    raise
