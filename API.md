#Wikipedia API

## 多语言
https://zh.m.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&meta=languageinfo&liprop=variantnames&licode=zh&prop=langlinks&lllimit=max&titles=%E6%98%9F%E9%99%85%E4%BA%89%E9%9C%B8II%EF%BC%9A%E8%99%9A%E7%A9%BA%E4%B9%8B%E9%81%97&llprop=url%7Cautonym%7Clangname&llinlanguagecode=zh

GET 参数：
```
action: query
format: json
formatversion: 2
meta: languageinfo
liprop: variantnames
licode: zh
prop: langlinks
lllimit: max
titles: 星际争霸II：虚空之遗
llprop: url|autonym|langname
llinlanguagecode: zh
```

返回：
```
{
  "batchcomplete": true,
  "query": {
    "pages": [
      {
        "pageid": 1621193,
        "ns": 0,
        "title": "星际争霸II：虚空之遗",
        "langlinks": [
          {
            "lang": "ar",
            "url": "https://ar.wikipedia.org/wiki/%D8%B3%D8%AA%D8%A7%D8%B1_%D9%83%D8%B1%D8%A7%D9%81%D8%AA_2:_%D9%84%D9%8A%D8%BA%D8%A7%D8%B3%D9%8A_%D8%A3%D9%88%D9%81_%D8%B0%D8%A7_%D9%81%D9%88%D9%8A%D8%AF",
            "langname": "阿拉伯语",
            "autonym": "العربية",
            "title": "ستار كرافت 2: ليغاسي أوف ذا فويد"
          },
          {
            "lang": "cs",
            "url": "https://cs.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "捷克语",
            "autonym": "čeština",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "en",
            "url": "https://en.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "英语",
            "autonym": "English",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "es",
            "url": "https://es.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "西班牙语",
            "autonym": "español",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "fa",
            "url": "https://fa.wikipedia.org/wiki/%D8%A7%D8%B3%D8%AA%D8%A7%D8%B1%DA%A9%D8%B1%D9%81%D8%AA_%DB%B2:_%D9%85%DB%8C%D8%B1%D8%A7%D8%AB_%D8%A8%D8%A7%D8%B7%D9%84",
            "langname": "波斯语",
            "autonym": "فارسی",
            "title": "استارکرفت ۲: میراث باطل"
          },
          {
            "lang": "fi",
            "url": "https://fi.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "芬兰语",
            "autonym": "suomi",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "fr",
            "url": "https://fr.wikipedia.org/wiki/StarCraft_2:_Legacy_of_the_Void",
            "langname": "法语",
            "autonym": "français",
            "title": "StarCraft 2: Legacy of the Void"
          },
          {
            "lang": "ko",
            "url": "https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%80%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8_II:_%EA%B3%B5%ED%97%88%EC%9D%98_%EC%9C%A0%EC%82%B0",
            "langname": "韩语",
            "autonym": "한국어",
            "title": "스타크래프트 II: 공허의 유산"
          },
          {
            "lang": "mn",
            "url": "https://mn.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "蒙古语",
            "autonym": "монгол",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "nl",
            "url": "https://nl.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "荷兰语",
            "autonym": "Nederlands",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "pl",
            "url": "https://pl.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "波兰语",
            "autonym": "polski",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "pt",
            "url": "https://pt.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "葡萄牙语",
            "autonym": "português",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "ro",
            "url": "https://ro.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "罗马尼亚语",
            "autonym": "română",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "ru",
            "url": "https://ru.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "俄语",
            "autonym": "русский",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "sv",
            "url": "https://sv.wikipedia.org/wiki/Starcraft_II:_Legacy_of_the_Void",
            "langname": "瑞典语",
            "autonym": "svenska",
            "title": "Starcraft II: Legacy of the Void"
          },
          {
            "lang": "uk",
            "url": "https://uk.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "乌克兰语",
            "autonym": "українська",
            "title": "StarCraft II: Legacy of the Void"
          },
          {
            "lang": "vi",
            "url": "https://vi.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void",
            "langname": "越南语",
            "autonym": "Tiếng Việt",
            "title": "StarCraft II: Legacy of the Void"
          }
        ]
      }
    ],
    "languageinfo": {
      "zh": {
        "variantnames": {
          "zh": "不转换",
          "zh-hans": "简体",
          "zh-hant": "繁體",
          "zh-cn": "大陆简体",
          "zh-hk": "香港繁體",
          "zh-mo": "澳門繁體",
          "zh-my": "大马简体",
          "zh-sg": "新加坡简体",
          "zh-tw": "臺灣正體"
        }
      }
    }
  },
  "limits": {
    "langlinks": 500
  }
}
```
