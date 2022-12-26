import pytest
from tortoise import Tortoise

from app.config import get_settings
from app.models import Summary, User
from app.security.auth import create_password_hash

settings = get_settings()


@pytest.mark.asyncio
async def test_text_summary_str_method():
    try:
        await Tortoise.init(db_url=settings.DATABASE_TEST_URL, modules={"models": settings.MODELS})
        await Tortoise.generate_schemas()
        payload = {"username": "test", "email": "test@mail.com", "full_name": "Test User", "password": "secret"}
        user = User(
            username=payload["username"],
            email=payload["email"],
            full_name=payload["full_name"],
            hashed_password=create_password_hash(payload["password"]),
        )
        await user.save()
        test_url = "https://lipsum.com/"
        summary = Summary(url=test_url, summary="", user_id=user.id)
        await summary.save()
        url = await Summary.filter(id=summary.id).first()
        assert str(url) == test_url
    finally:
        await Tortoise.close_connections()
