from crewai import Crew
from IPython.display import Markdown
from crew import outreach_specialist, outreach_quality_assurance_agent
from tasks import outreach_campaign_creation, campaign_quality_assurance_review

def main():
    """
    Main function to execute the customer outreach crew
    """
    crew = Crew(
        agents=[outreach_specialist, outreach_quality_assurance_agent],
        tasks=[outreach_campaign_creation, campaign_quality_assurance_review],
        verbose=2,
        memory=True
    )

    inputs = {
        "customer": "TechStartup Inc",
        "contact_person": "Sarah Johnson",
        "campaign_objective": "I need help creating an outreach campaign "
                             "to introduce our AI automation services "
                             "to potential enterprise clients. "
                             "Focus on productivity and cost savings benefits."
    }
    
    result = crew.kickoff(inputs=inputs)
    return Markdown(result)

if __name__ == "__main__":
    result = main()
    print(result)