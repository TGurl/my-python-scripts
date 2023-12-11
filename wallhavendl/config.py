import os


class Config:
    #################################
    #     Configuration Options     #
    #################################
    revision = "0.2.6"
    # Enter your API key
    # you can get it here: https://wallhaven.cc/settings/account
    apikey = "bkTDRcx01DsAqm0KCuiP1raddn5Xqy87"

    # Where should the Wallpapers be stored?
    location = os.path.join("~", "Pictures", "walls", "downloads")
    # How many Wallpapers should be downloaded, should be multiples of the
    # value in the THUMBS Variable
    wpnumber = 48
    # What page to start downloading at, default and minimum of 1.
    startpage = 1
    # Type standard (newest, oldest, random, hits, mostfav), search,
    # collections  (for now only the default collection), useruploads
    # (if selected, only FILTER variable will change the outcome)
    type = "standard"
    # From which Categories should Wallpapers be downloaded, first number is
    # for General, second for Anime, third for People, 1 to enable category,
    # 0 to disable it
    categories = "000"
    # filter wallpapers before downloading, first number is for sfw content,
    # second for sketchy content, third for nsfw content, 1 to enable,
    # 0 to disable
    filter = "000"
    # Which Resolutions should be downloaded, leave empty for all (most common
    # resolutions possible, for details see wallhaven site), separate multiple
    # resolutions with , eg. 1920x1080,1920x1200
    resolution = ""
    # alternatively specify a minimum resolution, please note that specifying
    # both resolutions and a minimum resolution will result in the desired
    # resolutions being ignored, to avoid unwanted behavior only set one of the
    # two options and leave the other blank
    atleast = ""
    # Which aspectratios should be downloaded, leave empty for all (possible
    # values: 4x3, 5x4, 16x9, 16x10, 21x9, 32x9, 48x9, 9x16, 10x16), separate
    # mutliple ratios with , eg. 4x3,16x9
    aspectratio = ""
    # Which Type should be displayed (relevance, random, date_added, views,
    # favorites, toplist, toplist-beta)
    mode = "random"
    # if MODE is set to toplist show the toplist for the given timeframe
    # possible values: 1d (last day), 3d (last 3 days), 1w (last week),
    # 1M (last month), 3M (last 3 months), 6M (last 6 months), 1y (last year)
    toprange = ""
    # How should the wallpapers be ordered (desc, asc)
    order = "desc"
    # Collections, only used if TYPE  =  collections
    # specify the name of the collection you want to download
    # Default is the default collection name on wallhaven
    # If you want to download your own Collections make sure USR is set to
    # your username. If you want to download someone elses public collection
    # enter the name here and the username under USR
    # Please note that the only filter option applied to Collections is the
    # Number of Wallpapers to download, there is no filter for resolution,
    # purity, ...
    collection = "Default"
    # Searchterm, only used if TYPE  =  search
    # you can also search by tags, use id:TAGID
    # to get the tag id take a look at: https://wallhaven.cc/tags/
    # for example: to search for nature related wallpapers via the nature tag
    # instead of the keyword use QUERY = "id:37"
    query = ""
    # Search images containing color
    # values are RGB (000000  =  black, ffffff  =  white, ff0000  =  red, ...)
    color = ""
    # Should the search results be saved to a separate subfolder?
    # 0 for no separate folder, 1 for separate subfolder
    subfolder = 0
    # User from which wallpapers should be downloaded
    # used for TYPE = useruploads and TYPE = collections
    # If you want to download your own Collection this has to be set to your
    # username
    usr = "geertje"
    # use gnu parallel to speed up the download (0, 1), if set to 1 make sure
    # you have gnuparallel installed, see normal.vs.parallel.txt for
    # speed improvements
    # using this option can lead to cloudflare blocking some of the downloads
    parallel = 0
    # custom thumbnails per page
    # changeable here: https://wallhaven.cc/settings/browsing
    # valid values: 24, 32, 64
    # if set to 32 or 64 you need to provide an api key
    thumbs = 24
    #################################
    #   End Configuration Options   #
    #################################
