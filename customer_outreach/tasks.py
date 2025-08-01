from crewai import Task
from crew import outreach_specialist, outreach_quality_assurance_agent
from tool import research_tool

outreach_campaign_creation = Task(
    description=(
        "Create a compelling outreach campaign for {customer}:\n"
	    "{campaign_objective}\n\n"
        "{contact_person} from {customer} is the target contact. "
		"Make sure to use everything you know "
        "to create the most effective outreach possible."
		"You must strive to provide a personalized "
        "and engaging campaign that drives results."
    ),
    expected_output=(
	    "A detailed, personalized outreach campaign for "
        "the target customer that addresses "
        "their specific needs and pain points.\n"
        "The campaign should include subject lines, "
        "email templates, and follow-up sequences. "
        "Include references to research used, "
        "including external data or insights. "
        "Ensure the campaign is compelling, "
		"leaving no aspect unaddressed, and maintain an engaging and professional "
		"tone throughout."
    ),
	tools=[research_tool],
    agent=outreach_specialist,
)

campaign_quality_assurance_review = Task(
    description=(
        "Review the outreach campaign created by the Senior Outreach Specialist for {customer}. "
        "Ensure that the campaign is compelling, personalized, and adheres to the "
		"high-quality standards expected for customer outreach.\n"
        "Verify that all aspects of the campaign objective "
        "have been addressed "
		"thoroughly, with an engaging and professional tone.\n"
        "Check for personalization elements and research used to "
        " create the campaign, "
		"ensuring the outreach is well-targeted and "
        "maximizes engagement potential."
    ),
    expected_output=(
        "A final, detailed, and compelling outreach campaign "
        "ready to be executed for the customer.\n"
        "This campaign should fully address the "
        "campaign objectives, incorporating all "
		"relevant feedback and improvements.\n"
		"Maintain a professional yet engaging tone that "
	    "reflects the company's personality while driving results."
    ),
    agent=outreach_quality_assurance_agent,
)