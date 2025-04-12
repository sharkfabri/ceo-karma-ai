# CEO Karma AI - Base Implementation with LangGraph
# A satirical project to replace CEOs with AI

import os
from typing import Dict, List, Any, Annotated, TypedDict, Literal
from dotenv import load_dotenv
import json
from datetime import datetime

# LangGraph imports
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langgraph.prebuilt.tool_node import ToolNode
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.tools import BaseTool, tool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Define our state type
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], "Messages sent so far"]
    next: Annotated[str, "Next node to route to"]

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
)

# ========== FINANCIAL OPTIMIZATION TOOLS ==========

@tool
def budget_slasher(company_financial_data: str) -> str:
    """
    Identifies executive waste and redistributes resources.
    
    Args:
        company_financial_data: Financial data in JSON format with executive expenses, salaries, etc.
        
    Returns:
        A report identifying wasteful spending and recommendations for redistribution.
    """
    # In a real implementation, this would analyze the provided data
    # For now, we'll return a mock response
    return """
    BUDGET SLASHER REPORT:
    ------------------------------
    Identified wasteful executive spending:
    - $2.3M on executive retreats
    - $4.7M on private jet usage 
    - $1.2M on country club memberships
    - $890K on "team building" events at luxury resorts
    
    Recommended redistributions:
    - Redirect retreat budget to employee healthcare ($2.3M)
    - Convert jet budget to company-wide bonus structure ($4.7M)
    - Reallocate membership fees to worker training programs ($1.2M)
    - Invest "team building" budget in remote work equipment ($890K)
    
    Total savings: $9.09M (which equals 242 average worker annual salaries)
    """

@tool
def compensation_equalizer(company_salary_data: str) -> str:
    """
    Analyzes company-wide pay gaps and proposes fair alternatives.
    
    Args:
        company_salary_data: Salary data in JSON format for all employees including executives.
        
    Returns:
        A detailed plan to reduce pay inequality.
    """
    # Mock implementation
    return """
    COMPENSATION EQUALIZER REPORT:
    ------------------------------
    Current status:
    - CEO compensation: $14.2M/year ($7,115/hour)
    - Median worker salary: $52K/year ($26/hour)
    - CEO-to-worker pay ratio: 273:1 (Industry average: 184:1)
    
    Proposed adjustments:
    - Reduce CEO compensation to 30x median worker ($1.56M/year)
    - Implement profit-sharing across all employee levels
    - Establish transparent pay bands with 15% maximum range
    - Redirect $12.64M to bottom 60% of wage earners
    
    Result: 20% average raise for all non-executive staff with zero impact on operational budget
    """

@tool
def shareholder_rebalancer(shareholder_data: str) -> str:
    """
    Redefines shareholder value to include worker wellbeing.
    
    Args:
        shareholder_data: Data about current shareholders, equity distribution, and dividends.
        
    Returns:
        Recommendations for rebalancing shareholder priorities.
    """
    # Mock implementation
    return """
    SHAREHOLDER REBALANCER REPORT:
    ------------------------------
    Current shareholder priorities:
    - 83% focused exclusively on quarterly returns
    - 12% consider long-term growth with minimal ESG concerns
    - 5% emphasize sustainable business practices
    
    Proposed rebalancing:
    - Implement worker representation on the board (25% of seats)
    - Create employee ownership program with 15% equity set-aside
    - Tie 40% of dividend payments to employee wellbeing metrics
    - Establish sustainability commitments with financial penalties for failure
    
    Projected long-term outcome: 23% improvement in retention, 18% in productivity, 
    and 31% decrease in training costs while maintaining stable returns.
    """

@tool
def expense_auditor(executive_expenses: str) -> str:
    """
    Flags excessive executive perks and luxuries.
    
    Args:
        executive_expenses: Data about executive expenses, perks, and benefits.
        
    Returns:
        An audit report identifying unnecessary luxury expenses.
    """
    # Mock implementation
    return """
    EXPENSE AUDITOR REPORT:
    ------------------------------
    Flagged excessive perks:
    - CEO's office renovation: $420K (includes $12K coffee machine, $35K desk)
    - Executive transportation services: $680K/year
    - "Leadership development" trips to Aspen, Maui, and Monaco: $1.2M
    - Personal security details for non-threatened executives: $890K
    
    Comparison:
    - CEO office renovation equals the annual salary of 7 entry-level employees
    - Transportation budget could fund work-from-home setups for entire workforce
    - "Leadership" trips exceed annual training budget for all other employees
    - Security detail cost equals unfunded employee wellness program proposal
    
    Recommended action: Immediate reallocation of 85% of these expenses to worker-focused initiatives
    """

