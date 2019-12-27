import os
from main_download import MainDownload

# Winter 2019 Anime
class Winter2019AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2019-1"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

# Egao no Daika
class EgaoNoDaikaDownload(Winter2019AnimeDownload):
    
    IMAGE_PREFIX = "http://egaonodaika.com/"
    PAGE_LINK = "http://egaonodaika.com/story/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/egao-no-daika"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div class=\"storyNo" + str(i+1) + " box_story\">")
                if len(first_split) < 2:
                    break
                second_split = first_split[1].split("<ul class=\"img_thum\">")
                if len(second_split) < 2:
                    break
                third_split = second_split[1].split("</ul>")
                textBlocks = third_split[0].split("src=\"../")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Endro
class EndroDownload(Winter2019AnimeDownload):
    
    PAGE_LINK = "http://www.endro.jp/"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 5
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/endro"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                first_split = response.split("<div class=\"storyNo" + episode + " box_story\">")
                if len(first_split) < 2:
                    break
                second_split = first_split[1].split("<ul class=\"img_thum\">")
                if len(second_split) < 2:
                    break
                third_split = second_split[1].split("</ul>")
                textBlocks = third_split[0].split("src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_LINK + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Girly Air Force
class GirlyAirForceDownload(Winter2019AnimeDownload):
    
    PAGE_LINK = "http://www.gaf-anime.jp/story.html"
    IMAGE_PREFIX = "http://www.gaf-anime.jp"
    # FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 5
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/girly-air-force"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_LINK)
            if len(response) == 0:
                return
            first_split = response.split("<div class=\"story_slide02_area\">")
            for i in range(len(first_split)):
                if i == 0:
                    continue
                second_split = first_split[i].split("<ul class=\"story_slide03\">")
                if len(second_split) < 2:
                    continue
                third_split = second_split[1].split("</ul>")
                episode = str(i).zfill(2)
                textBlocks = third_split[0].split("src=\".")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
                
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Gotoubun no Hanayome
class GotoubunDownload(Winter2019AnimeDownload):

    PAGE_PREFIX = "http://www.tbs.co.jp/anime/5hanayome/story/"
    # FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/gotoubun"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            page_response = self.get_response(self.PAGE_PREFIX)
            if (len(page_response) == 0):
                return
            main_page_split = page_response.split("<ul class=\"storynav clearfix\">")
            if (len(main_page_split) < 2):
                return
            main_page_split2 = main_page_split[1].split("</ul>")
            page_split = main_page_split2[0].split("<li><a href=\"")
            if len(page_split) < 2:
                return
            for i in range(len(page_split)):
                if i == 0:
                    continue
                episode = str(i).zfill(2)
                page_url = page_split[i].split("\"")[0]
                link = self.PAGE_PREFIX + page_url
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("<ul class=\"slides\">")
                if len(first_split) < 2:
                    break
                textBlocks = first_split[1].split("<img src=\"")
                for j in range(self.NUM_OF_PICTURES_PER_PAGE + 1):
                    if j == 0:
                        continue
                    imageUrl = self.PAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Kaguya-sama wa Kokurasetai
class KaguyasamaDownload(Winter2019AnimeDownload):

    PAGE_PREFIX = "https://kaguya.love/story/"
    PAGE_SUFFIX = ".html"
    IMAGE_PREFIX = "https://kaguya.love"
    FINAL_EPISODE = 12
    #NUM_OF_PICTURES_PER_PAGE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kaguya-sama"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                link = self.PAGE_PREFIX + episode + self.PAGE_SUFFIX
                response = self.get_response(link)
                if len(response) == 0:
                    break
                first_split = response.split("<div class=\"swiper-wrapper\">")
                if len(first_split) < 2:
                    return
                second_split = first_split[1].split("<div class=\"swiper-my-pagination\">")
                textBlocks = second_split[0].split("<img src=\"")
                if len(textBlocks) < 2:
                    return
                for j in range(len(textBlocks)):
                    if j == 0:
                        continue
                    imageUrl = self.IMAGE_PREFIX + textBlocks[j].split("\"")[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

class MahouShoujoTokushusenAsukaDownload(Winter2019AnimeDownload):
    
    PAGE_PREFIX = "http://magical-five.jp/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/mahou-shoujo-asuka"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.PAGE_PREFIX)
            split1 = response.split('<div id="StoryData">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div id="S_itl1">')[0].split('<div class="slider-sceneImage">')
            for i in range(len(split2) - 1, 0, -1):
                episode = str(len(split2) - i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                split3 = split2[i].split('<img src=".')
                for j in range(1, len(split3), 1):
                    imageUrl = self.PAGE_PREFIX + split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)    

class MiniTojiDownload(Winter2019AnimeDownload):
    
    PAGE_PREFIX = "http://minitoji.jp/"
    STORY_PAGE = "http://minitoji.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/mini-toji"
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
                episode = str(i-2).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<div class="block line_01">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('<div class="cate_bottom_tag">')[0].split('<img src="../')
                for j in range(1, len(split4), 1):
                    imageUrl = self.PAGE_PREFIX + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)  

class TateNoYuushaDownload(Winter2019AnimeDownload):
    
    PAGE_PREFIX = "http://shieldhero-anime.jp"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tate-no-yuusha"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.PAGE_PREFIX)
            split1 = response.split('<article class="p-intro">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</article>')[0].split('<div class="main">')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                split3 = split2[i].split('</div>')[0].split('<img src="')
                for j in range(1, len(split3), 1):
                    imageUrl = self.PAGE_PREFIX + split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e) 
    
class WatatenDownload(Winter2019AnimeDownload):
    
    PAGE_PREFIX = "http://watatentv.com/"
    STORY_PAGE = "http://watatentv.com/story.html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/wataten"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div class="flex_box_cb_wrap">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div class="clear"></div>')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<ol class="main">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</ol>')[0].split('<img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = self.PAGE_PREFIX + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
