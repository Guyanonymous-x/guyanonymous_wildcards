"""Country / region data for the world-proportional person generator.  Populations are rough 2024 totals in millions (UN-style best estimates);
the adult share (18+) is applied per region.  Edit freely.  rows: demonym (as used in countries_ethnic_prompts_*): (millions, region, age profile)"""
REGIONS = {  # code: (label, adult share of population, body-weight factor for heavy/very heavy)
 'EA': ('East Asia', .84, .6), 'SA': ('South Asia', .69, .6), 'SEA': ('Southeast Asia', .72, .55), 'CA': ('Central Asia and the Caucasus', .68, 1.1),
 'ME': ('the Middle East', .68, 1.5), 'NAF': ('North Africa', .66, 1.3), 'WAF': ('West Africa', .52, .65), 'EAF': ('East Africa and the Horn', .52, .65),
 'CSAF': ('Central and Southern Africa', .53, .7), 'WEU': ('Western, Northern and Southern Europe', .83, 1.1), 'EEU': ('Eastern Europe, Russia and the Balkans', .83, 1.2),
 'NAM': ('North America', .79, 1.9), 'LAC': ('Latin America and the Caribbean', .74, 1.4), 'OCE': ('Oceania and the Pacific', .75, 1.8)}
# age-profile adult band weights: 18-24, 25-34, 35-44, 45-54, 55-64, 65-74, 75-84, 85-94, 95-120
AGEP = {'young': [26, 31, 19, 11, 7, 4, 1.7, .3, .02], 'youngmid': [18, 26, 21, 15, 10, 6.5, 3, .5, .03], 'mid': [12.5, 20, 20, 17, 14, 10, 5, 1.4, .1], 'old': [8, 14, 16, 17, 16, 15, 10, 3.6, .3]}
BANDS = ['18_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75_84', '85_94', '95_120']
FEMALE_SHARE = {'18_24': .49, '25_34': .495, '35_44': .5, '45_54': .505, '55_64': .52, '65_74': .55, '75_84': .58, '85_94': .65, '95_120': .72}
RAW = """Chinese:1410:EA:mid Japanese:124:EA:old South Korean:52:EA:old North Korean:26:EA:mid Mongolian:3.4:EA:youngmid
Indian:1430:SA:youngmid Pakistani:240:SA:young Bangladeshi:173:SA:youngmid Nepali:31:SA:youngmid Sri Lankan:22:SA:mid Bhutanese:.78:SA:youngmid Maldivian:.52:SA:youngmid Afghan:42:SA:young
Indonesian:278:SEA:mid Filipino:117:SEA:youngmid Vietnamese:100:SEA:mid Thai:72:SEA:old Burmese:54:SEA:mid Malaysian:34:SEA:mid Cambodian:17:SEA:youngmid Lao:7.6:SEA:youngmid Singaporean:5.9:SEA:old Timorese:1.4:SEA:young Bruneian:.45:SEA:mid
Kazakhstani:20:CA:mid Uzbek:36:CA:youngmid Tajikistani:10:CA:young Kyrgyz:7:CA:youngmid Turkmen:6.5:CA:youngmid Azerbaijani:10.4:CA:mid Georgian:3.7:CA:old Armenian:3:CA:old
Iranian:90:ME:mid Turkish:86:ME:mid Iraqi:45:ME:young Saudi:37:ME:mid Yemeni:34:ME:young Syrian:23:ME:young Jordanian:11:ME:youngmid Israeli:9.8:ME:mid Lebanese:5.5:ME:mid Palestinian:5.5:ME:young Emirati:10:ME:mid Omani:4.6:ME:mid Kuwaiti:4.3:ME:mid Qatari:2.7:ME:mid Bahraini:1.5:ME:mid Cypriot:1.3:WEU:old
Egyptian:112:NAF:youngmid Sudanese:48:NAF:young Algerian:46:NAF:youngmid Moroccan:37:NAF:youngmid Tunisian:12:NAF:mid Libyan:7:NAF:youngmid Mauritanian:4.9:NAF:young
Nigerian:224:WAF:young Ghanaian:34:WAF:young Ivorian:29:WAF:young Nigerien:27:WAF:young Malian:23:WAF:young Burkinabè:23:WAF:young Senegalese:18:WAF:young Guinean:14:WAF:young Beninese:13.7:WAF:young Togolese:9:WAF:young Sierra Leonean:8.5:WAF:young Liberian:5.4:WAF:young Gambian:2.7:WAF:young Bissau-Guinean:2.1:WAF:young Cabo Verdean:.6:WAF:youngmid
Ethiopian:126:EAF:young Tanzanian:67:EAF:young Kenyan:55:EAF:young Ugandan:49:EAF:young Somali:18:EAF:young Rwandan:14:EAF:young Burundian:13:EAF:young Eritrean:3.7:EAF:young Djiboutian:1.1:EAF:young Malagasy:30:EAF:young Comorian:.85:EAF:young Mauritian:1.3:EAF:mid Seychellois:.1:EAF:mid South Sudanese:11:EAF:young
Congolese:108:CSAF:young South African:60:CSAF:youngmid Angolan:36:CSAF:young Mozambican:34:CSAF:young Cameroonian:28:CSAF:young Malawian:21:CSAF:young Zambian:21:CSAF:young Chadian:18:CSAF:young Zimbabwean:16:CSAF:young Central African:5.6:CSAF:young Namibian:2.6:CSAF:young Motswana:2.6:CSAF:young Gabonese:2.4:CSAF:young Mosotho:2.3:CSAF:young Equatorial Guinean:1.7:CSAF:young Swazi:1.2:CSAF:young São Toméan:.23:CSAF:young
German:84:WEU:old British:68:WEU:old French:65:WEU:old Italian:59:WEU:old Spanish:48:WEU:old Dutch:17.9:WEU:old Belgian:11.7:WEU:old Greek:10.4:WEU:old Portuguese:10.4:WEU:old Swedish:10.5:WEU:old Austrian:9.1:WEU:old Swiss:8.8:WEU:old Danish:5.9:WEU:old Finnish:5.6:WEU:old Norwegian:5.5:WEU:old Irish:5.3:WEU:old Luxembourger:.66:WEU:old Maltese:.54:WEU:old Icelandic:.38:WEU:old Andorran:.08:WEU:old Liechtensteiner:.04:WEU:old Monegasque:.04:WEU:old Sammarinese:.03:WEU:old Vatican:.0008:WEU:old
Russian:144:EEU:old Ukrainian:35:EEU:old Polish:38:EEU:old Romanian:19:EEU:old Czech:10.9:EEU:old Hungarian:9.6:EEU:old Belarusian:9.2:EEU:old Serbian:6.7:EEU:old Bulgarian:6.5:EEU:old Slovak:5.5:EEU:old Croatian:3.9:EEU:old Moldovan:3.4:EEU:old Bosnian:3.2:EEU:old Albanian:2.8:EEU:old Lithuanian:2.8:EEU:old Slovenian:2.1:EEU:old Latvian:1.9:EEU:old Macedonian:1.8:EEU:old Estonian:1.3:EEU:old Montenegrin:.62:EEU:old
American:340:NAM:mid Canadian:40:NAM:mid
Mexican:129:LAC:mid Brazilian:217:LAC:mid Colombian:52:LAC:mid Argentine:46:LAC:mid Peruvian:34:LAC:mid Venezuelan:28:LAC:mid Chilean:19.6:LAC:mid Guatemalan:18:LAC:youngmid Ecuadorian:18:LAC:mid Bolivian:12:LAC:youngmid Haitian:11.7:LAC:youngmid Cuban:11:LAC:mid Dominican:11.4:LAC:mid Honduran:10.5:LAC:youngmid Paraguayan:6.9:LAC:mid Nicaraguan:6.9:LAC:mid Salvadoran:6.3:LAC:mid Costa Rican:5.2:LAC:mid Panamanian:4.4:LAC:mid Uruguayan:3.4:LAC:mid Jamaican:2.8:LAC:mid Trinidadian:1.4:LAC:mid Guyanese:.8:LAC:mid Surinamese:.62:LAC:mid Belizean:.41:LAC:mid Bahamian:.41:LAC:mid Barbadian:.28:LAC:mid Saint Lucian:.18:LAC:mid Grenadian:.12:LAC:mid Vincentian:.1:LAC:mid Antiguan:.1:LAC:mid Kittitian:.05:LAC:mid
Australian:26:OCE:mid Papua New Guinean:10:OCE:young Fijian:.9:OCE:youngmid New Zealander:5.2:OCE:mid Solomon Islander:.74:OCE:young Ni-Vanuatu:.33:OCE:young Samoan:.22:OCE:youngmid I-Kiribati:.13:OCE:young Micronesian:.11:OCE:youngmid Tongan:.105:OCE:youngmid Marshallese:.04:OCE:young Palauan:.018:OCE:mid Nauruan:.012:OCE:young Tuvaluan:.011:OCE:young"""
def parse():
    rows = []
    import re
    for m in re.finditer(r'([A-Za-zÀ-ÿ\- ]+?):([\d.]+):([A-Z]+):(\w+)(?=\s|$)', RAW.replace('\n', ' ')):
        rows.append((m.group(1).strip(), float(m.group(2)), m.group(3), m.group(4)))
    return rows
