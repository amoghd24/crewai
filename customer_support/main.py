from crewai import Crew
from IPython.display import Markdown
from crew import support_agent, support_quality_assurance_agent
from tasks import inquiry_resolution, quality_assurance_review

def main():
    """
    Main function to execute the customer support crew
    """
    crew = Crew(
        agents=[support_agent, support_quality_assurance_agent],
        tasks=[inquiry_resolution, quality_assurance_review],
        verbose=2,
        memory=True
    )

    inputs = {
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": "I need help with setting up a Crew "
                   "and kicking it off, specifically "
                   "how can I add memory to my crew? "
                   "Can you provide guidance?"
    }
    
    result = crew.kickoff(inputs=inputs)
    return Markdown(result)

if __name__ == "__main__":
    result = main()
    print(result)