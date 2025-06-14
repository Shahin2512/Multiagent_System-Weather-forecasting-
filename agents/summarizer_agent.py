def summarize_launch_status(launch_info, weather_info):
    delay = False
    reasons = []

    if weather_info["wind_speed"] > 10:
        delay = True
        reasons.append("High wind speed")

    if weather_info["weather"].lower() not in ["clear", "clouds"]:
        delay = True
        reasons.append(f"Weather is {weather_info['weather']}")

    if delay:
        return f"The launch '{launch_info['name']}' scheduled at {launch_info['date']} from {launch_info['location']} may be delayed due to: {', '.join(reasons)}"
    else:
        return f"The launch '{launch_info['name']}' is likely to proceed as scheduled with clear weather conditions."
