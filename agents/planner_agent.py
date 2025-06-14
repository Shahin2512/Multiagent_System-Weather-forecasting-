def plan_user_goal(user_goal):
    if "spacex" in user_goal.lower():
        return ["Get next SpaceX launch", "Check weather at launch site", "Summarize delay possibility"]
    else:
        return ["Goal not supported yet"]
