from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./le_libros_caribe.db"
    SECRET_KEY: str = "cambia-esta-clave-en-produccion"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    STRIPE_SECRET_KEY: str = ""
    STRIPE_PRICE_ID_PREMIUM: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    S3_BUCKET_NAME: str = "le-libros-caribe"
    REDIS_URL: str = "redis://localhost:6379"
    AMAZON_AFFILIATE_TAG: str = "lecaribe-20"

    class Config:
        env_file = ".env"

settings = Settings()
