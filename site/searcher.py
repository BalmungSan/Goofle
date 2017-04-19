import pymongo
from pymongo import MongoClient
from collections import defaultdict

class Searcher:
  def __init__ (self):
    self.client = MongoClient('10.131.137.188', 27017)
    self.db = self.client.grupo_04
    self.db.authenticate("user1", "sepelu.2017")
    self.goofle = self.db.goofle
    self.spchars = {"á":"a", "à":"a", "â":"a", "ä":"a", "é":"e",
                    "è":"e", "ê":"e", "ë":"e", "í":"i", "ì":"i",
                    "î":"i", "ï":"i", "ó":"o", "ò":"o", "ô":"o",
                    "ö":"o", "ú":"u", "ù":"u", "û":"u", "ü":"u",
                    "ñ":"n", "!":"", "|":"", "°":"", "¬":"", "\"":""
                    "#":"", "$":"", "%":"", "&":"", "/":"", "(":"",
                    ")":"", "=":"", "'":"", "?":"", "¡":"", "¿":""
                    "@":"", "¨":"", "´":"", "+":"", "*":"", "~":""
                    "<":"", ">":"", "{":"", "[":"", "^":"", "}":""
                    "`":"", "]":"", ";":"", ",":"", ".":"", ":":""
                    "-":"", "_":"" }
  
  def search (self, words, top):
    result = defaultdict(lambda:0)
    for word in words:
      word = word.lower()
      for v, c in self.spchars.items():
        word = word.replace(v, c)
      files = self.goofle.find_one({"word": word}, {"_id": False, "files": True})
      if files is None:
        continue
      for _file in files["files"]:
        file, count = _file.values()
        result[file] += count
    resultlist = sorted(result.items(), key=lambda x:x[1], reverse = True)
    return resultlist[:top]

