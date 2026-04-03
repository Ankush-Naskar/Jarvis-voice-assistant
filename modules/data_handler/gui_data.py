from modules.data_handler.data_handling import DataEditing
edit = DataEditing()



def data_editing(lst):
    parent_key = ["basic"]*6 + ["artificial_intelligence"]*4 + ["commands"]*5
    child_keys = ["user_name", "assistant_name", "location", "timeout_seconds", "voice_model", "language", "open_ai_api_key", "open_ai_model", "max_token", "prompt", "stop", "google_search", "play_media", "open_website", "weather"]

    for parent, child, new_value in zip(parent_key, child_keys, lst):
        if not new_value == '':
            edit.settings_update(parent, child, new_value=new_value)

        else:
            continue

def data_collecting():
    pass