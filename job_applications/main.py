from crewai import Crew
from IPython.display import Markdown, display
from crew import researcher, profiler, resume_strategist, interview_preparer
from tasks import research_task, profile_task, resume_strategy_task, interview_preparation_task

def main():
    """
    Main function to execute the job applications crew
    """
    job_application_crew = Crew(
        agents=[researcher,
                profiler,
                resume_strategist,
                interview_preparer],

        tasks=[research_task,
               profile_task,
               resume_strategy_task,
               interview_preparation_task],

        verbose=True
    )

    job_application_inputs = {
        'job_posting_url': 'https://jobs.crewai.com/jobs/1504369508-ai-engineer-netapp-inc',
        'github_url': 'https://github.com/amoghd24',
        'personal_writeup': """Amogh is a MBA Grad with over a year experience in AI Agent development.
        His strangeths are building agenting workflows and productiom grade RAG systems.
        He is a quick learner and has a some exposure in fine-tuning and observability
        """
    }

    result = job_application_crew.kickoff(inputs=job_application_inputs)

    display(Markdown("./tailored_resume.md"))
    display(Markdown("./interview_materials.md"))
    
    return result

if __name__ == "__main__":
    result = main()
    print(result)