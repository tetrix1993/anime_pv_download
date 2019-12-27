import os
from main_download import MainDownload

# Fall 2018 Anime
class Fall2018AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2018-4"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

# Akanesasu Shoujo
class AkanesasuShoujoDownload(Fall2018AnimeDownload):
    
    PAGE_PREFIX = "http://akanesasushojo.com/"
    STORY_PAGE = "http://akanesasushojo.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/akanesasu-shoujo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(2, len(split2), 1):
                episode = str(i-1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_02">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div id="ext_area_02">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Anima Yell!
class AnimaYellDownload(Fall2018AnimeDownload):
    
    PAGE_PREFIX = "http://www.animayell.com/"
    STORY_PAGE = "http://www.animayell.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/anima-yell"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(2, len(split2), 1):
                episode = str(i-1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_03">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="cate_bottom_tag">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Beelzebub-jou no Okinimesu mama.
class BeelmamaDownload(Fall2018AnimeDownload):
    
    PAGE_PREFIX = "https://beelmama.com/"
    STORY_PAGE = "https://beelmama.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/beelmama"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<nav class="story_tab">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</nav>')[0].split('<a href="./')
            for i in range(2, len(split2), 1):
                episode = str(i-1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.STORY_PAGE + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="wrap clearfix">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</div>')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Goblin Slayer
class GoblinSlayerDownload(Fall2018AnimeDownload):

    PAGE_PREFIX = "http://goblinslayer.jp/"
    STORY_PAGE = "http://goblinslayer.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/goblin-slayer"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<h3>')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(len(split2) - 1, 0, -1):
                page_url = split2[i].split('"')[0]
                split3 = page_url.split('/')
                if len(split3) < 2:
                    continue
                episode = ""
                temp1 = split3[len(split3) - 1].split('episode')
                if len(temp1) < 2:
                    continue
                temp2 = temp1[1]
                if temp2 == '_special':
                    episode = 'sp'
                else:
                    try:
                        temp3 = int(temp2)
                    except:
                        continue
                    episode = temp2
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_response = self.get_response(page_url)
                split4 = page_response.split('<ul class="bxslider">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split5), 1):
                    imageUrl = split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Hangyakusei Million Arthur
class HangyakuseiMillionArthurDownload(Fall2018AnimeDownload):
    
    PAGE_PREFIX = "http://hangyakusei-anime.com/"
    STORY_PAGE = "http://hangyakusei-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hangyakusei"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_01">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="block line_02">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Irozuku Sekai no Ashita kara
class IrodukuDownload(Fall2018AnimeDownload):

    PAGE_PREFIX = "http://www.iroduku.jp/"
    STORY_PAGE = "http://iroduku.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/iroduku"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ul class="img_thum">')
            for i in range(1, len(split1), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split2 = split1[i].split('</ul>')[0].split('<img src="../')
                for j in range(1, len(split2), 1):
                    imageUrl = self.PAGE_PREFIX + split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Kishuku Gakkou no Juliet
class KishukuJulietDownload(Fall2018AnimeDownload):
    
    PAGE_PREFIX = "https://www.juliet-anime.com/"
    STORY_PAGE = "https://www.juliet-anime.com/story/index.html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kishuku-juliet"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div id="cms_block">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div class="main_sa08">')[0].split('<div class="nwu_box">')
            for i in range(len(split2) - 1, 0, -1):
                episode = str(len(split2) - i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split3 = split2[i].split('<a href="../')
                if len(split3) < 2:
                    continue
                page_url = self.PAGE_PREFIX + split3[1].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="block line_01">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="block line_02">')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Merc Storia: Mukiryoku no Shounen to Bin no Naka no Shoujo
class MercStoriaDownload(Fall2018AnimeDownload):
    
    PAGE_PREFIX = "http://www.mercstoria.jp/"
    STORY_PAGE = "http://www.mercstoria.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/merc-storia"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<h3>')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(len(split2) - 1, 0, -1):
                page_url = split2[i].split('"')[0]
                split3 = page_url.split('episode')
                if len(split3) < 2:
                    continue
                episode = ""
                temp1 = split3[1].split('.html')[0]
                try:
                    temp2 = int(temp1)
                except:
                    continue
                episode = temp1
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.STORY_PAGE + page_url
                page_response = self.get_response(page_url)
                split4 = page_response.split('<ul class="bxslider">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split5), 1):
                    imageUrl = self.STORY_PAGE + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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
    