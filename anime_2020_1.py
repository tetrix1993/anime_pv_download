import os
from main_download import MainDownload

# Darwin's Game https://darwins-game.com/story/ #Dゲーム @d_game_official [WED]
# Eizouken http://eizouken-anime.com/story/ #映像研 @Eizouken_anime [THU]
# Gotoubun no Hanayome http://www.tbs.co.jp/anime/5hanayome/ #五等分の花嫁 @5Hanayome
# Hatena Illusion http://hatenaillusion-anime.com/ #はてなイリュージョン #hatenaillusion @hatena_anime
# Heya Camp https://yurucamp.jp/heyacamp/ #ゆるキャン #へやキャン @yurucamp_anime [WED]
# Infinite Dendrogram http://dendro-anime.jp/story/ #デンドロ @dendro_anime
# Isekai Quartet 2 http://isekai-quartet.com/story/ #いせかる @isekai_quartet
# Ishuzoku Reviewers https://isyuzoku.com/story/ #isyuzoku @isyuzoku
# Itai no wa https://bofuri.jp/story/ #防振り @bofuri_anime
# Jibaku Shounen Hanako-kun https://www.tbs.co.jp/anime/hanakokun/story/ #花子くん #花子くんアニメ @hanakokun_info
# Koisuru Asteroid http://koiastv.com/story.html #koias #koiastv #恋アス @koiastv [SUN]
# Kyokou Suiri https://kyokousuiri.jp/ #虚構推理 @kyokou_suiri
# Murenase! Seton Gakuen https://anime-seton.jp/story/ #シートン #群れなせシートン学園 @anime_seton [TUE]
# Nekopara https://nekopara-anime.com/ja/story/ #ネコぱら @nekopara_anime
# Plunderer http://plunderer-info.com/ #プランダラ @plundereranime
# Rikekoi https://rikekoi.com/story #リケ恋 @rikeigakoini
# Somali https://somali-anime.com/ #ソマリと森の神様 @somali_anime
# Toaru Kagaku no Railgun T https://toaru-project.com/railgun_t/story/ #超電磁砲T @toaru_project

# Winter 2020 Anime
class Winter2020AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-1"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