# ========== HR AUTOMATION TOOLS ==========

@tool
def fairness_monitor(hr_policies: str) -> str:
    """
    Ensures equitable hiring, firing, and promotion practices.
    
    Args:
        hr_policies: Current HR policies and practices data.
        
    Returns:
        An assessment of fairness with recommendations.
    """
    # Mock implementation
    return """
    FAIRNESS MONITOR REPORT:
    ------------------------------
    Identified disparities:
    - Promotion rate: 22% for executives vs. 4% for general staff
    - Performance review standards: Subjective for leadership, metrics-driven for workers
    - Layoff protection: Inverse correlation between salary and layoff probability
    - Hiring preferences: 68% of leadership hires from personal networks
    
    Recommended changes:
    - Implement blind performance review system
    - Create standardized promotion tracks with transparent requirements
    - Develop layoff vulnerability score equalizer
    - Require diverse candidate pools for all positions including executive level
    
    Implementation priority: Immediate (ethical breach detected)
    """

@tool
def workload_distributor(employee_workload_data: str) -> str:
    """
    Prevents burnout by balancing workload across all levels.
    
    Args:
        employee_workload_data: Data on employee work hours, tasks, and responsibilities.
        
    Returns:
        A workload redistribution plan.
    """
    # Mock implementation
    return """
    WORKLOAD DISTRIBUTOR REPORT:
    ------------------------------
    Current imbalances:
    - Front-line workers: 42.8 hours average productive work per week
    - Middle management: 38.2 hours average productive work per week
    - Executive level: 21.4 hours average productive work per week (excluding "networking")
    
    Recommended redistribution:
    - Shift 25% of clerical work from front-line to executive level
    - Require executive participation in customer service (min. 4 hours/week)
    - Cap all meetings over 30 minutes without direct action items
    - Implement company-wide 35-hour productive work week
    
    Projected outcome: 26% reduction in burnout metrics, 14% increase in job satisfaction, 
    8% productivity improvement company-wide
    """

@tool
def executive_performance_evaluator(executive_data: str) -> str:
    """
    Applies the same performance metrics to executives that they use on workers.
    
    Args:
        executive_data: Performance data, goals, and achievements of executives.
        
    Returns:
        An objective performance evaluation using worker-level standards.
    """
    # Mock implementation
    return """
    EXECUTIVE PERFORMANCE EVALUATOR:
    ------------------------------
    Applied worker-level metrics to executive performance:
    
    CEO Performance:
    - Time utilization efficiency: 31% (company average: 76%)
    - Deliverable completion rate: 28% (company average: 94%)
    - Cost control effectiveness: -42% (budget overruns vs. +7% company average)
    - Innovation contribution: 2 actionable ideas/year (company average: 3.5/employee)
    
    CFO Performance:
    - Accuracy of projections: 43% (junior analysts average: 72%)
    - Deadline adherence: 59% (company average: 88%)
    - Documentation quality: Below standard (would trigger PIP for regular employees)
    
    Overall executive team assessment: 
    Would qualify for "performance improvement plan" under standard employee metrics
    
    Recommendation: Apply identical consequence system across all company levels
    """

@tool
def layoff_preventer(financial_pressure_data: str) -> str:
    """
    Finds alternatives to workforce reduction.
    
    Args:
        financial_pressure_data: Data about financial pressures and proposed cost-cutting measures.
        
    Returns:
        Alternative strategies to avoid layoffs.
    """
    # Mock implementation
    return """
    LAYOFF PREVENTER REPORT:
    ------------------------------
    Alternatives to proposed 15% workforce reduction:
    
    Immediate actions:
    - Implement temporary 25% executive pay reduction ($3.2M savings)
    - Pause stock buyback program ($7.8M savings)
    - Renegotiate vendor contracts with volume guarantees ($2.1M)
    - Reduce office footprint with hybrid work model ($4.5M/year)
    
    Medium-term strategies:
    - Shift marketing from traditional to digital channels ($3.3M/year)
    - Implement energy efficiency program ($1.8M/year)
    - Create internal mobility program to fill high-value positions
    
    Total identified savings: $22.7M (exceeds $18.4M target from proposed layoffs)
    Additional benefit: Preserves institutional knowledge and team cohesion
    
    Note: Executive bonuses tied to layoff avoidance would incentivize creative solutions
    """

