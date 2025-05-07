import requests
from pprint import pprint as print

def tiktok_video(link):
    url = "https://tiktok-download-without-watermark.p.rapidapi.com/analysis"

    querystring = {"url":link,"hd":"0"}

    headers = {
        "X-RapidAPI-Key": "856e827511msh721cd9717275d23p15a5b0jsn2763a200e040",
        "X-RapidAPI-Host": "tiktok-download-without-watermark.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = response.json()
    # rest = {'code': 0,
    #     'data': {'anchors': None,
    #             'anchors_extras': '',
    #             'author': {'avatar': 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/1971e99be0d67160f34f39fb1d66a0e5~c5_300x300.jpeg?x-expires=1695387600&x-signature=cFzeZhkOCQLHJX4DY9HON9ejFbU%3D',
    #                         'id': '107955',
    #                         'nickname': 'TikTok',
    #                         'unique_id': 'tiktok'},
    #             'aweme_id': 'v12044gd0000chf9eabc77u9q6ptbo60',
    #             'collect_count': 484,
    #             'comment_count': 796,
    #             'commerce_info': {'adv_promotable': False,
    #                                 'auction_ad_invited': False,
    #                                 'branded_content_type': 0,
    #                                 'with_comment_filter_words': False},
    #             'commercial_video_info': '',
    #             'cover': 'https://p16-sign.tiktokcdn-us.com/obj/tos-useast5-p-0068-tx/d07f8ac373a14ca38494f5801087f300_1683920692?x-expires=1695387600&x-signature=setLI4zhMwHuvmr8bCW%2BurLAL94%3D&s=AWEME_DETAIL&se=false&sh=&sc=dynamic_cover&l=202309211352105D541C3A63B4CF4E960E',
    #             'create_time': 1683920690,
    #             'digg_count': 10881,
    #             'download_count': 48,
    #             'duration': 9,
    #             'id': '7232384225691880746',
    #             'is_ad': False,
    #             'music': 'https://sf16-ies-music-va.tiktokcdn.com/obj/tos-useast2a-ve-2774/a2a2110b65d14a1fa5cdb990c278571e',
    #             'music_info': {'album': 'Speak Up',
    #                             'author': '',
    #                             'cover': 'https://p16-va-default.akamaized.net/img/tos-useast2a-v-2774/3cfbc126d3384e5797bdfc8ab51b1237~c5_720x720.jpeg',
    #                             'duration': 34,
    #                             'id': '7146691693914491694',
    #                             'original': False,
    #                             'play': 'https://sf16-ies-music-va.tiktokcdn.com/obj/tos-useast2a-ve-2774/a2a2110b65d14a1fa5cdb990c278571e',
    #                             'title': 'Speak Up'},
    #             'origin_cover': 'https://p16-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/4a234410949e48859b2967a134f7cb6e_1683920691~tplv-tiktokx-360p.jpeg?x-expires=1695387600&x-signature=7aTQxU%2F29mGcGfeF%2BWs71UzC0YY%3D&s=AWEME_DETAIL&se=false&sh=&sc=feed_cover&l=202309211352105D541C3A63B4CF4E960E',
    #             'play': 'https://v16m-default.akamaized.net/f027f31a97777934a56687578a38970d/650c9ef4/video/tos/maliva/tos-maliva-ve-0068c799-us/ocCQEBIYD8ARVXggoRMnSperpwlCcnkeLDsbBz/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=1760&bt=880&bti=OUBzOTg7QGo0NzZAL3AjLTAzYCM1NTNg&cs=0&ds=6&ft=iJOG.y7oZzv0PD1daShxg9wSbgMrBEeC~&mime_type=video_mp4&qs=0&rc=ODk3OWQ7OjZnM2g1OzM4OUBpM3J3OTw6ZmQ8azMzZzczNEBhMTEzMjQuXi0xLV5fLjZeYSMzX21ucjRfYmNgLS1kMS9zcw%3D%3D&l=202309211352105D541C3A63B4CF4E960E&btag=e00088000',
    #             'play_count': 614509,
    #             'region': 'US',
    #             'share_count': 214,
    #             'size': 1057015,
    #             'title': 'tag that person who can always read your mind',
    #             'wm_size': 1117329,
    #             'wmplay': 'https://v16m-default.akamaized.net/78746dd8760268588c2ed0d3337b8ecf/650c9ef4/video/tos/maliva/tos-maliva-ve-0068c799-us/oEaQEI7YD8ARSXggoRenSperpwLCcnk9xDsbBn/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=1860&bt=930&bti=OUBzOTg7QGo0NzZAL3AjLTAzYCM1NTNg&cs=0&ds=3&ft=iJOG.y7oZzv0PD1daShxg9wSbgMrBEeC~&mime_type=video_mp4&qs=0&rc=NGY2OWU7ZGdkNjo2ZDY6OUBpM3J3OTw6ZmQ8azMzZzczNEA1LzBeX2AyXl4xYDI1MzItYSMzX21ucjRfYmNgLS1kMS9zcw%3D%3D&l=202309211352105D541C3A63B4CF4E960E&btag=e00088000'},
    #     'msg': 'success',
    #     'processed_time': 0.1642}
    # return rest['data']['cover'] bunda fayl ko'rinishida kelyapti
    video = rest['data']['play']
    audio = rest['data']['music_info']['play']
    return video, audio

    # print(rest)
# tiktokloader('https://www.tiktok.com/@tiktok/video/7232384225691880746')


