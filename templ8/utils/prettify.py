from emoji import emojize


def prettify_log(msg: str) -> str:
    tophat = emojize(":tophat:", use_aliases=True)
    return f"{tophat} {msg} {tophat}"


def prettify_heading(msg: str) -> str:
    heart = emojize(":heart:", use_aliases=True)
    return f"{heart} {msg} {heart}"
