import json
from types import SimpleNamespace


class ArticleCustomAttributes:

    VsInfoArtikelNum: SimpleNamespace
    VsInfoEbene: SimpleNamespace
    VsInfoEbenenString: SimpleNamespace

    def __init__(self, data=None):
        if data is None:
            with open("src/pyweclapp/cat/json_data/article.json", "r") as f:
                data = json.load(f)
        for key, value in data.items():
            setattr(self, key, SimpleNamespace(**value))
