from abc import ABC


class Injector:
    """
    Simple dependency injection container using a dictionary.
    """
    def __init__(self):
        self.services = {}

    def register(self, abstract_class: type(ABC), implementation):
        """
        Registers a service with the container.

        Args:
          abstract_class: The abstract class.
          implementation: The implementation instance to register.
        """
        self.services[abstract_class] = implementation

    def get(self, abstract_class: type(ABC)):
        """
        Retrieves a registered service from the container.

        Args:
          abstract_class: The abstract class of the implementation to retrieve.

        Returns:
          The registered implementation instance.

        Raises:
          KeyError: If the service is not registered.
        """
        return self.services[abstract_class]
