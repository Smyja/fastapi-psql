mport uuid
from typing import Union, Final, List

from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy import (
    Column,
    String,
    BigInteger,
    DateTime,
    func,
    Boolean,
    Text,
    ForeignKey,
    Index,
    update,
    text,
    SmallInteger,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import declared_attr

from .db import Base


class Site(Base):
    """Model describes user's site.

    title should have up to 100 alphanumeric chars with(out) hyphens.
    title shouldn't start or end with hyphens.

    website link should be unique because of the limitations of the internet.

    vercel_project_name is the project name for Vercel. It should be unique
    vercel_project_name uses uuid_generate_v4 postgre function which requires
    pgcrypto extension.
    """

    __tablename__ = "sites"

    id = Column(BigInteger, primary_key=True)
    title = Column(String(200), nullable=False, default="Title")
    description = Column(Text, nullable=False, default="Site description")
    notion_link = Column(String(200), nullable=False)
    website_link = Column(String(200), default=lambda: uuid.uuid4().hex)
    favicon_link = Column(String(200))
    social_media_link = Column(String(200))
    pages = Column(JSONB, default="{}")
    vercel_project_name = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    paid_plan = Column(Boolean, default=False)
    body_custom_code = Column(Text)
    head_custom_code = Column(Text)
    css_custom_code = Column(Text)

  