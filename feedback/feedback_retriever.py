import json

FEEDBACK_FILE = "data/feedback.json"


def load_feedback():

    try:

        with open(FEEDBACK_FILE, "r") as f:

            return json.load(f)

    except:

        return []