# Wikipedia API

## 多语言

### 中文
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

### 英文
https://en.m.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&meta=languageinfo&liprop=variantnames&licode=en&prop=langlinks&lllimit=max&titles=Domodedovo_(town)&llprop=url%7Cautonym%7Clangname&llinlanguagecode=en

GET 参数：
```
action: query
format: json
formatversion: 2
meta: languageinfo
liprop: variantnames
licode: en
prop: langlinks
lllimit: max
titles: Domodedovo_(town)
llprop: url|autonym|langname
llinlanguagecode: en
```

返回：
```
{
  "batchcomplete": true,
  "query": {
    "normalized": [
      {
        "fromencoded": false,
        "from": "Domodedovo_(town)",
        "to": "Domodedovo (town)"
      }
    ],
    "pages": [
      {
        "pageid": 6700516,
        "ns": 0,
        "title": "Domodedovo (town)",
        "langlinks": [
          {
            "lang": "ar",
            "url": "https://ar.wikipedia.org/wiki/%D8%AF%D9%88%D9%85%D9%88%D8%AF%D9%8A%D8%AF%D9%88%D9%81%D9%88",
            "langname": "Arabic",
            "autonym": "العربية",
            "title": "دوموديدوفو"
          },
          {
            "lang": "az",
            "url": "https://az.wikipedia.org/wiki/Domodedovo",
            "langname": "Azerbaijani",
            "autonym": "azərbaycanca",
            "title": "Domodedovo"
          },
          {
            "lang": "azb",
            "url": "https://azb.wikipedia.org/wiki/%D8%AF%D9%88%D9%85%D9%88%D8%AF%D8%AF%D9%88%D9%88%D9%88",
            "langname": "South Azerbaijani",
            "autonym": "تۆرکجه",
            "title": "دوموددووو"
          },
          {
            "lang": "ba",
            "url": "https://ba.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_(%D2%A1%D0%B0%D0%BB%D0%B0)",
            "langname": "Bashkir",
            "autonym": "башҡортса",
            "title": "Домодедово (ҡала)"
          },
          {
            "lang": "be",
            "url": "https://be.wikipedia.org/wiki/%D0%94%D0%B0%D0%BC%D0%B0%D0%B4%D0%B7%D0%B5%D0%B4%D0%B0%D0%B2%D0%B0",
            "langname": "Belarusian",
            "autonym": "беларуская",
            "title": "Дамадзедава"
          },
          {
            "lang": "bg",
            "url": "https://bg.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE",
            "langname": "Bulgarian",
            "autonym": "български",
            "title": "Домодедово"
          },
          {
            "lang": "ca",
            "url": "https://ca.wikipedia.org/wiki/Domod%C3%A9dovo",
            "langname": "Catalan",
            "autonym": "català",
            "title": "Domodédovo"
          },
          {
            "lang": "ce",
            "url": "https://ce.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_(%D0%B3%D3%80%D0%B0%D0%BB%D0%B0)",
            "langname": "Chechen",
            "autonym": "нохчийн",
            "title": "Домодедово (гӀала)"
          },
          {
            "lang": "ceb",
            "url": "https://ceb.wikipedia.org/wiki/Domodedovo",
            "langname": "Cebuano",
            "autonym": "Cebuano",
            "title": "Domodedovo"
          },
          {
            "lang": "crh",
            "url": "https://crh.wikipedia.org/wiki/Domodedovo_(%C5%9Feer)",
            "langname": "Crimean Tatar",
            "autonym": "qırımtatarca",
            "title": "Domodedovo (şeer)"
          },
          {
            "lang": "cs",
            "url": "https://cs.wikipedia.org/wiki/Domod%C4%9Bdovo",
            "langname": "Czech",
            "autonym": "čeština",
            "title": "Domodědovo"
          },
          {
            "lang": "da",
            "url": "https://da.wikipedia.org/wiki/Domodedovo",
            "langname": "Danish",
            "autonym": "dansk",
            "title": "Domodedovo"
          },
          {
            "lang": "de",
            "url": "https://de.wikipedia.org/wiki/Domodedowo",
            "langname": "German",
            "autonym": "Deutsch",
            "title": "Domodedowo"
          },
          {
            "lang": "eo",
            "url": "https://eo.wikipedia.org/wiki/Domodedovo_(Moskva_provinco)",
            "langname": "Esperanto",
            "autonym": "Esperanto",
            "title": "Domodedovo (Moskva provinco)"
          },
          {
            "lang": "et",
            "url": "https://et.wikipedia.org/wiki/Domodedovo",
            "langname": "Estonian",
            "autonym": "eesti",
            "title": "Domodedovo"
          },
          {
            "lang": "fa",
            "url": "https://fa.wikipedia.org/wiki/%D8%AF%D9%88%D9%85%D9%88%D8%AF%D8%AF%D9%88%D9%81%D9%88_(%D8%B4%D9%87%D8%B1)",
            "langname": "Persian",
            "autonym": "فارسی",
            "title": "دوموددوفو (شهر)"
          },
          {
            "lang": "fi",
            "url": "https://fi.wikipedia.org/wiki/Domodedovo_(kaupunki)",
            "langname": "Finnish",
            "autonym": "suomi",
            "title": "Domodedovo (kaupunki)"
          },
          {
            "lang": "fr",
            "url": "https://fr.wikipedia.org/wiki/Domodedovo_(ville)",
            "langname": "French",
            "autonym": "français",
            "title": "Domodedovo (ville)"
          },
          {
            "lang": "he",
            "url": "https://he.wikipedia.org/wiki/%D7%93%D7%95%D7%9E%D7%95%D7%93%D7%93%D7%95%D7%91%D7%95",
            "langname": "Hebrew",
            "autonym": "עברית",
            "title": "דומודדובו"
          },
          {
            "lang": "hsb",
            "url": "https://hsb.wikipedia.org/wiki/Domodedowo_(m%C4%9Bsto)",
            "langname": "Upper Sorbian",
            "autonym": "hornjoserbsce",
            "title": "Domodedowo (město)"
          },
          {
            "lang": "it",
            "url": "https://it.wikipedia.org/wiki/Domodedovo",
            "langname": "Italian",
            "autonym": "italiano",
            "title": "Domodedovo"
          },
          {
            "lang": "ja",
            "url": "https://ja.wikipedia.org/wiki/%E3%83%89%E3%83%A2%E3%82%B8%E3%82%A7%E3%83%89%E3%83%B4%E3%82%A9",
            "langname": "Japanese",
            "autonym": "日本語",
            "title": "ドモジェドヴォ"
          },
          {
            "lang": "ko",
            "url": "https://ko.wikipedia.org/wiki/%EB%8F%84%EB%AA%A8%EB%8D%B0%EB%8F%84%EB%B3%B4",
            "langname": "Korean",
            "autonym": "한국어",
            "title": "도모데도보"
          },
          {
            "lang": "lld",
            "url": "https://lld.wikipedia.org/wiki/Domodedovo_(zit%C3%A0)",
            "langname": "Ladin",
            "autonym": "Ladin",
            "title": "Domodedovo (zità)"
          },
          {
            "lang": "lt",
            "url": "https://lt.wikipedia.org/wiki/Domodedovas",
            "langname": "Lithuanian",
            "autonym": "lietuvių",
            "title": "Domodedovas"
          },
          {
            "lang": "lv",
            "url": "https://lv.wikipedia.org/wiki/Domodedova",
            "langname": "Latvian",
            "autonym": "latviešu",
            "title": "Domodedova"
          },
          {
            "lang": "mhr",
            "url": "https://mhr.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_(%D0%BE%D0%BB%D0%B0)",
            "langname": "Eastern Mari",
            "autonym": "олык марий",
            "title": "Домодедово (ола)"
          },
          {
            "lang": "nl",
            "url": "https://nl.wikipedia.org/wiki/Domodedovo",
            "langname": "Dutch",
            "autonym": "Nederlands",
            "title": "Domodedovo"
          },
          {
            "lang": "nn",
            "url": "https://nn.wikipedia.org/wiki/Domodedovo",
            "langname": "Norwegian Nynorsk",
            "autonym": "norsk nynorsk",
            "title": "Domodedovo"
          },
          {
            "lang": "nb",
            "url": "https://no.wikipedia.org/wiki/Domodedovo_(by)",
            "langname": "Norwegian Bokmål",
            "autonym": "norsk bokmål",
            "title": "Domodedovo (by)"
          },
          {
            "lang": "os",
            "url": "https://os.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_(%D1%81%D0%B0%D1%85%D0%B0%D1%80)",
            "langname": "Ossetic",
            "autonym": "ирон",
            "title": "Домодедово (сахар)"
          },
          {
            "lang": "pl",
            "url": "https://pl.wikipedia.org/wiki/Domodiedowo",
            "langname": "Polish",
            "autonym": "polski",
            "title": "Domodiedowo"
          },
          {
            "lang": "pnb",
            "url": "https://pnb.wikipedia.org/wiki/%D8%AF%D9%88%D9%85%D9%88%D8%AF%DB%8C%D8%AF%D9%88%D9%88",
            "langname": "Western Punjabi",
            "autonym": "پنجابی",
            "title": "دومودیدوو"
          },
          {
            "lang": "pt",
            "url": "https://pt.wikipedia.org/wiki/Domodedovo",
            "langname": "Portuguese",
            "autonym": "português",
            "title": "Domodedovo"
          },
          {
            "lang": "ro",
            "url": "https://ro.wikipedia.org/wiki/Domodedovo",
            "langname": "Romanian",
            "autonym": "română",
            "title": "Domodedovo"
          },
          {
            "lang": "ru",
            "url": "https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_(%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)",
            "langname": "Russian",
            "autonym": "русский",
            "title": "Домодедово (город)"
          },
          {
            "lang": "sah",
            "url": "https://sah.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE",
            "langname": "Sakha",
            "autonym": "саха тыла",
            "title": "Домодедово"
          },
          {
            "lang": "sco",
            "url": "https://sco.wikipedia.org/wiki/Domodedovo_(toun)",
            "langname": "Scots",
            "autonym": "Scots",
            "title": "Domodedovo (toun)"
          },
          {
            "lang": "simple",
            "url": "https://simple.wikipedia.org/wiki/Domodedovo_(town)",
            "langname": "Simple English",
            "autonym": "Simple English",
            "title": "Domodedovo (town)"
          },
          {
            "lang": "sr",
            "url": "https://sr.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE",
            "langname": "Serbian",
            "autonym": "српски / srpski",
            "title": "Домодедово"
          },
          {
            "lang": "sv",
            "url": "https://sv.wikipedia.org/wiki/Domodedovo",
            "langname": "Swedish",
            "autonym": "svenska",
            "title": "Domodedovo"
          },
          {
            "lang": "tl",
            "url": "https://tl.wikipedia.org/wiki/Domodedovo_(town)",
            "langname": "Tagalog",
            "autonym": "Tagalog",
            "title": "Domodedovo (town)"
          },
          {
            "lang": "tr",
            "url": "https://tr.wikipedia.org/wiki/Domodedovo_(%C5%9Fehir)",
            "langname": "Turkish",
            "autonym": "Türkçe",
            "title": "Domodedovo (şehir)"
          },
          {
            "lang": "tt",
            "url": "https://tt.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_(%D1%88%D3%99%D2%BB%D3%99%D1%80)",
            "langname": "Tatar",
            "autonym": "татарча / tatarça",
            "title": "Домодедово (шәһәр)"
          },
          {
            "lang": "uk",
            "url": "https://uk.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D1%94%D0%B4%D0%BE%D0%B2%D0%BE",
            "langname": "Ukrainian",
            "autonym": "українська",
            "title": "Домодєдово"
          },
          {
            "lang": "ur",
            "url": "https://ur.wikipedia.org/wiki/%D8%AF%D9%88%D9%85%D9%88%D8%AF%DB%8C%D8%AF%D9%88%D9%88_(%D9%82%D8%B5%D8%A8%DB%81)",
            "langname": "Urdu",
            "autonym": "اردو",
            "title": "دومودیدوو (قصبہ)"
          },
          {
            "lang": "vep",
            "url": "https://vep.wikipedia.org/wiki/Domodedovo_(lidn)",
            "langname": "Veps",
            "autonym": "vepsän kel’",
            "title": "Domodedovo (lidn)"
          },
          {
            "lang": "vi",
            "url": "https://vi.wikipedia.org/wiki/Domodedovo_(th%C3%A0nh_ph%E1%BB%91)",
            "langname": "Vietnamese",
            "autonym": "Tiếng Việt",
            "title": "Domodedovo (thành phố)"
          },
          {
            "lang": "war",
            "url": "https://war.wikipedia.org/wiki/Domodedovo_(bungto)",
            "langname": "Waray",
            "autonym": "Winaray",
            "title": "Domodedovo (bungto)"
          },
          {
            "lang": "xal",
            "url": "https://xal.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_%D0%B1%D0%B0%D0%BB%D2%BB%D1%81%D0%BD",
            "langname": "Kalmyk",
            "autonym": "хальмг",
            "title": "Домодедово балһсн"
          },
          {
            "lang": "zh",
            "url": "https://zh.wikipedia.org/wiki/%E5%A4%9A%E8%8E%AB%E5%82%91%E5%A4%9A%E6%B2%83",
            "langname": "Chinese",
            "autonym": "中文",
            "title": "多莫傑多沃"
          },
          {
            "lang": "zh-min-nan",
            "url": "https://zh-min-nan.wikipedia.org/wiki/Domodedovo_(si%C3%A2%E2%81%BF)",
            "langname": "Chinese (Min Nan)",
            "autonym": "Bân-lâm-gú",
            "title": "Domodedovo (siâⁿ)"
          }
        ]
      }
    ],
    "languageinfo": {
      "en": {
        "variantnames": {
          "en": "English"
        }
      }
    }
  },
  "limits": {
    "langlinks": 500
  }
}
```
