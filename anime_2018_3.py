import os
from main_download import MainDownload

# Summer 2018 Anime
class Summer2018AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2018-3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

# Angolmois: Genkou Kassenki
class AngolmoisDownload(Summer2018AnimeDownload):

    PAGE_PREFIX = "https://angolmois-anime.jp/"
    STORY_PAGE_PREFIX = "https://angolmois-anime.jp/story/"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/angolmois"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                response = self.get_response(self.STORY_PAGE_PREFIX + episode)
                split1 = response.split('<ul class="storySlider">')
                if len(split1) < 2:
                    return
                split2 = split1[1].split('</ul>')[0].split('<img src="../../')
                for j in range(1, len(split2), 1):
                    imageUrl = self.PAGE_PREFIX + split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Asobi Asobase
class AsobiAsobaseDownload(Summer2018AnimeDownload):
    
    IMAGE_PREFIX = "http://asobiasobase.com/assets/story/"
    STORY_PAGE = "http://asobiasobase.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/asobi-asobase"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div class="sub-menu">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div id="Content">')[0].split('<a href="./')
            for i in range(2, len(split2), 1):
                episode = str(i-1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(1, 7, 1):
                    imageUrl = self.IMAGE_PREFIX + str(i-1) + '_' + str(j) + '.jpg'
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Chio-chan no Tsuugakurou
class ChioChanDownload(Summer2018AnimeDownload):
    
    STORY_PAGE = "http://chiochan.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/chio-chan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div class="cts_box_bg" id="s')
            for i in range(len(split1) - 1, 0, -1):
                episode = ''
                try:
                    episode_num = int(split1[i].split('"')[0])
                    episode = str(episode_num).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split2 = split1[i].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split2), 1):
                    imageUrl = self.STORY_PAGE + split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Grand Blue
class GrandBlueDownload(Summer2018AnimeDownload):

    PAGE_PREFIX = "https://www.grandblue-anime.com/"
    STORY_PAGE = "https://www.grandblue-anime.com/story/introduction.html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/grand-blue"
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

# Hanebado!
class HanebadoDownload(Summer2018AnimeDownload):

    PAGE_PREFIX = "http://hanebad.com/img/story/ep"
    FINAL_EPISODE = 13
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hanebado"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + ".png"):
                    continue
                imageUrl = self.PAGE_PREFIX + str(i) + '.png'
                filepathWithoutExtension = self.base_folder + "/" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Happy Sugar Life
