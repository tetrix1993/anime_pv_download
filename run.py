# How to use
# Method 1:
#   Search the anime's full name (in romaji, not english title)
#
# Method 2:
#   Find out which season and the year of the anime you want when the anime first aired
#   Winter - 1, Spring - 2, Summer - 3, Fall - 4
#
#   E.g. Your anime first aired in Spring 2019, search '2019-2'
#   E.g. Your anime first aired in Fall 2018, search '2018-4'
#
#   Look below to see if your anime is listed there.
#
# Once you found your anime, remove the first '#' on the same line. Then run the script in command prompt/terminal (E.g. python run.py)

from multiprocessing import Process
from anime_2018_4 import *
from anime_2019_1 import *
from anime_2019_2 import *
from anime_2019_3 import *
from anime_2019_4 import *
from anime_2020_1 import *
from anime_2020_2 import *

def run_process(download):
    print("Running " + download.__class__.__name__ + " (" + str(os.getpid()) + ")")
    download.run()

def process_download(downloads):
    processes = []
    for download in downloads:
        process = Process(target=run_process, args=(download,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

def run():
    downloads = []
    
    # 2020-2 Spring 2020 Anime
    
    #downloads.append(GleipnirDownload()) #Gleipnir
    #downloads.append(HachinanDownload()) #Hachi-nan tte, Sore wa Nai deshou!
    #downloads.append(HamehuraDownload()) #Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...
    #downloads.append(Honzuki2Download()) #Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season
    #downloads.append(Kaguyasama2Download()) #Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen
    #downloads.append(MaohgakuinDownload()) #Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
    #downloads.append(Oregairu3Download()) #Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan
    #downloads.append(ReZero2Download()) #Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season
    #downloads.append(TamayomiDownload()) #Tamayomi
    #downloads.append(TeiboDownload()) #Houkago Teibou Nisshi
    #downloads.append(Tsugumomo2Download()) #Tsugu Tsugumomo
    #downloads.append(YesterdayDownload()) #Yesterday wo Utatte

    # 2020-1 Winter 2020 Anime
    
    #downloads.append(BofuriDownload()) #Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.
    #downloads.append(DarwinsGameDownload()) #Darwin's Game
    #downloads.append(EizoukenDownload()) #Eizouken ni wa Te wo Dasu na!
    #downloads.append(HatenaIllusionDownload()) #Hatena Illusion
    #downloads.append(HeyaCampDownload()) #Heya Camp
    #downloads.append(InfiniteDendrogramDownload()) #Infinite Dendrogram
    #downloads.append(IsekaiQuartet2Download()) #Isekai Quartet 2
    #downloads.append(IshuzokuReviewersDownload()) #Ishuzoku Reviewers
    #downloads.append(HanakoKunDownload()) #Jibaku Shounen Hanako-kun
    #downloads.append(KoisuruAsteroidDownload()) #Koisuru Asteroid
    #downloads.append(KyokouSuiriDownload()) #Kyokou Suiri
    #downloads.append(MurenaseSetonGakuenDownload()) #Murenase! Seton Gakuen
    #downloads.append(NekoparaDownload()) #Nekopara
    #downloads.append(PlundererDownload()) #Plunderer
    #downloads.append(RailgunTDownload()) #Toaru Kagaku no Railgun T
    #downloads.append(RikekoiDownload()) #Rikei ga Koi ni Ochita no de Shoumei shitemita.
    #downloads.append(SomaliDownload()) #Somali to Mori no Kamisama
    
    # 2019-4 Fall 2019 Anime
    
    #downloads.append(AssassinsPrideDownload()) #Assassins Pride
    #downloads.append(Bokuben2Download()) #Bokutachi wa Benkyou ga Dekinai!
    #downloads.append(ChoyoyuDownload()) #Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!
    #downloads.append(HonzukiDownload()) #Honzuki no Gekokujou
    #downloads.append(KandagawaJetGirlsDownload()) #Kandagawa Jet Girls
    #downloads.append(KemonomichiDownload()) #Hataage! Kemono Michi
    #downloads.append(NoukinDownload()) #Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!
    #downloads.append(NullPetaDownload()) #Null Peta
    #downloads.append(OresukiDownload()) #Ore wo Suki nano wa Omae dake ka yo
    #downloads.append(RifleIsBeautifulDownload()) #Rifle is Beautiful
    #downloads.append(SaikoroDownload()) #Houkago Saikoro Club
    #downloads.append(ShinchouYuushaDownload()) #Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru
    #downloads.append(ValLoveDownload()) #Val x Love
    
    # 2019-3 Summer 2019 Anime
    
    #downloads.append(ArifuretaDownload()) #Arifureta Shokugyou de Sekai Saikyou
    #downloads.append(DumbbellDownload()) #Dumbbell Nan Kilo Moteru?
    #downloads.append(GranbelmDownload()) #Granbelm
    #downloads.append(HensukiDownload()) #Kawaikereba Hentai demo Suki ni Natte Kuremasu ka?
    #downloads.append(IsekaiCheatDownload()) #Isekai Cheat Magician
    #downloads.append(JyoshimudaDownload()) #Joshikousei no Mudazukai
    #downloads.append(KanataNoAstraDownload()) #Kanata no Astra
    #downloads.append(MachikadoMazokuDownload()) #Machikado Mazoku
    #downloads.append(MaousamaRetryDownload()) #Maou-sama, Retry!
    #downloads.append(OkaasanOnlineDownload()) #Tsuujou Kougeki ga Zentai Kougeki de Ni-kai Kougeki no Okaasan wa Suki Desu ka?
    #downloads.append(SounanDesukaDownload()) #Sounan desu ka?
    #downloads.append(TejinaDownload()) #Tejina-senpai
    #downloads.append(UchinokoDownload()) #Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai.
    
    # 2019-2 Spring 2019 Anime
    
    #downloads.append(BokubenDownload()) #Bokutachi wa Benkyou ga Dekinai
    #downloads.append(ChoukadouGirlDownload()) #Chou Kadou Girl 1/6
    #downloads.append(HachinaiDownload()) #Hachigatsu no Cinderella Nine
    #downloads.append(HitoribocchiDownload()) #Hitoribocchi no Marumaru Seikatsu
    #downloads.append(IsekaiQuartetDownload()) #Isekai Quartet
    #downloads.append(KenjaNoMagoDownload()) #Kenja no Mago
    #downloads.append(MidaraNaAochanDownload()) #Midara na Ao-chan wa Benkyou ga Dekinai
    #downloads.append(NankokoDownload()) #Nande Koko ni Sensei ga!?
    #downloads.append(NobutsumaDownload()) #Nobunaga-sensei no Osanazuma
    #downloads.append(SenkosanDownload()) #Sewayaki Kitsune no Senko-san
    #downloads.append(SenryuuShoujoDownload()) #Senryuu Shoujo
    #downloads.append(YatogameDownload()) #Yatogame-chan Kansatsu Nikki
    #downloads.append(YunoDownload()) #Kono Yo no Hate de Koi wo Utau Shoujo YU-NO
    
    # 2019-1 Winter 2019 Anime
    
    #downloads.append(CircletPrincessDownload()) #Circlet Princess
    #downloads.append(DateALive3Download()) #Date A Live III
    #downloads.append(DomeKanoDownload()) #Domestic na Kanojo
    #downloads.append(EgaoNoDaikaDownload()) #Egao no Daika
    #downloads.append(EndroDownload()) #Endro~!
    #downloads.append(GirlyAirForceDownload()) #Girly Air Force
    #downloads.append(GotoubunDownload()) #Gotoubun no Hanayome
    #downloads.append(GrimmsNotesDownload()) #Grimms Notes The Animation
    #downloads.append(KaguyasamaDownload()) #Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen
    #downloads.append(MahouShoujoTokushusenAsukaDownload()) #Mahou Shoujo Tokushusen Asuka
    #downloads.append(MiniTojiDownload()) #Mini Toji
    #downloads.append(PastelMemoriesDownload()) #Pastel Memories
    #downloads.append(TateNoYuushaDownload()) #Tate no Yuusha no Nariagari
    #downloads.append(WatatenDownload()) #Watashi ni Tenshi ga Maiorita!
    
    # 2018-4 Fall 2018 Anime
    
    #downloads.append(AkanesasuShoujoDownload()) #Akanesasu Shoujo
    #downloads.append(AnimaYellDownload()) #Anima Yell!
    #downloads.append(AobutaDownload()) #Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai
    #downloads.append(BeelmamaDownload()) #Beelzebub-jou no Okinimesu mama.
    #downloads.append(ConceptionDownload()) #Conception
    #downloads.append(GoblinSlayerDownload()) #Goblin Slayer
    #downloads.append(HangyakuseiMillionArthurDownload()) #Hangyakusei Million Arthur
    #downloads.append(ImoimoDownload()) #Ore ga Suki nano wa Imouto dakedo Imouto ja Nai
    #downloads.append(IrodukuDownload()) #Irozuku Sekai no Ashita kara
    #downloads.append(KishukuJulietDownload()) #Kishuku Gakkou no Juliet
    #downloads.append(MercStoriaDownload()) #Merc Storia: Mukiryoku no Shounen to Bin no Naka no Shoujo
    #downloads.append(ReleaseTheSpyceDownload()) #Release the Spyce
    #downloads.append(SoraumiDownload()) #Sora to Umi no Aida
    #downloads.append(SsssGridmanDownload()) #SSSS.Gridman
    #downloads.append(TensuraDownload()) #Tensei shitara Slime datta Ken
    #downloads.append(TonariNoKyuuketsukiSanDownload()) #Tonari no Kyuuketsuki-san
    #downloads.append(UlyssesDownload()) #Ulysses: Jehanne Darc to Renkin no Kishi
    #downloads.append(UzamaidDownload()) #Uchi no Maid ga Uzasugiru!

    process_download(downloads)

if __name__ == '__main__':
    run()
