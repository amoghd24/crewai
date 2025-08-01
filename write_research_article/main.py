from crewai import Crew
from IPython.display import Markdown
from .crew import planner, writer, editor
from .tasks import plan, write, edit

def main():
    """
    Main function to execute the research and writing crew
    """
    crew = Crew(
        agents=[planner, writer, editor],
        tasks=[plan, write, edit],
        verbose=2
    )
    
    result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})
    return Markdown(result)

if __name__ == "__main__":
    result = main()
    print(result)