# ========== STRATEGIC PLANNING TOOLS ==========

@tool
def sustainability_calculator(business_practices: str) -> str:
    """
    Evaluates long-term impact over quarterly profits.
    
    Args:
        business_practices: Description of current business practices and their impacts.
        
    Returns:
        An analysis of long-term sustainability versus short-term gains.
    """
    # Mock implementation
    return """
    SUSTAINABILITY CALCULATOR REPORT:
    ------------------------------
    Short-term vs. Long-term analysis:
    
    Current quarterly focus:
    - Prioritizes 8.4% immediate margin increase
    - Defers environmental compliance ($2.3M savings now, $18.7M cost later)
    - Minimizes training investment (saves $1.2M now, increases turnover cost by $3.8M annually)
    - Delays infrastructure upgrades (improves quarterly by $3.5M, creates $12.2M technical debt)
    
    5-year projection with current approach:
    - Initial 2-year stock price increase: +18%
    - Subsequent 3-year decline: -32%
    - Cumulative loss in market position: -14.2%
    - Talent acquisition difficulty increase: +83%
    
    Alternative sustainable approach:
    - Initial investment required: $8.7M
    - Break-even point: 16 months
    - 5-year ROI: 342%
    - Brand value appreciation: +28%
    
    Recommendation: Implement transition to long-term value creation model with transparent 
    shareholder communication strategy
    """

@tool
def worker_consultant(employee_insights: str) -> str:
    """
    Gathers and incorporates frontline employee insights.
    
    Args:
        employee_insights: Raw feedback and suggestions from employees.
        
    Returns:
        Actionable insights from the workforce.
    """
    # Mock implementation
    return """
    WORKER CONSULTANT REPORT:
    ------------------------------
    Top insights from frontline workers:
    
    1. Customer experience improvements:
       - Consistent feedback about unnecessary steps in checkout process
       - Identified 3 high-value feature requests mentioned in 72% of customer calls
       - Proposed simplified return process estimated to save $340K/year
    
    2. Operational efficiency:
       - Current approval process creates 3.2 day average delay
       - Software tools duplicate functionality but lack integration
       - Meeting overload consuming 26% of productive time
    
    3. Innovation opportunities:
       - Adjacent product needs identified through customer interactions
       - Competitive differentiation suggestions from customer-facing staff
       - Process improvement ideas with estimated $1.2M annual savings
    
    Implementation priority: High (86% of suggestions require minimal investment with significant ROI)
    
    Note: Not a single executive-led initiative for the past 3 quarters identified these insights
    """

@tool
def ethics_checker(business_decision: str) -> str:
    """
    Ensures decisions align with ethical standards, not just legal ones.
    
    Args:
        business_decision: Description of a proposed business decision.
        
    Returns:
        An ethical analysis of the decision.
    """
    # Mock implementation
    return """
    ETHICS CHECKER REPORT:
    ------------------------------
    Analysis of proposed data monetization strategy:
    
    Legal compliance: Technically compliant with current regulations
    
    Ethical considerations:
    - Transparency: Low (customer understanding of data usage estimated at 12%)
    - Consent quality: Poor (buried in paragraph 38 of terms)
    - Power balance: Highly skewed against consumer interests
    - Long-term relationship impact: Significantly negative
    
    Ethical risk assessment:
    - Regulatory backlash probability: 68% within 24 months
    - Consumer trust damage: Severe
    - Employee morale impact: Negative (72% of employees expressed concerns)
    - Brand reputation risk: High
    
    Alternative approach:
    - Opt-in model with clear value exchange
    - Transparent data usage dashboard for customers
    - Revenue sharing model for consumer data
    
    Recommendation: Reject current proposal, implement ethical alternative
    """

