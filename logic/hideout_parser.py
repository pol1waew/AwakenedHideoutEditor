import pandas as pd
import re
import uuid


class HideoutParser:
    VERSION_REGEX = r'"version"\s*:\s*(\d+)'
    LANGUAGE_REGEX = r'"language"\s*:\s*"([\w\s]+)"'
    HIDEOUT_NAME_REGEX = r'"hideout_name"\s*:\s*"([\w\s]+)"'
    HIDEOUT_HASH_REGEX = r'"hideout_hash"\s*:\s*(\d+)'
    DECORATIONS_REGEX = r'"([\w\s]+)"\s*:\s*{\s*"hash"\s*:\s*(\d+),\s*"x"\s*:\s*(\d+),\s*"y"\s*:\s*(\d+),\s*"r"\s*:\s*(\d+),\s*"fv"\s*:\s*(\d+)\s*}'


    def parse_hideout_file(self, file_path : str) -> bool:
        """Parse hideout file from file_path

        Returns a bool value indicating the success of file parsing. Will return False if file not exists. 
        """
        
        with open(file_path, "r") as file:
            hideout_data = file.read()
            
            try:
                self.version = re.search(self.VERSION_REGEX, hideout_data).group(1)
                self.language = re.search(self.LANGUAGE_REGEX, hideout_data).group(1)
                self.hideout_name = re.search(self.HIDEOUT_NAME_REGEX, hideout_data).group(1)
                self.hideout_hash = re.search(self.HIDEOUT_HASH_REGEX, hideout_data).group(1)
            except AttributeError:
                return False
            
            doodads_raw_data = re.findall(self.DECORATIONS_REGEX, hideout_data)

            if not doodads_raw_data:
                return False

            self.doodads_data = pd.DataFrame(doodads_raw_data, columns=["name", "hash", "x", "y", "r", "fv"])
            self.doodads_data.insert(0, "uuid", None)

            self.doodads_data = self.doodads_data.astype({"uuid" : str, "name" : str, "hash" : int, 
                                                          "x" : int, "y" : int, "r" : int, "fv" : int})

            self.doodads_data["uuid"] = self.doodads_data["uuid"].apply(lambda id: uuid.uuid4())
            return True

    def make_output_file(self, file_path : str):
        with open(file_path, "w") as file:
            file.write("qweqeqwe")

    def set_decoration_location(self, uuid : int, target_x : int, target_y : int):
        self.doodads_data.loc[self.doodads_data["uuid"] == uuid, ["x",]] = target_x
        self.doodads_data.loc[self.doodads_data["uuid"] == uuid, ["y",]] = target_y

    def set_decoration_r(self, uuid : int, target_r : int):
        self.doodads_data.loc[self.doodads_data["uuid"] == uuid, ["r",]] = target_r

    def set_decoration_fv(self, uuid : int, target_fv : int):
        self.doodads_data.loc[self.doodads_data["uuid"] == uuid, ["fv",]] = target_fv

    def remove_decoration_by_uuid(self, uuid : int):
        self.doodads_data = self.doodads_data.drop(self.doodads_data[self.doodads_data["uuid"] == uuid].index)

    def remove_decoration_by_hash(self, hash : int):
        pass

    def add_decoration(self):
        pass