# Darwin's Game
class DarwinsGameDownload(Winter2020AnimeDownload):
    STORY_PAGE = "https://darwins-game.com/story/"
    PAGE_PREFIX = "https://darwins-game.com/story/?id=ep"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/darwins-game"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ul class="story_list">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="./?id=ep')
            for i in range(1, len(split2), 1):
                episode_num = ''
                try:
                    episode_num = split2[i].split('"')[0]
                    temp = int(episode_num)
                except:
                    continue
                episode = episode_num.zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + episode_num
                page_response = self.get_response(page_url)
                split3 = page_response.split('<div class="slider clearfix">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</div>')[0].split('<img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = self.STORY_PAGE + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Eizouken ni wa Te wo Dasu na!
class EizoukenDownload(Winter2020AnimeDownload):
    PAGE_PREFIX = "http://eizouken-anime.com"
    STORY_DATA_JSON = "http://eizouken-anime.com/story/story_data.json"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/eizouken"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            story_json = self.get_json(self.STORY_DATA_JSON)
            story_data = story_json['data']
            for data in story_data:
                name = data['name']
                episode_num = name.split('.html')[0]
                try:
                    temp = int(episode_num)
                except:
                    continue
                episode = episode_num.zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg"):
                    continue
                html = data['html']
                split1 = html.split('<img src="')
                for i in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[i].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(i).zfill(2)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Gotoubun no Hanayome 2
class Gotoubun2Download(Winter2020AnimeDownload):

    PAGE_PREFIX = "http://www.tbs.co.jp/anime/5hanayome/story/"
    # FINAL_EPISODE = 12
    NUM_OF_PICTURES_PER_PAGE = 4

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/gotoubun2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        return
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

# Hatena Illusion
class HatenaIllusionDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "http://hatenaillusion-anime.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hatena-illusion"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Heya Camp
class HeyaCampDownload(Winter2020AnimeDownload):
    
    PAGE_PREFIX = "https://yurucamp.jp/news/page/"
    FINAL_EPISODE = 13
    FIRST_EPISODE_ARTICLE_ID = 5138
    FINAL_EPISODE_ARTICLE_ID = 10000 # to be updated
    
    CHAR_DAI = "\\xe7\\xac\\xac" #第
    CHAR_WA = "\\xe8\\xa9\\xb1" #話
    
    MAX_PAGES = 20 # To avoid infinite loop
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/heya-camp"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            page = 0
            loop = True
            while page < self.MAX_PAGES and loop:
                page += 1
                page_url = self.PAGE_PREFIX + str(page)
                response = self.get_response(page_url)
                split1 = response.split('<ul id="articleList">')
                if len(split1) < 2:
                    continue
                split2 = split1[1].split("wp-pagenavi")[0].split('<li><a href="')
                for i in range(1, len(split2), 1):
                    article_url = split2[i].split('"')[0]
                    article_url_split = article_url.split('/')
                    article_id = article_url_split[len(article_url_split) - 1]
                    if int(article_id) < self.FIRST_EPISODE_ARTICLE_ID:
                        loop = False
                        break
                    split3 = split2[i].split('<p class="articleTitle">')
                    if len(split3) < 2:
                        continue
                    article_title = split3[1].split('</p>')[0]
                    if self.CHAR_DAI in article_title and self.CHAR_WA in article_title:
                        split4 = article_title.split(self.CHAR_WA)[0].split(self.CHAR_DAI)
                        if len(split4) < 2:
                            continue
                        episode_num = split4[1]
                        try:
                            temp = int(episode_num) # check if it is an integer
                            episode = episode_num.zfill(2)
                            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                                continue
                            article_response = self.get_response(article_url)
                            split5 = article_response.split('<article>')
                            if len(split5) < 2:
                                continue
                            split6 = split5[1].split('</article>')[0].split('<p><a href="')
                            for j in range(1, len(split6), 1):
                                imageUrl = split6[j].split('"')[0]
                                filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                                self.download_image(imageUrl, filepathWithoutExtension)
                        except Exception as e:
                            print("Error in running " + self.__class__.__name__)
                            print(e)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Infinite Dendrogram
class InfiniteDendrogramDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "http://dendro-anime.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/infinite-dendrogram"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Isekai Quartet 2
class IsekaiQuartet2Download(Winter2020AnimeDownload):
    PAGE_PREFIX = "http://isekai-quartet.com/"
    STORY_PAGE = "http://isekai-quartet.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/isekai-quartet2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        return
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div id="S_')
            for i in range(len(split1)-1, 0, -1):
                num = split1[i].split('"')[0]
                try:
                    number = int(num)
                except Exception as e:
                    continue
                episode = str(number).zfill(2)
                split2 = split1[i].split('<div class="slider-sceneImage">')
                #print('daaaaa')
                if len(split2) < 2:
                    continue
                #print('goooo')
                split3 = split2[1].split('<div class="ep-text">')[0].split('<img src="')
                for j in range(1, len(split3), 1):
                    split4 = split3[j].split('../')
                    if len(split4) < 2:
                        continue
                    imageUrl = self.PAGE_PREFIX + split4[1].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

# Ishuzoku Reviewers
class IshuzokuReviewersDownload(Winter2020AnimeDownload):
    PAGE_PREFIX = "https://isyuzoku.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ishuzoku-reviewers"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.
class BofuriDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "https://bofuri.jp/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/bofuri"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Jibaku Shounen Hanako-kun
class HanakoKunDownload(Winter2020AnimeDownload):
    PAGE_PREFIX = "https://www.tbs.co.jp/anime/hanakokun/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hanako-kun"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Koisuru Asteroid
class KoisuruAsteroidDownload(Winter2020AnimeDownload):
    STORY_PAGE = "http://koiastv.com/story.html"
    PAGE_PREFIX = "http://koiastv.com/story"
    IMAGE_PREFIX = "http://koiastv.com/"
    PAGE_SUFFIX = ".html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/koisuru-asteroid"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<a href="story')
            for i in range(1, len(split1), 1):
                episode_split = split1[i].split('.html"')[0]
                try:
                    temp = int(episode_split)
                except Exception as e:
                    continue
                episode = episode_split.zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + episode_split + self.PAGE_SUFFIX
                page_response = self.get_response(page_url)
                split2 = page_response.split('<ol class="main">')
                if len(split2) < 2:
                    continue
                split3 = split2[1].split('</ol>')[0].split('<img src="')
                for j in range(1, len(split3), 1):
                    imageUrl = self.IMAGE_PREFIX + split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        

# Kyokou Suiri
class KyokouSuiriDownload(Winter2020AnimeDownload):
    PAGE_PREFIX = "https://kyokousuiri.jp/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kyokou-suiri"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Murenase! Seton Gakuen
class MurenaseSetonGakuenDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "https://anime-seton.jp/"
    STORY_PAGE = "https://anime-seton.jp/story/"
    FINAL_EPISODE = 13
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/murenase-seton"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<section class="story__list">')[1].split('</section>')[0].split('<li>')
            total_episodes = len(split1) - 1
            for i in range(total_episodes):
                episode = str(i+1).zfill(2)
                if (self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg")):
                    continue
                page_url = self.STORY_PAGE + "?ep=" + str(i+1)
                page_response = self.get_response(page_url)
                split2 = page_response.split('<ul class="slider">')
                if len(split2) < 2:
                    continue
                split3 = split2[1].split('</ul>')[0].split('<li><img src="')
                for j in range(1, len(split3), 1):
                    imageUrl = split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j).zfill(2)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Nekopara
class NekoparaDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "https://nekopara-anime.com/ja/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/nekopara"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Plunderer
class PlundererDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "http://plunderer-info.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/plunderer"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Rikei ga Koi ni Ochita no de Shoumei shitemita.
class RikekoiDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "https://rikekoi.com/story"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rikekoi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

class SomaliDownload(Winter2020AnimeDownload):
    PAGE_PREFIX = "https://somali-anime.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/somali"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass

# Toaru Kagaku no Railgun T
class RailgunTDownload(Winter2020AnimeDownload):

    PAGE_PREFIX = "https://toaru-project.com/railgun_t/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/railgun-t"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass