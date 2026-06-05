import json

FEEDBACK_FILE = "data/feedback.json"


def save_feedback(generated_text, edited_text):

    try:
        with open(FEEDBACK_FILE, "r") as f:
            feedback_data = json.load(f)

    except:
        feedback_data = []

    feedback_data.append(
        {
            "generated": generated_text,
            "edited": edited_text
        }
    )

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(
            feedback_data,
            f,
            indent=4
        )