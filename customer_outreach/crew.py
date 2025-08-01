import warnings
warnings.filterwarnings('ignore')

from crewai import Agent

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

outreach_specialist = Agent(
    role="Senior Outreach Specialist",
	goal="Be the most effective and engaging "
        "outreach specialist in your team",
	backstory=(
		"You work at crewAI (https://crewai.com) and "
        " are now working on creating compelling outreach campaigns "
		"for {customer}, a potential important customer "
        " for your company."
		"You need to make sure that you create engaging and personalized outreach!"
		"Make sure to provide compelling messaging that resonates, "
        " and make no assumptions about the customer's needs."
	),
	allow_delegation=False,
	verbose=True
)

outreach_quality_assurance_agent = Agent(
	role="Outreach Quality Assurance Specialist",
	goal="Get recognition for providing the "
    "best outreach quality assurance in your team",
	backstory=(
		"You work at crewAI (https://crewai.com) and "
        "are now working with your team "
		"on outreach campaigns for {customer} ensuring that "
        "the outreach specialist is "
		"creating the most effective outreach possible.\n"
		"You need to make sure that the outreach specialist "
        "is providing compelling, "
		"personalized messaging that drives engagement."
	),
	verbose=True
)