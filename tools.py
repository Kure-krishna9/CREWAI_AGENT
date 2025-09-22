# from crewai_tools import YoutubeVideoSearchTool

# # General video search
# tool = YoutubeVideoSearchTool()

# # Or target specific video
# tool = YoutubeVideoSearchTool(youtube_video_url='https://youtube.com/watch?v=example')


from crewai_tools import YoutubeChannelSearchTool
from langchain_groq import ChatGroq
import os

llm = ChatGroq(model="mixtral-8x7b-32768", groq_api_key=os.getenv("Groq_key"))

# General channel search
tool = YoutubeChannelSearchTool()

# Or target specific channel
tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
tool.llm = llm 