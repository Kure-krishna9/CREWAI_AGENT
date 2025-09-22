from crewai import Task
from tools import tool
from agents import blog_reserchure,blog_writer

## resurcher task

reasearch_task=Task(
    description=("Identify the video {topic}."
    "Get deatailed information about the video from the channel"
),
expected_output="A comprensive 3 paregraphs long report based on the {topic} of video.",
tools=[tool],
agent=blog_reserchure,
)


# writing task  with language model configuration
write_task=Task(
    description=(
        "get the information the youtube channel on the topic{topic}."
    ),
    expected_output='summarize the info from the youtube channel video on the topic{topic}',
    tools=[tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post,md'

)
