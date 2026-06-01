from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CoreStock API"
    api_prefix: str = "/api"
    database_url: str

    demo_reset_enabled: bool = False
    demo_reset_token: str | None = None
    demo_reset_cooldown_seconds: int = 300

    cors_allowed_origins: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(env_file=".env")

    @field_validator("cors_allowed_origins")
    @classmethod
    def validate_cors_allowed_origins(cls, origins: list[str]) -> list[str]:
        if not origins:
            raise ValueError("CORS_ALLOWED_ORIGINS must contain at least one origin.")

        if "*" in origins:
            raise ValueError("Wildcard CORS origin '*' is not allowed.")

        return origins

    @model_validator(mode="after")
    def validate_demo_reset_security(self) -> "Settings":
        if self.demo_reset_enabled:
            if not self.demo_reset_token:
                raise ValueError(
                    "DEMO_RESET_TOKEN must be configured when demo reset is enabled."
                )

            if self.demo_reset_token == "change-me":
                raise ValueError(
                    "DEMO_RESET_TOKEN must be changed before enabling demo reset."
                )

            if len(self.demo_reset_token) < 32:
                raise ValueError(
                    "DEMO_RESET_TOKEN must be at least 32 characters long."
                )

        return self


settings = Settings()
