from ninja import Schema


class TokenPairSchema(Schema):
    access: str
    refresh: str


class ErrorSchema(Schema):
    message: str


class AuthCredentialsSchema(Schema):
    username: str
    password: str