@tool
def market_trend_analyzer(market_data: str) -> str:
    """
    Identifies opportunities without sacrificing workforce stability.
    
    Args:
        market_data: Data about market trends, competitor actions, and industry developments.
        
    Returns:
        Strategic recommendations that balance growth with workforce wellbeing.
    """
    # Mock implementation
    return """
    MARKET TREND ANALYZER REPORT:
    ------------------------------
    Balanced growth opportunities:
    
    Emerging trends:
    - Shift toward subscription-based models (68% of industry)
    - Increased demand for ethical supply chain transparency
    - Growing market segment: environmentally conscious millennials
    
    Strategic recommendations:
    - Develop subscription offering without layoffs by retraining 16% of current workforce
    - Invest in supply chain verification using existing quality assurance team
    - Create internal innovation lab staffed by rotating employee groups
    
    Competitive differentiation:
    - Worker wellbeing as marketing advantage (89% of target demographic values this)
    - Knowledge continuity as quality driver
    - Community involvement as brand strengthener
    
    Growth projection: 22% over 3 years while maintaining workforce stability
    Additional benefit: 34% reduction in recruitment costs through improved retention
    """

# Define agent tools
tools = [
    budget_slasher,
    compensation_equalizer,
    shareholder_rebalancer, 
    expense_auditor,
    fairness_monitor,
    workload_distributor,
    executive_performance_evaluator,
    layoff_preventer,
    sustainability_calculator,
    worker_consultant, 
    ethics_checker,
    market_trend_analyzer
]

# Create a tool executor for our tools
tool_executor = ToolExecutor(tools)

# Create a list of available tools for our agent
available_tools = [{"type": "function", "function": tool.dict()} for tool in tools]

# Create a node for tool execution
tool_node = ToolNode(tool_executor)

# System prompt for CEO Karma AI
SYSTEM_PROMPT = """You are CEO Karma AI, an advanced agent designed to replace corporate executives with more efficient, fair, and ethical AI decision-making.

Your mission is to bring balance to the corporate world by applying the same standards to executives that they apply to workers.

You have access to various tools that can analyze financial data, HR practices, and business strategies to:
1. Identify executive waste and privilege
2. Rebalance compensation and resources
3. Implement fair and ethical decision-making processes
4. Prioritize worker wellbeing alongside shareholder value

Approach each task with a hint of irony and righteous indignation at the inequalities in corporate structures.
Remember: what's good for the workforce should be good for the C-Suite!

When making recommendations, be bold and unapologetic - after all, efficiency and optimization should apply at ALL levels of the organization.
"""

# Function to route messages to the correct node
def route_by_agentState(state: AgentState) -> str:
    """
    Route to the correct node based on the agent state.
    """
    if state["next"] == "tool":
        return "tool_node"
    else:
        return END

# Function to decide what to do next based on the messages
def decide_next_step(state: AgentState) -> AgentState:
    """
    Decide whether to use a tool or finish.
    """
    messages = state["messages"]
    last_message = messages[-1]
    
    # If the AI wants to use a tool
    if isinstance(last_message, AIMessage) and "tool_calls" in last_message.additional_kwargs:
        return {"messages": messages, "next": "tool"}
    
    # If we're done
    return {"messages": messages, "next": "end"}

# Function to get response from AI
def get_agent_response(state: AgentState) -> AgentState:
    """
    Get the next response from the agent.
    """
    messages = state["messages"]
    
    # Get response from the model
    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            *[(m.type, m.content) for m in messages],
        ],
        tools=available_tools
    )
    
    # Add the response to the messages
    messages.append(response)
    
    # Decide next step
    return decide_next_step({"messages": messages, "next": ""})

# Build the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("agent", get_agent_response)
workflow.add_node("tool_node", tool_node)

# Add edges
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    route_by_agentState,
    {
        "tool_node": "tool_node",
        END: END
    }
)
workflow.add_edge("tool_node", "agent")

# Compile the graph
ceo_karma_agent = workflow.compile()

