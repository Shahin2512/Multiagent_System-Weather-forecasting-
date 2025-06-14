import os
from agents.planner_agent import plan_user_goal
from agents.spacex_agent import get_next_launch
from agents.weather_agent import get_weather
from agents.summarizer_agent import summarize_launch_status
from dotenv import load_dotenv
load_dotenv()


def main():
    user_goal = "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed"
    
    plan = plan_user_goal(user_goal)
    print("Planner Output:", plan)

    launch_info = get_next_launch()
    print("Launch Info:", launch_info)

    weather_info = get_weather(launch_info["latitude"], launch_info["longitude"])
    print("Weather Info:", weather_info)

    summary = summarize_launch_status(launch_info, weather_info)
    print("\nFinal Summary:\n", summary)

if __name__ == "__main__":
    main()
