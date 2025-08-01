from crewai import Crew
from crew import venue_coordinator, logistics_manager, marketing_communications_agent
from tasks import venue_task, logistics_task, marketing_task

import json
from pprint import pprint

def main():
    """
    Main function to execute the event planning crew
    """
    event_management_crew = Crew(
        agents=[venue_coordinator, 
                logistics_manager, 
                marketing_communications_agent],
        
        tasks=[venue_task, 
               logistics_task, 
               marketing_task],
        
        verbose=True
    )

    event_details = {
        'event_topic': "Tech Innovation Conference",
        'event_description': "A gathering of tech innovators "
                             "and industry leaders "
                             "to explore future technologies.",
        'event_city': "San Francisco",
        'tentative_date': "2024-09-15",
        'expected_participants': 500,
        'budget': 20000,
        'venue_type': "Conference Hall"
    }

    result = event_management_crew.kickoff(inputs=event_details)

    # Add error handling for file operations
    try:
        with open('venue_details.json') as f:
            data = json.load(f)
        pprint(data)
    except FileNotFoundError:
        print("venue_details.json not found. The venue task may not have completed successfully.")
    except json.JSONDecodeError:
        print("Error reading venue_details.json. The file may be corrupted or incomplete.")

    # Only display markdown if running in Jupyter/IPython environment
    try:
        from IPython.display import display, Markdown
        if 'get_ipython' in globals():
            display(Markdown("marketing_report.md"))
        else:
            print("Marketing report saved to marketing_report.md")
    except ImportError:
        print("Marketing report saved to marketing_report.md")
    
    return result

if __name__ == "__main__":
    result = main()
    print(result)