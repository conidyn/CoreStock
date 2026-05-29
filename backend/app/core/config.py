from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CoreStock API"
    api_prefix: str = "/api"
    database_url: str

    demo_reset_enabled: bool = False
    demo_reset_token: str | None = None
    demo_reset_cooldown_seconds: int = 300

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
