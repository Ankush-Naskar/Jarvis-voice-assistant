import os
import json
import shutil


class DataHandling:
    def __init__(self, bookmark_path="data/bookmarks.json", settings_path="data/settings.json"):
        self.bookmark_path = bookmark_path
        self.settings_path = settings_path
        self.settings_template = "templates/settings_template.json"
        self.bookmark_template = "templates/bookmarks_template.json"

        # Create settings.json if it does not exist

        if not os.path.exists("data/"):
            os.makedirs("data/")
        if not os.path.exists(self.settings_path):
            shutil.copy(self.settings_template, self.settings_path)
        if not os.path.exists(self.bookmark_path):
            shutil.copy(self.bookmark_template, self.bookmark_path)

        self.bookmarks_data = self.read_json(self.bookmark_path)
        self.settings_data = self.read_json(self.settings_path)
    
    # Read json
    def read_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        return json_data
    
    
class DataCollecting(DataHandling):
    
    # Bookmark data
    def get_bookmarks(self, parent_key, child_key):
        links = self.bookmarks_data.get(parent_key, {}).get(child_key)
        return links
    
    # Settings 
    def get_settings(self, parent_key, child_key):
        settings = self.settings_data.get(parent_key, {}).get(child_key)
        return settings
    
class DataEditing(DataHandling):
        
        def settings_update(self, parent_key, child_key, new_value):
            data = self.read_json(self.settings_path)
            data[parent_key][child_key] = new_value
            
            with open(self.settings_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

    
