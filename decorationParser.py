from bs4 import BeautifulSoup
import requests
from mtx_exceptions import *


class DecorationParser:
    HIDEOUT_DECORATION_CATEGORIES_URL = "https://poedb.tw/us/Hideout_Doodads"
    DECORATION_URL_TEMPLATE = "https://poedb.tw/us/{}"
    OUTPUT_FILE_PATH = "decorations_list.txt"
    OUTPUT_DATA_FORMAT = "{decoration_name},{mtx_state}"


    @classmethod
    def parse_all_decorations(cls):
        print("Start parsing all PoE decorations")

        decorations = []
        mtx_statuses = []
        page = requests.get(cls.HIDEOUT_DECORATION_CATEGORIES_URL)
        soup = BeautifulSoup(page.text, "html.parser")

        categories = soup.select("div.table-responsive > table > tbody > tr > td > a")

        for category in categories:
            found_decorations, found_states = DecorationParser.parse_category(category.get_text())

            decorations.extend(found_decorations)
            mtx_statuses.extend(found_states)

        print("All PoE decorations successfully parsed")

        cls.make_output_file(decorations, mtx_statuses)

    @classmethod
    def parse_category(cls, category_name : str) -> tuple[list[str], list[int]]:
        print("Start working with {} category".format(category_name))

        url = cls.DECORATION_URL_TEMPLATE.format(category_name.replace(" ", "_"))
        page = requests.get(url)

        if not page:
            print("Cannot access {} category page".format(category_name))
            return [], []

        soup = BeautifulSoup(page.text, "html.parser")

        # Getting all MTX (skins and decorations)
        # to compare with all found category decorations
        mtxs_container = soup.find("div", {"id" : category_name.replace(" ", "") + "MTX"})
        mtx_decorations = []     

        if mtxs_container:
            mtxs_data = mtxs_container.select("div.flex-grow-1 > a")
        
            for mtx in mtxs_data:
                mtx_decorations.append(mtx.get_text())

        # Getting all category decorations
        decorations_container = soup.find("div", {"id" : category_name.replace(" ", "") + "DoodadCategory"})

        if not decorations_container:
            print("Parsing {} category skipped".format(category_name))
            return [], []

        decorations_data = decorations_container.select("div.flex-grow-1 > a")
        decorations = []
        mtx_statuses = []

        for decoration in decorations_data:
            decoration_name = decoration.get_text()
            
            decorations.append(decoration_name)

            if category_name in EXCEPTIONS.keys() and decoration_name in EXCEPTIONS.get(category_name).keys():
                mtx_statuses.append(EXCEPTIONS.get(category_name).get(decoration_name))
            else:
                mtx_statuses.append(1 if decoration_name in mtx_decorations else 0)

        print("Category {} successfully parsed".format(category_name))

        return decorations, mtx_statuses
    
    @classmethod
    def make_output_file(cls, decorations : list[str], mtx_statuses : list[int]):
        print("Start making output file")

        if len(decorations) != len(mtx_statuses):
            print("Make output file error: different len of parameters")
            return

        with open(cls.OUTPUT_FILE_PATH, "w") as file:
            decorations_count = len(decorations)

            for i in range(decorations_count):
                file.write(cls.OUTPUT_DATA_FORMAT.format(decoration_name = decorations[i], mtx_state = mtx_statuses[i]))

                if i < decorations_count - 1:
                    file.write("\n")
        
        print("Output file successully maded")


if __name__ == "__main__":
    DecorationParser.parse_all_decorations()
