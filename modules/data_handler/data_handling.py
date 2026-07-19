import json
import os
import shutil


class DataHandling():
    def __init__(self, bookmark_path="data/bookmarks.json", settings_path="data/settings.json"):
        self.bookmark_path = bookmark_path
        self.settings_path = settings_path

        self.settings_template = "templates/settings_template.json"
        self.bookmark_template = "templates/bookmarks_template.json"

        if not os.path.exists("data/"):
            os.makedirs("data/")
        if not os.path.exists(self.settings_path):
            shutil.copy(self.settings_template, self.settings_path)
        if not os.path.exists(self.bookmark_path):
            shutil.copy(self.bookmark_template, self.bookmark_path)

        # json data sored in list 
        self.parent_key_list = []
        self.child_key_list = []
        self.label_list = []
        self.type_list = []
        self.default_list = []

        # loading json data 
        self.bookmarks_data = self.load_json_data(self.bookmark_path)
        self.settings_data = self.load_json_data(self.settings_path)

        # run load_entry_labels function
        self.load_entry_labels() 
    
    # Function for reading json
    def load_json_data(self, path):
        with open(path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        return json_data
    
    # Function for creae seperate list from json data 
    def load_entry_labels(self):
        for key in self.settings_data.keys():
            category_key = list(self.settings_data.get(key).keys())
            # self.child_key_list.append(category_key) #Create list of child_keys
            for key1 in category_key:
                self.parent_key_list.append(key) # Create list of Parent keys
                self.child_key_list.append(key1) #Create list of child_keys

                lable = self.settings_data.get(key).get(key1).get("label")
                self.label_list.append(lable) #creat list of lables

                type = self.settings_data.get(key).get(key1).get("type")
                self.type_list.append(type) # Create list of types 

                default = self.settings_data.get(key).get(key1).get("default")
                self.default_list.append(default) #Creat list of default values

    #Funcion for editing old values on the baasis of new values.
    def collecting_entry_values(self, new_val):
        for parent, child, new in zip(self.parent_key_list, self.child_key_list, new_val):
            if new != "":
                self.settings_data[parent][child]["default"] = new

        with open(self.settings_path, "w", encoding="utf-8") as f:
            json.dump(self.settings_data, f, indent=4) # Editing values with input values

    def adding_new_values(self):
        pass

    def get_settings(self, child_key):
        if child_key in self.child_key_list:
            position = self.child_key_list.index(child_key)
            default = self.default_list[position]
            return default
    
    # Settings 
    def get_bookmarks(self, parent_key, child_key):
        links = self.bookmarks_data.get(parent_key, {}).get(child_key)
        return links

if __name__ == "__main__":
    app = DataHandling()
    app.get_settings()
