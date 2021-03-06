import os
from main_download import MainDownload

# Winter 2018 Anime
class Winter2018AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2018-1"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

# Beatless
class BeatlessDownload(Winter2018AnimeDownload):

    IMAGE_URL = "http://beatless-anime.jp/images/episodes_%s.jpg"
    INTER_IMAGE_URL = "http://beatless-anime.jp/images/episodes_inter%s.jpg"
    FINAL_EPISODE = 24
    NUM_OF_INTER_EPISODES = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/beatless"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + ".jpg"):
                    continue
                imageUrl = self.IMAGE_URL % episode
                filepathWithoutExtension = self.base_folder + "/" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
            for i in range(1, self.NUM_OF_INTER_EPISODES + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/inter" + episode + ".jpg"):
                    continue
                imageUrl = self.INTER_IMAGE_URL % episode
                filepathWithoutExtension = self.base_folder + "/inter" + episode
                self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Darling in the FranXX
class DarlingInTheFranxxDownload(Winter2018AnimeDownload):

    IMAGE_URL = "https://darli-fra.jp/assets/img/common/story/%s/%s_%s.jpg"
    FINAL_EPISODE = 24
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/darling-in-the-franxx"
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
                    imageUrl = self.IMAGE_URL % (episode, episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Death March kara Hajimaru Isekai Kyousoukyoku
class DeathMarchDownload(Winter2018AnimeDownload):

    STORY_PAGE = "https://deathma-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/death-march"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ol class="list_story">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ol>')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.STORY_PAGE + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split3 = page_response.split('<div class="detail">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</section>')[0].split('<img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Grancrest Senki
class GrancrestSenkiDownload(Winter2018AnimeDownload):

    IMAGE_URL = "https://grancrest-anime.jp/assets/img/common/story/%s/%s.jpg"
    FINAL_EPISODE = 24
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/grancrest-senki"
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

# Hakumei to Mikochi
class HakumikoDownload(Winter2018AnimeDownload):

    IMAGE_URL = "http://hakumiko.com/images/story/%s/p_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hakumiko"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            episodes = []
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                episodes.append(episode)
            episodes.append('ova')
            for ep in episodes:
                if self.is_file_exists(self.base_folder + "/" + ep + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1).zfill(3)
                    imageUrl = self.IMAGE_URL % (ep.zfill(3), imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + ep + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
    
# Karakai Jouzu no Takagi-san
class TakagisanDownload(Winter2018AnimeDownload):
    
    IMAGE_URL = "https://takagi3.me/1st/images/story%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_PICTURES = [4, 4, 6, 4, 5, 5, 4, 4, 4, 4, 5, 3]
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/takagi-san"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_PICTURES[i]):
                    imageNum = str(j+1).zfill(2)
                    imageUrl = self.IMAGE_URL % (episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Marchen Madchen
class MarchenMadchenDownload(Winter2018AnimeDownload):

    PAGE_PREFIX = "https://maerchen-anime.com/"
    STORY_URL = "https://maerchen-anime.com/result/%s.html"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/marchen-madchen"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                response = self.get_response(self.STORY_URL % episode)
                split1 = response.split('<div class="ph"><a href="../')
                for j in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Mitsuboshi Colors
class MitsuboshiColorsDownload(Winter2018AnimeDownload):

    STORY_URL = "http://mitsuboshi-anime.com/story/vol%s/"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/mitsuboshi-colors"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg"):
                    continue
                response = self.get_response(self.STORY_URL % str(i+1))
                split1 = response.split('<div class="storyText">')
                if len(split1) < 2:
                    continue
                split2 = split1[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split2), 1):
                    imageUrl = split2[j].split('"')[0].replace('-600x338','').replace('-400x224','')
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j).zfill(2)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Overlord II
class Overlord2Download(Winter2018AnimeDownload):
    
    IMAGE_PREFIX = "http://overlord-anime.com/assets/story/"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/overlord2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageUrl = self.IMAGE_PREFIX + str(i+1) + '_' + str(j+1) + '.jpg'
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Pop Team Epic
class PopTeamEpicDownload(Winter2018AnimeDownload):

    IMAGE_URL = "http://hoshiiro.jp/img/story/img_%s_%s.png"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 9
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/pop-team-epic"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1).zfill(2)
                    imageUrl = self.IMAGE_URL % (episode, imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Ramen Daisuki Koizumi-san
class RamenKoizumiDownload(Winter2018AnimeDownload):

    IMAGE_URL = "http://ramen-koizumi.com/img/story/ep%s/img%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ramen-koizumi"
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

# Ryuuou no Oshigoto!
class RyuohDownload(Winter2018AnimeDownload):

    IMAGE_URL = "http://www.ryuoh-anime.com/story/images/%s-%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ryuoh"
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

# Slow Start
class SlowStartDownload(Winter2018AnimeDownload):

    IMAGE_URL = "https://slow-start.com/uploads/story%s_%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 3
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/slow-start"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (str(i), imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Sora yori mo Tooi Basho
class YorimoiDownload(Winter2018AnimeDownload):

    IMAGE_URL = "http://yorimoi.com/assets/story/%s_%s.jpg"
    FINAL_EPISODE = 13
    NUM_OF_PICTURES_PER_PAGE = 6
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yorimoi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                for j in range(self.NUM_OF_PICTURES_PER_PAGE):
                    imageNum = str(j+1)
                    imageUrl = self.IMAGE_URL % (str(i), imageNum)
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Toji no Miko
class TojiNoMikoDownload(Winter2018AnimeDownload):
    
    PAGE_PREFIX = "http://tojinomiko.jp/"
    STORY_URL = "http://tojinomiko.jp/story/%s.html"
    FINAL_EPISODE = 24
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/toji-no-miko"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                response = self.get_response(self.STORY_URL % episode)
                split1 = response.split('<div class="ph"><a href="../')
                for j in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Yuru Camp
class YuruCampDownload(Winter2018AnimeDownload):

    IMAGE_URL = "https://yurucamp.jp/first/story/images/%s/%s.jpg"
    FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 8
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yurucamp"
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
