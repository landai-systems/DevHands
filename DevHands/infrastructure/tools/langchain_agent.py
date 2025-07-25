# devhands/infrastructure/tools/langchain_agent.py

from typing import Optional
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI


class LangchainAgent:
    """
    Encapsulates the LangChain interaction for executing DevHands tasks.
    """

    def __init__(
        self,
        model_name: str = "gpt-4o",
        temperature: float = 0.3
    ) -> None:
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)

    def run_prompt(self, prompt_template: str, input_vars: dict) -> str:
        """
        Executes a prompt template with placeholders.
        Returns: LLM response as string.
        """
        prompt: Runnable = ChatPromptTemplate.from_template(prompt_template)
        chain = prompt | self.llm
        result = chain.invoke(input_vars)
        return result.content.strip() if hasattr(result, "content") else str(result)

    def explain_code(self, code: str, goal: str) -> str:
        """
        Example method for refactoring analysis.
        """
        prompt = """You are an experienced software architect.
        Analyze the following code with respect to the goal: {goal}

        CODE:
        ```python
        {code}
        Return improvement suggestions in diff format. Only include relevant changes and clear recommendations."""
        return self.run_prompt(prompt, {"code": code, "goal": goal})
