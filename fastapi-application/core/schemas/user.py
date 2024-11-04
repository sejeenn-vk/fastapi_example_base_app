from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    foo: int
    bar: int


class UserCreate(UserBase):
    ...


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
    