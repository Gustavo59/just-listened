from pydantic import BaseModel


class AuthenticateUserInputDto(BaseModel):
    id_token: str


class AuthenticateUserOutputDto(BaseModel):
    access_token: str
