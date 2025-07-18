import pandas as pd
import re
import uuid


class HideoutParser:
    VERSION_REGEX = r'"version"\s*:\s*(\d+)'
    LANGUAGE_REGEX = r'"language"\s*:\s*"([\w\s]+)"'
    HIDEOUT_NAME_REGEX = r'"hideout_name"\s*:\s*"([\w\s]+)"'
    HIDEOUT_HASH_REGEX = r'"hideout_hash"\s*:\s*(\d+)'
    DECORATIONS_REGEX = r'"([\w\s]+)"\s*:\s*{\s*"hash"\s*:\s*(\d+),\s*"x"\s*:\s*(\d+),\s*"y"\s*:\s*(\d+),\s*"r"\s*:\s*(\d+),\s*"fv"\s*:\s*(\d+)\s*}'


    def __init__(self, file_path : str):
        self.get_hideout_information(file_path)

    def get_hideout_information(self, file_path : str):
        with open(file_path, "r") as file:
            hideout_data = file.read()
            
            self.version = re.search(self.VERSION_REGEX, hideout_data).group(1)
            self.language = re.search(self.LANGUAGE_REGEX, hideout_data).group(1)
            self.hideout_name = re.search(self.HIDEOUT_NAME_REGEX, hideout_data).group(1)
            self.hideout_hash = re.search(self.HIDEOUT_HASH_REGEX, hideout_data).group(1)
            
            decorations_raw_data = re.findall(self.DECORATIONS_REGEX, hideout_data)
            self.decorations_data = pd.DataFrame(decorations_raw_data, columns=["name", "hash", "x", "y", "r", "fv"])
            self.decorations_data.insert(0, "uuid", None)

            self.decorations_data = self.decorations_data.astype({"uuid" : str, "name" : str, "hash" : int,
                                                                  "x" : int, "y" : int, "r" : int, "fv" : int})

            self.decorations_data["uuid"] = self.decorations_data["uuid"].apply(lambda id: uuid.uuid4())

    def set_decoration_location(self, uuid : int, target_x : int, target_y : int):
        self.set_decoration_x(uuid, target_x)
        self.set_decoration_y(uuid, target_y)

    def set_decoration_x(self, uuid : int, target_x : int):
        self.decorations_data.loc[self.decorations_data["uuid"] == uuid, ["x",]] = target_x
    
    def set_decoration_y(self, uuid : int, target_y : int):
        self.decorations_data.loc[self.decorations_data["uuid"] == uuid, ["y",]] = target_y

    def set_decoration_r(self, uuid : int, target_r : int):
        self.decorations_data.loc[self.decorations_data["uuid"] == uuid, ["r",]] = target_r

    def set_decoration_fv(self, uuid : int, target_fv : int):
        self.decorations_data.loc[self.decorations_data["uuid"] == uuid, ["fv",]] = target_fv

    def remove_decoration_by_uuid(self, uuid : int):
        self.decorations_data = self.decorations_data.drop(self.decorations_data[self.decorations_data["uuid"] == uuid].index)

    def remove_decoration_by_hash(self, hash : int):
        pass

    def add_decoration(self):
        pass