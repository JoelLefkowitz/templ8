from typing import Dict, List


class InvalidCommand(Exception):
    def __init__(self, command: List[str], cli: str) -> None:
        super().__init__(f"\n\nInvalid command: {command}\n\n{cli}")


class InvalidConfigPath(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\n\nInvalid configuration path: {path}")


class InvalidOutputDir(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"\n\nInvalid output directory: {path}")


class MissingContext(Exception):
    def __init__(self, context: str, config: Dict) -> None:
        super().__init__(
            f"\n\nMissing context: {context}\nNot found in config: {config}"
        )
        

class RuntimeContextError(Exception):
    def __init__(self, failed_evaluation: str, config: Dict) -> None:
        super().__init__(
            f"\n\nFailed to evaluate context: {failed_evaluation}\nConfig: {config}"
        )
