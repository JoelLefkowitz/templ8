from dataclasses import dataclass


@dataclass
class TemplaterOptions:
    silent: bool
    overwrite: bool
    assume_yes: bool
    skip_callbacks: bool
