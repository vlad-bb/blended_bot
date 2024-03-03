from .connect_db import connect
from .models import Users


async def save_or_update_user_to_db(user_data: dict):
    user = Users.objects(user_id=user_data.get("user_id")).first()
    if user:
        user.first_name = user_data.get("first_name")
        user.last_name = user_data.get("last_name")
        user.username = user_data.get("username")
        user.language_code = user_data.get("language_code")
        user.is_active = True
    else:
        user: Users = Users(user_id=user_data.get("user_id"), first_name=user_data.get("first_name"),
                            last_name=user_data.get("last_name"), username=user_data.get("username"),
                            language_code=user_data.get("language_code"))
    user.save()
