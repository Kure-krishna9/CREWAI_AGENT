from crewai import Agent
from tools import tool

### Create senior blog content resercher
blog_reserchure=Agent(
    role="Blog resurcher for youtube video",
    goal="get the relevent video content for the topic{topic} from yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding video in AI Data science, Machine earning And Gen Ai"
    ),
    tools=[],
    allow_delegation=True
)

## Creating a senior blog writing Agent  withn yt Tool

blog_writer=Agent(
    role='Writer',
    goag='Narrate compiling tech stories about the video {topic}',
    verbose=True,
    memory=True,
    backstory=(
        " With a flair for simplifying complex topics you craft"
        "engaging narrative that capivate  adn educate,bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools=[tool],
    allow_delegation=False




)