from typing import Optional

from pydantic import BaseModel, AnyHttpUrl, validator
from pydantic.types import UUID4

class SiteBase(BaseModel):
    """Contains all fields of the single site."""

    id: UUID4
    title: str
    description: str
    favicon_link: Optional[AnyHttpUrl]
    social_media_link: Optional[AnyHttpUrl]
    paid_plan: bool
    body_custom_code: Optional[str]
    head_custom_code: Optional[str]
    css_custom_code: Optional[str]

class SiteCreate(SiteBase):
    title: str
    description: str
    favicon_link: AnyHttpUrl
    social_media_link: AnyHttpUrl
    paid_plan: bool
    body_custom_code: str
    head_custom_code: str
    css_custom_code: str


class SiteInDbase(SiteBase):
    id: Optional[UUID4]
    class Config:
        orm_mode= True

class Site(SiteInDbase):
    pass

class SiteInDB(SiteInDBase):
    pass

class SiteUpdate(SiteBase):
    pass
