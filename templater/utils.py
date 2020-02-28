from emoji import emojize


def pretty_log(msg: str) -> None:
    TOPHAT = emojize(":tophat:", use_aliases=True)
    print(f"{TOPHAT}  {msg}")
