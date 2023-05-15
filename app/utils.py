def get_current_user():
    """Get the current user from the session."""
    user_id = session.get("user_id")
    if user_id is None:
        return None

    user = User.query.get(user_id)
    return user
