import re

def ibtcode_detect(text: str) -> str:
    text_lower = text.lower()

    # Default values
    state = "stable"
    emotion = "neutral"
    intensity = 0.5
    intent = "inform"
    truth = "high"
    context = "customer_support"

    # ---- INTENT DETECTION ----
    if "third time" in text_lower or "again" in text_lower:
        intent = "follow_up"
        emotion = "frustration"
        intensity = 0.7
        state = "unstable"

    if "please respond" in text_lower:
        intent = "pressure"
        emotion = "frustration"
        intensity = 0.85
        state = "reactive"

    if "any update" in text_lower:
        intent = "follow_up"
        emotion = "curiosity"
        intensity = 0.6

    if "no worries" in text_lower:
        intent = "accept_delay"
        emotion = "calm"
        intensity = 0.6
        truth = "masked"

    # ---- EMOTION DETECTION ----
    if "disappointed" in text_lower:
        emotion = "disappointment"
        intensity = 0.8
        state = "unstable"
        intent = "complain"

    # ---- BUILD IBT OUTPUT ----
    ibt = f"""IBT{{
  S={state};
  E={emotion}({intensity});
  I={intent};
  T={truth};
  C={context};
}}"""

    return ibt