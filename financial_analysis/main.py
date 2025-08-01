from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from IPython.display import Markdown

from crew import data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent
from tasks import data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task

def main():
    """
    Main function to execute the financial analysis crew
    """
    # Define the crew with agents and tasks
    financial_trading_crew = Crew(
        agents=[data_analyst_agent, 
                trading_strategy_agent, 
                execution_agent, 
                risk_management_agent],
        
        tasks=[data_analysis_task, 
               strategy_development_task, 
               execution_planning_task, 
               risk_assessment_task],
        
        manager_llm=ChatOpenAI(model="gpt-3.5-turbo", 
                               temperature=0.7),
        process=Process.hierarchical,
        verbose=True
    )

    # Example data for kicking off the process
    financial_trading_inputs = {
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
        'news_impact_consideration': True
    }

    ### This execution will take some time to run
    result = financial_trading_crew.kickoff(inputs=financial_trading_inputs)
    
    return Markdown(result)

if __name__ == "__main__":
    result = main()
    print(result)