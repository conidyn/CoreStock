import time

from fastapi import APIRouter, Header, HTTPException, status

from app.core.config import settings
from app.seed.reset_dev_data import reset_dev_data
from app.seed.run_seed import run as run_seed

router = APIRouter(
    prefix="/demo",
    tags=["Demo"],
)

last_reset_at: float | None = None


@router.post("/reset")
def reset_demo_environment(
    x_demo_token: str | None = Header(default=None),
):
    global last_reset_at

    if not settings.demo_reset_enabled:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Demo data reset is currently unavailable.",
        )

    if not settings.demo_reset_token or x_demo_token != settings.demo_reset_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to perform this action.",
        )

    now = time.time()

    if last_reset_at is not None:
        seconds_since_last_reset = now - last_reset_at

        if seconds_since_last_reset < settings.demo_reset_cooldown_seconds:
            remaining_seconds = int(
                settings.demo_reset_cooldown_seconds - seconds_since_last_reset
            )

            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=(
                    "The demo environment was recently restored. "
                    f"Please wait {remaining_seconds} seconds before resetting it again."
                ),
            )

    reset_dev_data()
    run_seed()

    last_reset_at = now

    return {
        "message": "The demo environment has been restored to its initial state.",
    }
