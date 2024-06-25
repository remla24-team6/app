import os
import pandas as pd


def add_feedback_and_get_new_accuracy(url, label, feedback):
    
    feedback_file_path = f"{os.getenv('SAVE_TRAINING_DATA_FOLDER')}{os.getenv('SAVE_TRAINING_DATA_FILENAME')}"
    feedback_data = pd.read_csv(feedback_file_path)
    new_row = pd.DataFrame({"url": [url], "label": [label], "feedback": [feedback]})
    updated_data = pd.concat([feedback_data, new_row], ignore_index=True)

    new_accuracy = round(updated_data["feedback"].mean(), 3)

    updated_data.to_csv(feedback_file_path, index=False)

    return new_accuracy
