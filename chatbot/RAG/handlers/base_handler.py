# ./chatbot/rag/base_handler.py

from abc import ABC, abstractmethod

class BaseQAHandler(ABC):
    """
    Abstract base class for QA Handlers. All subclasses should implement the abstract methods.
    """

    @abstractmethod
    def load_prompt_template(self):
        """
        Abstract method to load the prompt template for generating queries.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def get_answer(self, query: str):
        """
        Abstract method to generate an answer for a given query.
        Must be implemented by subclasses.

        Args:
            query (str): The user's query or question.

        Returns:
            str: The response generated by the QA handler.
        """
        pass