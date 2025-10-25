from .rules import is_blocked


def evaluate_prompt(text: str) -> dict[str, str]:
    if is_blocked(text):
        return {"decision": "blocked", "reason": "policy_match"}
    return {"decision": "allow", "reason": "clean"}
