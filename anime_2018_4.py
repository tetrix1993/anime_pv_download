import os
from main_download import MainDownload

# Fall 2018 Anime
class Fall2018AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2018-4"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

# Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai
class AobutaDownload(Fall2018AnimeDownload):
    
    PAGE_PREFIX = "https://ao-buta.com/"
    STORY_PAGE = "https://ao-buta.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/aobuta"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<nav class="page_tab">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</nav>')[0].split('<a href="./')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.STORY_PAGE + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<div class="img_list">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</ul>')[0].split('<img src="../')
                for j in range(1, len(split4), 1):
                    imageUrl = self.PAGE_PREFIX + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
    