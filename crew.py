from crewai import Crew,Process
from agents import blog_writer,blog_reserchure
from tools import tool
from task import reasearch_task,write_task

## Following the tech focused crew with come enhanced configuration

crew=Crew(
    agents=[blog_reserchure,blog_writer],
    tasks=[reasearch_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)


## task execution process with enhance feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Science'})
print(result)