class HappySugarLifeDownload(Summer2018AnimeDownload):
    
    PAGE_PREFIX = "http://happysugarlife.tv/"
    STORY_PAGE = "http://happysugarlife.tv/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/happy-sugar-life"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ul class="swiper-wrapper">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<li class="')
            for i in range(len(split2) - 1, 0, -1):
                split3 = split2[i].split('<p class="txt01">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('th')[0].split('st')[0].split('nd')[0].split('rd')[0]
                episode = ''
                try:
                    episode = str(int(split4)).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split5 = split2[i].split('<a href="./')
                if (len(split5) < 2):
                    continue
                pageLink = self.STORY_PAGE + split5[1].split('"')[0]
                pageResponse = self.get_response(pageLink)
                split6 = pageResponse.split('<div class="swiper-wrapper">')
                if len(split6) < 2:
                    continue
                split7 = split6[1].split('</div>')[0].split('<img src="../../')
                for j in range(1, len(split7), 1):
                    imageUrl = self.PAGE_PREFIX + split7[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Harukana Receive
class HarukanaReceiveDownload(Summer2018AnimeDownload):
    
    IMAGE_PREFIX = "http://www.harukana-receive.jp/assets/story/"
    STORY_PAGE = "http://www.harukana-receive.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/harukana-receive"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div class="d-flex justify-content-center story-navi flex-wrap">')
            if len(split1) < 3:
                return
            split2 = split1[2].split('<section')[0].split('<a href="./')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(1, 7, 1):
                    imageUrl = self.IMAGE_PREFIX + str(i) + '_' + str(j) + '.jpg'
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Hataraku Saibou
class HatarakuSaibouDownload(Summer2018AnimeDownload):
    
    PAGE_PREFIX = "https://hataraku-saibou.com/"
    STORY_PAGE = "https://hataraku-saibou.com/story/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hataraku-saibou"
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
                split3 = split2[i].split('?story=')
                if len(split3) < 2:
                    continue
                episode_url = split3[1].split('"')[0]
                if 'introduction' in episode_url:
                    continue
                episode = ''
                try:
                    episode = str(int(episode_url)).zfill(2)
                except:
                    episode = episode_url
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                pageUrl = self.STORY_PAGE + split2[i].split('"')[0]
                pageResponse = self.get_response(pageUrl)
                split4 = pageResponse.split('<div class="story_slider">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# High Score Girl
class HiScoreGirlDownload(Summer2018AnimeDownload):

    PAGE_LINK = "http://hi-score-girl.com/story/"
    PAGE_PREFIX = "http://hi-score-girl.com"
    FIRST_EPISODE = 1
    FINAL_EPISODE = 15
    NUM_OF_PICTURES_PER_PAGE = 3
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hi-score-girl"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            split1 = response.split('INTRODUCTION')
            if len(split1) < 2:
                return
            split2 = split1[1].split('INTRODUCTION II')[0].split('<div class="sm">')
            for i in range(1, len(split2), 1):
                episode = str(self.FIRST_EPISODE + i - 1).zfill(2)
                if (self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg")):
                    continue
                split3 = split2[i].split('<a href="..')
                if (len(split3) < 2):
                    continue
                pageLink = self.PAGE_PREFIX + split3[1].split('"')[0]
                pageResponse = self.get_response(pageLink)
                split4 = pageResponse.split('<div class="img_u wdxmax">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('<div class="block line_04">')[0]
                split6 = split5.split('<div class="ph"><a href="..')
                for j in range(1, len(split6), 1):
                    imageUrl = self.PAGE_PREFIX + split6[j].split('?')[0]
                    imageFileName = episode + '_' + str(j)
                    filepathWithoutExtension = self.base_folder + "/" + imageFileName
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e) 

# Hyakuren no Haou to Seiyaku no Valkyria
class HyakurenDownload(Summer2018AnimeDownload):

    STORY_PAGE = "http://hyakuren-anime.com/story/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hyakuren"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div id="slideshow')
            for i in range(1, len(split1), 1):
                episode = ''
                try:
                    episode = str(int(split1[i].split('"')[0])).zfill(2)
                except:
                    continue
                if (self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg")):
                    continue
                split2 = split1[i].split('<ul class="clearfix">')[0].split('<img src="')
                for j in range(1, len(split2), 1):
                    imageUrl = self.STORY_PAGE + split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e) 

# Isekai Maou to Shoukan Shoujo no Dorei Majutsu
class IsekaiMaouDownload(Summer2018AnimeDownload):
    
    STORY_PAGE = "https://isekaimaou-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/isekai-maou"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split("<div class=\\'story-item\\'>")
            for i in range(len(split1) - 1, 0, -1):
                episode = str(len(split1) - i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split2 = split1[i].split("<a href=\\'")
                if len(split2) < 2:
                    continue
                pageUrl = self.STORY_PAGE + split2[1].split("\\'")[0]
                pageResponse = self.get_response(pageUrl)
                split3 = pageResponse.split("<main id=\\'detail-main\\'")
                if len(split3) < 2:
                    continue
                split4 = split3[1].split("<br />")[0].split('<img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Island
class IslandDownload(Summer2018AnimeDownload):

    STORY_PAGE = "http://never-island.com/story/"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/island"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                response = self.get_response(self.STORY_PAGE + episode)
                split1 = response.split('<div class="slide_list">')
                if len(split1) < 2:
                    continue
                split2 = split1[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split2), 1):
                    imageUrl = split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Overlord III
class Overlord3Download(Summer2018AnimeDownload):
    
    IMAGE_PREFIX = "http://overlord-anime.com/assets/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/overlord3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageUrl = self.IMAGE_PREFIX + str(i+15) + '_' + str(j+1) + '.jpg'
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Satsuriku no Tenshi
class SatsurikuDownload(Summer2018AnimeDownload):
    
    IMAGE_URL = "http://satsuriku.com/images/story/%s/p_%s.jpg"
    FINAL_EPISODE = 16
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/satsuriku"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1).zfill(3)
                    imageUrl = self.IMAGE_URL % (episode.zfill(3), imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Shichisei no Subaru
class ShichiseiNoSubaruDownload(Summer2018AnimeDownload):
    
    IMAGE_PREFIX = "http://7subaru.jp/wp-content/themes/subaru/img/story/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/shichisei-no-subaru"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageUrl = self.IMAGE_PREFIX + episode + '/' + str(j+1).zfill(2) + '.png'
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Tsukumogami Kashimasu
class TsukumogamiDownload(Summer2018AnimeDownload):

    IMAGE_URL = "http://tsukumogami.jp/assets/img/common/story/img%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tsukumogami"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1).zfill(2)
                    imageUrl = self.IMAGE_URL % (episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Yuragi-sou no Yuuna-san
class YuragisouDownload(Summer2018AnimeDownload):

    IMAGE_URL = "https://yuragisou.com/assets/img/common/story/%s/%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yuragisou"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1).zfill(2)
                    imageUrl = self.IMAGE_URL % (episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
