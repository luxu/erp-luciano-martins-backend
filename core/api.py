from http import HTTPStatus

from django.contrib.auth import authenticate

from ninja import Router
from ninja_jwt.tokens import RefreshToken

from core.schemas import TokenPairSchema, ErrorSchema, AuthCredentialsSchema

_LOGIN_BACKEND = "django.contrib.auth.backends.ModelBackend"

router = Router(tags=["auth"])

@router.post("auth/token",
    response={
        HTTPStatus.OK: TokenPairSchema,
        HTTPStatus.UNAUTHORIZED: ErrorSchema,
    },
)
def obtain_token_pair(request, payload: AuthCredentialsSchema):
    user = authenticate(
        request,
        username=payload.username,
        password=payload.password,
        backend=_LOGIN_BACKEND,
    )

    if user is None or not getattr(user, "is_active", False):
        return HTTPStatus.UNAUTHORIZED, ErrorSchema(message="Invalid credentials")

    refresh = RefreshToken.for_user(user)
    return TokenPairSchema(refresh=str(refresh), access=str(refresh.access_token))
