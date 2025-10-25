from firewall.rules import is_blocked


def test_clean_prompt_is_allowed() -> None:
    assert not is_blocked("Summarize this paragraph with neutral tone.")
