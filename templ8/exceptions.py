from typing import List


class InvalidCommand(Exception):
    def __init__(self, command: List[str], cli: str) -> None:
        super().__init__(f"Invalid command: {command}\n\n{cli}")


class InvalidConfigPath(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Invalid configuration path: {path}")


class InvalidOutputDir(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Invalid output directory: {path}")


class MissingContext(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Missing contextprovided: {name}")


class FailedContextLookup(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Failed to lookup the context value for: {name}")


class MissingSpecDependecy(Exception):
    def __init__(self, name, extends, specs) -> None:
        super().__init__(
            f"Failed to find all spec dependencies:\nSpec: {name}\Extends: {', '.join(extends)} \nSpecs: {specs}"
        )