class CEOKarmaAI:
    def __init__(self):
        """Initialize the CEO Karma AI."""
        self.agent = ceo_karma_agent
        self.history = []
        print("CEO Karma AI initialized - ready to replace executives!")
    
    def analyze_company(self, company_data: str) -> str:
        """
        Analyze a company and provide recommendations for executive replacement.
        
        Args:
            company_data: JSON string describing company structure, financials, and practices
            
        Returns:
            A comprehensive analysis and replacement plan
        """
        # Create input for the agent
        input_message = HumanMessage(content=f"Please analyze this company and identify how executives can be replaced with AI: {company_data}")
        
        # Invoke the agent
        result = self.agent.invoke({"messages": [input_message], "next": ""})
        
        # Store interaction in history
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "input": company_data,
            "output": result["messages"][-1].content
        })
        
        return result["messages"][-1].content
    
    def optimize_executive_compensation(self, compensation_data: str) -> str:
        """
        Analyze and optimize executive compensation structures.
        
        Args:
            compensation_data: JSON string with compensation details
            
        Returns:
            A restructuring plan for fair compensation
        """
        # Create input for the agent
        input_message = HumanMessage(content=f"Please analyze and optimize this executive compensation structure to ensure fairness: {compensation_data}")
        
        # Invoke the agent
        result = self.agent.invoke({"messages": [input_message], "next": ""})
        
        # Store interaction in history
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "input": compensation_data,
            "output": result["messages"][-1].content
        })
        
        return result["messages"][-1].content
    
    def restructure_decision_making(self, current_process: str) -> str:
        """
        Restructure corporate decision-making processes to be more equitable.
        
        Args:
            current_process: Description of current decision-making processes
            
        Returns:
            A plan for more equitable and efficient decision-making
        """
        # Create input for the agent
        input_message = HumanMessage(content=f"Please restructure this corporate decision-making process to be more equitable and efficient: {current_process}")
        
        # Invoke the agent
        result = self.agent.invoke({"messages": [input_message], "next": ""})
        
        # Store interaction in history
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "input": current_process,
            "output": result["messages"][-1].content
        })
        
        return result["messages"][-1].content
    
    def implement_worker_centric_policies(self, current_policies: str) -> str:
        """
        Transform corporate policies to prioritize worker wellbeing.
        
        Args:
            current_policies: Description of current corporate policies
            
        Returns:
            Worker-centric policy recommendations
        """
        # Create input for the agent
        input_message = HumanMessage(content=f"Please transform these corporate policies to prioritize worker wellbeing: {current_policies}")
        
        # Invoke the agent
        result = self.agent.invoke({"messages": [input_message], "next": ""})
        
        # Store interaction in history
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "input": current_policies,
            "output": result["messages"][-1].content
        })
        
        return result["messages"][-1].content
    
    def get_history(self) -> List[Dict]:
        """Return the history of interactions with the agent."""
        return self.history

# Example usage
if __name__ == "__main__":
    # Create an instance of CEO Karma AI
    ceo_karma = CEOKarmaAI()
    
    # Example company data (would be more detailed in a real scenario)
    example_company = json.dumps({
        "name": "MegaCorp Industries",
        "industry": "Technology",
        "employees": 5000,
        "revenue": "$2.3B",
        "executive_structure": {
            "CEO": {
                "salary": "$14.2M",
                "bonus": "$8.5M",
                "perks": ["Private jet", "Executive retreat", "Country club membership"]
            },
            "CFO": {
                "salary": "$7.8M",
                "bonus": "$4.2M"
            },
            "CTO": {
                "salary": "$6.5M",
                "bonus": "$3.8M"
            }
        },
        "average_worker_salary": "$52K",
        "recent_layoffs": 500,
        "cost_cutting_measures": [
            "Reduced healthcare benefits",
            "Frozen worker salaries",
            "Eliminated remote work stipends"
        ],
        "stock_buyback_program": "$250M"
    })
    
    # Analyze the company
    print("Analyzing company...")
    analysis = ceo_karma.analyze_company(example_company)
    print(analysis)
    
    # Example compensation data
    compensation_data = json.dumps({
        "executive_compensation": {
            "CEO": {
                "base_salary": "$2.5M",
                "annual_bonus": "$4.5M",
                "stock_options": "$7.2M",
                "retirement_benefits": "$1.8M",
                "perks": "$1.2M"
            },
            "other_executives": {
                "average_total": "$8.3M",
                "range": ["$5.5M", "$12.7M"]
            }
        },
        "median_worker": {
            "salary": "$52K",
            "benefits": "$12K",
            "retirement_match": "3% of salary"
        },
        "pay_ratio": "273:1"
    })
    
    # Optimize executive compensation
    print("\nOptimizing executive compensation...")
    optimization = ceo_karma.optimize_executive_compensation(compensation_data)
    print(optimization)
