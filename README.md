# guyanonymous_wildcards

A slightly extensive wildcard system for generating text prompts for txt2img generation, written in plain sentences for natural-language models such as Krea 2 and Moss Image.

**Current version: v122**

**Contents:** [Introduction](#introduction) · [What's New in v122](#whats-new-in-v122) · [What's New in v121](#whats-new-in-v121) · [What's New in v120](#whats-new-in-v120) · [What's New in v119](#whats-new-in-v119) · [What's New in v118](#whats-new-in-v118) · [What's New in v117](#whats-new-in-v117) · [What's New in v116](#whats-new-in-v116) · [What's New in v115](#whats-new-in-v115) · [What's New in v114](#whats-new-in-v114) · [What's New in v113](#whats-new-in-v113) · [What's New in v112](#whats-new-in-v112) · [Features](#features) · [Getting Started](#getting-started) · [Using the Features](#using-the-features) · [Full Changelog](#full-changelog)

## Introduction

Guyanonymous' Wildcards is a library of about 122,000 wildcard text files (122009 `.txt` files in [`wildcards/`](wildcards/) at v122). Each file holds one option per line. When a prompt says `__name__`, your image tool replaces it with a random line from `name.txt`. Many files refer to other files, so one reference can build a whole description: a person, an outfit, a room, an animal, a vehicle, a street sign, a book cover and so on.

The library is for people who make images with text-to-image tools and want varied, detailed prompts that still make sense. Lines are full descriptive sentences, not tag lists. There are no emphasis weights, LoRA tags or negative prompts. That is why it suits natural-language models such as Krea 2 and MOSS-Image. The docs also cover tag-style and token-limited models (see [Model-specific guidance](#model-specific-guidance)).

People files describe adults aged 18 to 120. The one exception is the awkward family photo lists (`afp_*`), where children can appear in family groups, always clothed; those lists are self-contained, so nothing else in the library can reach them and they cannot reach anything else. Some families are adult-themed: clinical anatomy descriptions, adult accessories, chastity devices and a "bad taste" set. These sit in their own files and the default person templates do not call them, so you only get them if you reference them yourself. Real brand names appear only in the `maker_*` files. All other names (authors, shops, brands, teams, people) are invented.

Each release gets a `release/vNN` branch (v74 is the first version tracked in git; each release also updates this README). Release zips and the "All Options Once" export are built from this tree and are not stored here.

## What's New in v122

The comprehensive fix of v121: every Cokin filter and other makers' filters, real concept and test vehicles, more civic and industrial places, all 99 gangs of The Warriors, detailed descriptions of 179 religious figures, and longer lists throughout.

- Lens filters (`lensf_`): all 172 Cokin filters on the guide (v121 had 74), plus 77 filters and lens tricks of other makers and kinds, each with its product name and effect-only, short, medium and long; all added to the photography styles.
- Real concept and test vehicles (`rveh_`): 80 real cars, bikes, aircraft, flying cars, record cars, trains, boats and submarines, from the Dymaxion car to the Avrocar, each named and look-only, short, medium and long.
- Civic and industrial places: 16 more kinds (`firestn_`, `policestn_`, `prisonyd_`, `airport_`, `railyard_`, `busdepot_`, `cemetery_`, `brewery_`, `mill_`, `warehouse_`, `printwks_`, `sawmill_`, `brickwks_`, `glasswks_`, `datactr_`, `observ_`), 27 in all.
- Gangs of The Warriors (`wgang_`): all 99 gangs of the film, the novel and the wider world, each named and look-only, short, medium and long.
- Religious figures (`reldesc_`): 179 gods, saints, prophets and sacred beings in short, medium and long detail with their own art styles; the old relig_ templates now use them (old lines kept).
- Longer lists: more vehicle kinds, looks, materials and details in all 20 genres, 46 more weapon kinds and 14 more weapon genres, more camera subjects, windows, masks and glasses, and richer long descriptions for 30 franchise species.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 24 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v122 entry points is in `wildcards/v122_entry_points.txt`.

## What's New in v121

Franchise species in named, generic and look-only versions, camera views through things, lens filters, civic and industrial places, genre and concept vehicles, and home-made and genre weapons.

- Franchise species (`fspecies_`, `peoples_named_`): 100 peoples of films, TV, games and books, each in three versions (with its real name, with a generic name, and look-only), each short, medium and long. The v112 named lists are now public too.
- Camera views (`camv_`): looking out from the back of a mouth, between fingers, through peepholes, keyholes, door cracks, under doors and beds, windows from outside with their coverings, bars, fences, chain link, masks, welder's masks and sunglasses, and more; one adult view in its own list (`camv_vagina_prompt`).
- Lens filters (`lensf_`): the Cokin range by name and code, plus effect-only versions and extra lens tricks, each short, medium and long; added to the photography styles.
- Civic and industrial places (`lawcourt_`, `townhall_`, `postal_`, `waterworks_`, `powerst_`, `steelw_`, `factoryw_`, `dockyard_`, `minework_`, `refinery_`, `wasteyard_`): low budget to grand, run-down to top of the line, with the people who work there.
- Genre and concept vehicles (`gveh_`, `cveh_`): 20 genres from western and spy to homemade play, surreal and biopunk, each from crude to masterpiece, practical to absurd, plus a mix maker and 28 test and concept vehicles.
- Home-made and genre weapons (`hweap_`, `gweap_`): pretend play props to expert home workshop pieces, and 14 genres from steampunk to samurai; looks only.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 20 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v121 entry points is in `wildcards/v121_entry_points.txt`.

## What's New in v120

Detailed peoples, gods and cryptids, a random god maker, animals and the people who work with them, circus and stage shows from around the world, and vehicle special effects.

- Peoples redone (`pdesc_`): 102 legendary, historical, ancestral and scriptural peoples, each with short, medium and long detailed descriptions, so pictures hold even when a model has never heard the name. The old `peoples_` templates now use them; the old lines are kept.
- Gods (`sacred_`, `newgod_`): the 18 sacred figures redone in short, medium and long, and a random new-god maker.
- Cryptids (`cryptid_`): all 62 cryptids of the Wikipedia list, each in short, medium and long, shown as trail-camera shots, eyewitness photos, field illustrations and more.
- Animals (`barn_`, `dogpark_`, `catcafe_`, `petshop_`, `vet_`, `rodeo_`, `stable_`, `shelter_`, `wrescue_`, `falconry_`, `beekeep_`): animals and the people who work with them.
- Shows (`circus_`, `iceshow_`, `acircus_`, `opera_`, `stageplay_`, `orch_`, `band_`, `soloplay_`, `wstage_`): circus to opera, orchestras to solo players, and stage traditions from around the world.
- Vehicle effects (`vfx_`): speed, movement, force fields and beams for underwater, water, land, air and space vehicles.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 27 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v120 entry points is in `wildcards/v120_entry_points.txt`.

## What's New in v119

Beauty, world adornment and body jewelry, crafts and small shops, Rube Goldberg machines and practical jokes.

- Beauty (`makeup_`, `wig_`, `fragr_`, `nailart_`): makeup artists, wigs and hairpieces, perfume and fragrance, and nail art, from market stalls to celebrity studios.
- Adornment (`adorn_`, `bjewel_`): adornment from 24 traditions around the world, worn by people, and body jewelry worn on the face, ears and body, well beyond earrings.
- Crafts and small shops (`knit_`, `wood_`, `hatshop_`, `shoeshop_`, `optic_`, `fitting_`): needlecraft, woodworking, hatters, shoemakers, opticians, and bridal and suit fittings.
- Rube Goldberg machines (`rg_`): simple to complex chains where every step fits the next, shown whole, mid-run, close up or as diagrams, with their inventors.
- Practical jokes (`prank_`): traditional to crazy, simple to complex, set up, being set up, and sprung.
- Every new place list runs from low budget to extravagant, with a separate condition from run-down to top of the line.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 14 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v119 entry points is in `wildcards/v119_entry_points.txt`.

## What's New in v118

Food and drink: barbecues, desserts, chocolate and candy, cheese, dinner parties, waiters, bartenders, home cooking, kitchen mishaps, farmers' markets, and food from perfect to spoiled.

- Food places and people (`bbq_`, `dessert_`, `candy_`, `cheese_`, `dinner_`, `waiter_`, `bartend_`, `hcook_`, `mishap_`, `fmarket_`): barbecues and grilling, desserts and pastries, chocolate and candy making, cheese shops and dairies, dinner parties and potlucks, waiters and table service, bartenders and cocktails, home cooking, kitchen mishaps and farmers' markets, from street stalls to luxury.
- Food in every condition (`fstate_`): perfect, partly eaten, imperfect, failed, spoiled and dropped, from moldy bread to failed casseroles.
- Every new place list runs from low budget to extravagant, with a separate condition from run-down to top of the line.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 11 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v118 entry points is in `wildcards/v118_entry_points.txt`.

## What's New in v117

Couples on dates from the first to the fiftieth year, pairs of people, flea markets, laundromats, fast food, murals, plazas, rides, natural wonders, skateparks, rural landmarks, drug dealers, crime organizations, gangs, neighborhood patrols and advertising through the ages.

- Couples on dates (`date_`): first, second and third dates, a year, five, ten, twenty-five and fifty years together, each with fitting places and closeness, and whether one, the other or both are enjoying it or attracted. Pairs of people (`pair_`): friends, rivals, twins, partners and more.
- Places (`flea_`, `laundry_`, `ffood_`, `mural_`, `plaza_`, `ride_`, `wonder_`, `skate_`, `rural_`): flea markets and auctions, laundromats and vending, fast food, murals and street art, fountains and plazas, amusement rides, waterfalls and natural wonders, skateparks and BMX, and rural landmarks, low budget to luxury.
- Crime (`dealer_`, `corg_`): drug dealers from lookouts up to kingpins, and crime organizations of the world as types and looks.
- Gangs and patrols (`gang_`, `patrol_`): original serious, costumed, era, silly and good-deed gangs with clothing, turf and poses, and neighborhood patrols old and new.
- Advertising through the ages (`adera_`): ad styles by decade back to the 1800s, then by century to ancient Rome, Egypt and China, with products of each period.
- Every new place list runs from low budget to extravagant, with a separate condition from run-down to top of the line.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 16 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v117 entry points is in `wildcards/v117_entry_points.txt`.

## What's New in v116

Mobility aids, sports fans, military life, bachelorette parties done right, picnics, camping, diving, mushrooms and foraging, insects close up, birds, police stations, jails and courtrooms.

- Mobility aids (`mobil_`): wheelchairs, prosthetic legs and arms, canes, walkers, crutches, scooters, white canes, guide dogs and hearing aids, old and new, each with everyday actions that fit it.
- Sports fans (`sfan_`): made-up teams in village squares, pubs, tailgates, terraces, stadiums and luxury boxes.
- Military life (`mil_`): field camps, barracks, mess halls and command centers, plus Roman, Viking, samurai, Napoleonic, First World War, 1940s, royal guard and future troops in their own camps.
- Bachelorette parties (`bach_`): the bride in a white or standout party look and her friends in matching outfits, on nights out, pool days, dinners and day trips. The adult strip lists now name the bride's party outfit and keep bachelorette parties for male strippers.
- Outdoors (`picnic_`, `camp_`, `dive_`, `forage_`): picnics from a road verge to a yacht deck, camping from a tarp to a glamping tent, diving from a jetty to a deep-sea habitat, and mushrooms and foraging.
- Nature (`insect_`, `bird_`): 30 insects and small creatures in macro, and 30 birds from around the world, plus birdwatchers.
- Law (`police_`, `jail_`, `court_`): police posts to forensic labs, dungeons to open prisons, village courts to supreme courts, with era officers in their own stations.
- Every new place list runs from low budget to extravagant, with a separate condition from run-down to top of the line.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 13 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v116 entry points is in `wildcards/v116_entry_points.txt`.

## What's New in v115

Tattoo parlors, salons and barbers, hospitals, street food and plating, arcades and casinos, stations and vehicle interiors, protests, natural disasters, skies, letters, fan conventions, movie theatres and a clothing fit scale.

- Shops (`tat_`, `salon_`): tattoo and piercing parlors and hair salons and barbers, from kitchen tables and street barbers to gallery studios and celebrity salons, with staff, clients and results.
- Hospitals (`hosp_`): rural clinics and field tents to private suites, from 1918 wards to future medical bays, with staff, patients and visitors.
- Food (`sfood_`): street food and markets around the world, from carts to gourmet food halls, and plating from paper boats to fine dining.
- Games (`arcade_`, `casino_`): arcades from seaside coin-pushers to VR arenas; gambling from back-room card dens to high-roller salons.
- Travel (`transit_`): stations from rural halts to spaceports, and the insides of vehicles from chicken buses to private jets.
- Events and weather (`protest_`, `disaster_`, `sky_`): protests from a handful of people to vast crowds; natural disasters and the rescue; skies and weather.
- Paper (`writ_`): letters, documents and handwriting props with wording in quotes.
- Fandom (`fancon_`, `cine_`): comic, sci-fi and cosplay conventions from library rooms to mega halls; movie theatres from bedsheet screens to luxury recliners.
- Clothing fit (`fit_scale_`): seven steps from painted on to drowning in it for seven kinds of garment, with woman's and man's versions; the older `fit_` lists are kept.
- Every new place list runs from low budget to extravagant, with a separate condition from run-down to top of the line.
- Fix: 22 old-age lines that read "Age has deeply marked his, ..." now read "his face" (and "her face").
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 18 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts at the three sizes.

The full list of v115 entry points is in `wildcards/v115_entry_points.txt`.

## What's New in v114

Street life, nightlife and theatres, pet costumes, postcards and greeting cards, drugs and implants, tomb raiders, crimes in action, pawn shops, cults and holy relics, revealing costumes, sleeping poses, world-wide homes, and fixes for ages, lairs and holiday scenes ([docs/INDEX_v114.txt](docs/INDEX_v114.txt)). Since v113:

- Street (`street_`): stunts and stunt performers, weird world records, groupies, buskers and street performers, people down on their luck shown with dignity (with cardboard sign text), and carnival games and sideshows.
- Nightlife (`night_`, `theatre_`): taverns, speakeasies, dance halls, nightclubs, raves and bars from the 1600s to now, inside and out; movie palaces, drive-ins, opera houses and playhouses.
- Cards and pets (`pet_`, `postcard_card_`, `greet_`): pet costumes and gear, postcards from made-up towns, and greeting cards for 23 occasions.
- Drugs and tech (`drug_`, `tech_`): drugs and medicines as props and places only, and implants and wearables.
- Crime and belief (`raid_`, `crim_action_`, `under_`, `pawn_`, `cult_`, `relic_`): tomb raiders, crimes in action, under-the-counter goods in 12 kinds of shop, pawn shops, cults with leaders, followers and crowds, and holy relics.
- Costumes and sleep (`reveal_`, `sleep_`): revealing Halloween costumes on purpose or by accident, and asleep and passed-out poses and faces.
- World homes (`global_`): homes in 15 regions inside and out, with wealth and condition; about half of random locations now come from them, and holiday decorations sit in homes where each holiday is kept.
- Fixes: ages 85 to 94 now about 7% and 95 to 120 about 3% of people, with milder old-age looks most of the time; lairs open inside with hideout cues and era-fit objects; holiday slogan tops are paired sensibly; menorahs are seven-branched, or nine-branched for Hanukkah.
- Adult lists stay in their own family (`adult_reveal_`, `adult_cfnm_`) and are left out of the normal samples and showcases.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 24 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts representing everything the library can do, at the three sizes (steps 50, cfg 3.75).

The full list of v114 entry points is in `wildcards/v114_entry_points.txt`.

## What's New in v113

Tropes from film, TV, books, comics and advertising: camera tricks and lighting, visual metaphors, character archetypes, 29 genre packs, story moments, trope settings, movie posters, TV, film and print ads, covers, comics, a trope mixer, and more poachers ([docs/INDEX_v113.txt](docs/INDEX_v113.txt)). Since v112:

- Camera and light tropes (`trope_shot_`, `trope_light_`): 115 framings from Dutch angles and god's-eye views to bullet time, split screens and sniper scopes, plus 52 lighting tropes in heroic, noir, horror, night, color-wash, stage and natural moods.
- Visual metaphors (`trope_meta_`): personal rainclouds, battle auras, dying candles and more for live action, and cartoon and manga effects such as anger veins, heart eyes and circling stars, grouped by feeling.
- Archetypes (`trope_char_`): about 110 stock characters in 11 groups, from the reluctant hero and the mad scientist to the drunken master and the fish out of water, in women's, men's and shared versions.
- Genres (`trope_genre_`): 29 genre packs (action, noir, kaiju, wuxia, western, cosmic horror, tokusatsu and more), each with its own look, props, wear, places and set-piece moments.
- Story moments (`trope_moment_`) and settings (`trope_place_`): frozen story beats for one person, two people and groups, and 80 trope settings from abandoned asylums to villain volcano lairs, each with fitting dressing.
- Media (`trope_poster_`, `trope_cover_`, `trope_ad_`, `trope_comic_`): movie posters by era, layout and condition; book, magazine, VHS and album covers; TV commercials, cinema and print ads for 30 product kinds; and comic panels, all with made-up titles, taglines, brands and slogans.
- Mixer (`trope_mix_`): combines an archetype or moment, a visual metaphor, a trope setting, a framing, a light and a genre look in one scene.
- Also new: 8 more kinds of poacher for the criminals (`crim_poacher_`), from Victorian pheasant poachers to shark-finning crews.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 12 new-area showcases of 20 prompts each at 1024, with ages spread evenly by decade; 100 sample prompts representing everything the library can do, at the three sizes (steps 50, cfg 3.75).
- Words on posters, covers, ads and comics come only from made-up text pools, in quotes.

The full list of v113 entry points is in `wildcards/v113_entry_points.txt`.

## What's New in v112

Film styles, Muybridge motion studies, 99 holiday characters and holiday wear and decorations, novelty holidays, 200 villain and hero lairs, costumes, mascots and fursuits, 199 religious figures and symbols, cabinets of curiosity, shrunken heads, hides and taxidermy, ray guns, criminals, lost and legendary peoples, zoos, pop-up books and blueprints ([docs/INDEX_v112.txt](docs/INDEX_v112.txt)). Since v111:

- Film (`film_`): film-making styles by genre and by genre per era; Muybridge-style motion studies (`muybridge_`) of people and animals, past, present and future.
- Holidays: 99 holiday characters from around the world (`hol_`), holiday clothing with sayings, decorations for 20 occasions (`hol_decor_`), and Festivus with 29 more novelty holidays (`novelty_`).
- Lairs (`loc_lair_`): 100 supervillain lairs and 100 superhero hideouts across every era, cost and size, each with rooms, objects, souvenirs, tech, weapons, traces and conditions.
- Costumes (`costume_`): 100 themes at six levels from screen-accurate to cheap bagged and flirty; mascot suits (`mascot_`) and fursuits (`fursuit_`) of 50 species and five styles.
- Religious figures (`relig_`): 199 gods, saints, prophets, demigods and sacred beings from 31 traditions, in short, medium and long forms and each tradition's own art styles, plus a symbol-only picture for every figure; figures whose faiths restrict images appear as symbols only.
- Curiosities: 109 cabinets of curiosity (`cab_`), shrunken heads (`shrunken_`), hides, furs, animal parts and the crafts made from them, illegal goods plain and seized (`animal_`), and bad and horror taxidermy (`taxi_`).
- Also new: sleepwalking (`sleepwalk_`), ray guns in layers across 14 eras and genres (`raygun_`), criminal wardrobes and tools for 30 types at every level and style (`crim_`), 221 lost, legendary, ancestral, fictional and future peoples (`peoples_`), zoos and menageries from cruel to excellent (`zoo_`), pop-up books (`popup_`), blueprints, diagrams and patent drawings (`blueprint_`), and special events (`event_`): weddings, funerals, adult birthday parties and anniversary parties, big to small, extravagant to cheap, classy to tacky, flawless to disastrous; performers (`perf_`): bands, solo singers, karaoke, vaudeville, circus and sideshow acts with their wardrobe, gear, stages, crowds and views; bookstores, newsstands and magazine shops around the world (`bookshop_`); wear modifiers (`wearmod_`) that add realistic stains, marks and dents to any garment or object.
- Fixes: mounted animals now say taxidermy, so they render as real specimens instead of plush toys.
- Showcase files: two prompts from each new area at 512, 1024 and 1408, plus a zip of 27 new-area showcases of 20 prompts each at 1024; 100 sample prompts representing everything the library can do, at the three sizes (steps 50, cfg 3.75). Showcases highlight what is new or changed in this version; samples represent everything the library can do.
- Adult lists stay in their own families (`cosnude_`, `irnude_`, `adult_`) and are left out of the normal samples and showcases.

The full list of v112 entry points is in `wildcards/v112_entry_points.txt`.

## What's New in v111

Things going wrong in 134 activities, bad snapshots that react, bigger awkward family photos, roller and inline skating by era, and dance: styles, steps, fads and how every generation dances ([docs/INDEX_v111.txt](docs/INDEX_v111.txt)). Since v110:

- Things going wrong (`mis_`): 20 mishaps for each of 134 activities (sports, music, crafts, hobbies, adventure and workouts) in three levels, small, mid and big, each with its own faces, bystanders and body positions; big ones add the aftermath. People are any adult age, injuries are everyday and non-gory, and eyes are on what is going wrong.
- Bad snapshots: people react to the moment and look at it (away from the lens), with 54 moments, 16 posed-photo mishaps, bystanders, places and outfits, plus framing mistakes (cut-off heads, animals blocking the view, a thumb over the lens) and bird droppings.
- Awkward family photos: many more eras, backdrops, outfit themes, adults, children (always clothed, in lists that reach nothing else), poses, oddities and mishaps that show the reaction.
- Wheels: skateboarding and surfing join the extreme sports; roller skating by era (1870s halls, 1920s clamp-on skates, 1950s rinks, 1970s roller disco, 2020s revival), roller derby, and inline skating (the late-1980s and 1990s boom, aggressive inline, today), each with era outfits, places and mishaps.
- Dance (`dance_`): 32 styles across solo, pairs and groups, from ballet, tap, flamenco and voguing to the waltz, Argentine tango, salsa and lindy hop, line dancing, ceilidh, disco, K-pop and Bollywood, plus pole fitness, twerking, the haka, the Sufi whirling sema, ancient-style hula, the lion dance and Bon Odori; every step line gives the body position, with holds, formations, outfits, music and places.
- Fad dances (`dance_fad_`): 25 from the Charleston and the Twist to the Floss, each with its signature move; crowd dancing (`dance_crowd_`): how people dance to 23 kinds of music by decade, from 1950s jiving and punk pogoing to raves and festival bass drops; and dance-floor mishaps.
- Showcase files: 16 prompts (two from each new area) at 512, 1024 and 1408, plus a zip of 8 new-area showcases of 20 prompts each at 1024; 100 sample prompts representing everything the library can do, at the three sizes (steps 50, cfg 3.75).

The full list of v111 entry points is in `wildcards/v111_entry_points.txt`.

## What's New in v110

3,755 location lines rewritten, heat shimmer, awkward family photos, bad snapshots, taxidermy, mounted heads, trophies, breakdancing, infrared and UV styles, ways of seeing people, glasses prescriptions, zombies, vampires, werewolves, fae, fairies and maps ([docs/INDEX_v110.txt](docs/INDEX_v110.txt)). Since v109:

- Locations: 3,755 weak place lines rewritten and checked inside their prompt sentences (writer's notes removed, fragments made into full descriptions, 'no X' lines turned into what is there, palettes given colours, signs and labels given quoted wording from 84 new `loc_text_*` lists); 169 regional lines rewritten as short regional versions.
- Heat shimmer: the desert line now fits its scenes, and six new hot things (road, airport tarmac, barbecue, car bonnet, jet exhaust, bonfire) each come in a real and a spectacle version.
- Awkward family photos (`afp_`): era studio styles, matching outfits, backdrops, poses, odd props and mid-pose mishaps. These lists are self-contained; children appear only here, always clothed, and the build checks that they cannot reach any other file.
- Bad snapshots (`snap_`): adults caught at the worst moment, natural or mid-pose, and a separate adults-only exposure list (`snap_exposure_prompt`).
- Objects: bad taxidermy (`ob_taxidermy_`), mounted heads on walls (`ob_mounted_head_`, humans only as joke props) and trophies of every kind (`ob_trophy_`), with photo prompts; all in the object roll-ups.
- Breakdancing joins the extreme sports (`adv_breakdance_`) with moves, crews, places and action cameras.
- Infrared and UV photo styles (`irstyle_`): 8 filters, each through its processing (straight from camera, red/blue swapped, black and white, unbalanced), with what glows and what goes dark.
- Ways of seeing people (`seeing_`): auras, X-rays, heat maps, night vision, lidar and more; glasses prescriptions (`acc_glasses_rx`) from eyes shrunk by strong minus lenses to owlish strong plus, bifocals and varifocals.
- Zombies, vampires, werewolves, the fae and fairies (`myth_`): 12 looks each across genres and cultures, in 9 treatments (ultra-realistic to children's animation style) and 17 eras.
- Maps (`map_`): 38 map types, 13 projections, 12 styles from ancient to treasure maps, with mediums, conditions, details, titles and views.
- Rule check: fewer false reports (sign-up and sign-out, label printers, 'a Uruguayan'); landscape prompts read 'A landscape of desert dunes'.
- Showcase files (34 prompts, two from each new area) and 100 sample prompts at 512, 1024 and 1408 pixel counts (steps 50, cfg 3.75), plus a zip of 17 new-area showcases of 20 prompts each at 1024.

The full list of v110 entry points is in `wildcards/v110_entry_points.txt`. From v110 the build tools are kept out of this repository.

## What's New in v109

Locations, objects, era looks, fixtures, trading cards, card and board games, activities and medical scenes ([docs/INDEX_v109.txt](docs/INDEX_v109.txt), notes in [wildcards/_tools/V109_CHANGES.md](wildcards/_tools/V109_CHANGES.md)). Since v108:

- **Locations:** the 350 Locations inventory becomes 1,422 places in 20 groups (`loc_<group>_<place>_*`) with scene, people, time, era and regional prompts (`loc_scene`, `loc_people`, `loc_era_scene`). Real brands are replaced by descriptions of their look, child-related places are never sexual, and measurements are left out.
- **Objects:** every object kind named in the inventory has its own wildcards (`ob_<object>_type/_material/_wear/_detail/_full/_text`), with quoted text where text belongs; city signs quote names from the name system.
- **Era objects and fixtures:** 230 objects have period looks from before 1800 to today (`ob_<object>_era_<period>`), and 79 architectural fixtures are added (doors, windows, staircases, lifts, roofs and more).
- **Trading cards (`tc_`):** sports, film, artist, creature, wildlife, vehicle and more in seven decade styles, five grades of visible condition, graded cases, packs and boxes, albums, sleeves and displays. Team names and numbers on shirts are quoted (`name_team`, `name_jersey_number`).
- **Card and board games (`cg_`, `bg_`):** 20 kinds of special-deck card game and 36 board and tabletop games, unbranded and described by look and rules, with boxes, parts, every text area on a card quoted, stages from set-up to finished, and top-down views.
- **Activities (`adv_`):** 71 adventure, extreme, solo outdoor and workout activities with outfits, equipment, poses and freely mixed places.
- **Medical scenes (`med_`):** clinical, nonsexual examinations, treatments and surgery for the health locations, in seven decades.
- **Library fixes:** body builds follow the person's age, "no visible signs of aging" is rewritten positively, and numbers and names on sportswear and uniforms are quoted.
- **Showcase and sample files:** the 40 showcase prompts (1024 and 1408 sizes plus a key file) highlight what is new in this version; the 100 sample prompts are representative of everything the library can do. Both are in [docs/showcase/](docs/showcase/), built by `_tools/v109_showcase.py`.

The full list of v109 entry points is in `wildcards/v109_entry_points.txt` and `wildcards/v109_loc_entry_points.txt`.

## What's New in v108

Review fixes, level-6 endings for same-sex scenes, place-friendly activity photo styles and a navel file ([docs/INDEX_v108.txt](docs/INDEX_v108.txt), notes in [wildcards/_tools/V108_CHANGES.md](wildcards/_tools/V108_CHANGES.md)). Since v107:

- **Level 6, two men and two women:** every `adult_l6_panel_mm*` and `adult_l6_panel_ww*` line now ends with a level-6 ending that fits the pose, so level 6 is no longer the same as level 5.
- **Level 1:** the bent-forward-at-a-table pose moves out of `adult_l1_panel_wm`; it stays at level 2 and above.
- **Wet places:** level 1 and level 3 location scenes at a shower, steam room, sauna, plunge pool, hot tub or lake dock now put people in swimwear.
- **Panels and groups:** wording about body parts the pose hides is removed, 69 positions are tidied, an impossible floor position is replaced, three-person nude sentences match who is in the scene, and group scenes read "This scene shows three adults. They are ...".
- **Fluid wording:** "not white" is replaced with "clear and transparent".
- **Activities:** every `act_*_scene_prompt` sentence starts with a capital ("The scene includes ..."), and `act_*_frame_prompt` now draws its photo style from the new `act_frame_style` (six on-location styles), so no studio backdrop appears in a dojo or on a beach.
- **Body features:** `f_body_nipples` and `head_chin` wording fixes, and a new `body_navel` (10 navel shapes).
- **Showcase and sample files:** 40 showcase prompts at 1024 and 1408 sizes plus a key file, and 100 sample prompts, in [docs/showcase/](docs/showcase/), built by `_tools/v108_showcase.py`.

The full list of v108 entry points is in `wildcards/v108_entry_points.txt`.

## What's New in v107

A fuller range for body features and three activities ([docs/INDEX_v107.txt](docs/INDEX_v107.txt), notes in [wildcards/_tools/V107_CHANGES.md](wildcards/_tools/V107_CHANGES.md)). Since v106 it adds:

- **Areola and nipple sizes:** `f_body_nipples` gains 35 lines that pair five areola sizes, from about the width of a thumbnail to about seven centimetres across, with seven nipple forms (tiny flat, small, medium, long, thick, inverted, puffy). No skin colour is named.
- **Anal area:** new `f_body_anus` and `m_body_anus` describe the shape, folds and hair, and the buttocks around it. No skin colour is named.
- **Yoga, dance classes and martial arts:** the action lists grow from 3 lines to 24, 20 and 20, and the clothes, equipment and setting lists are wider (leotards, leggings, fitted tops, training suits).
- **Showcase and sample files:** 40 showcase prompts at 1024 and 1408 sizes plus a key file, and 100 sample prompts, in [docs/showcase/](docs/showcase/), built by `_tools/v107_showcase.py`.

The full list of v107 entry points is in `wildcards/v107_entry_points.txt`.

## What's New in v106

Clothed bulges by fabric, structured group, wrestling and location scenes, and a chin fix ([docs/INDEX_v106.txt](docs/INDEX_v106.txt), notes in [wildcards/_tools/V106_CHANGES.md](wildcards/_tools/V106_CHANGES.md)). Since v105 it adds:

- Clothed men: `male_bulge_tight`, `_brief`, `_jock`, `_medium`, `_loose`, `_clothed` and `_covered`, written from image tests. Tight stretch fabric holds the penis flat against the belly, briefs outline it, a jockstrap has a modest close pouch, medium fabric softens the outline and loose fabric only tents over an erect penis.
- Level panels `adult_lN_panel_wm/_ww/_mm` rewritten with full geometry: who faces whom, torsos turned toward each other, a three-quarter camera, placed hands, and both people stated as men or women where needed.
- Structured three-person scenes at levels 1 to 6 (`adult_lN_group`), with explicit acts at levels 5 and 6.
- New `adult_l4_wrestling_mm`, `adult_l5_wrestling_mm` and `adult_l6_wrestling_mm`.
- Ten structured venues for a woman and a man at every level (`adult_lN_location`).
- Level 3 solo scenes use topless or shirtless in real bottoms; hand-on-stomach lines for women at levels 1 and 2 now use hand on hip or inner thigh.
- Chin: `head_chin` no longer has a deep cleft, which drew a split chin. A cleft is now a small shallow dimple low on the chin tip.
- **Showcase and sample files:** the showcase files (40 prompts at 1024 and 1408 sizes, plus a key file) highlight what is new or changed in this version, while the 100 sample prompts are representative of everything the model can do. Both are in [docs/showcase/](docs/showcase/), built by `_tools/v106_showcase.py`.
- Tools: `_tools/V106_showcase_generator.py` and `_tools/convert_list.py` build the body-feature grids (2x2 or 2x3, one person per feature, close-ups of the part, one title per image). Those grid files are not stored in this repository.

The full list of v106 entry points is in `wildcards/v106_entry_points.txt`.

## What's New in v105

Level panels for every cast, typed acts, kink and named positions ([docs/INDEX_v105.txt](docs/INDEX_v105.txt), research notes in [docs/RESEARCH_v105.txt](docs/RESEARCH_v105.txt)). Since v104 it adds:

- Level panels: `adult_lN_panel_wm`, `_ww`, `_mm` for levels 1 to 6, each introducing every person once and tying every body part to its owner.
- Typed acts at levels 5 and 6: vaginal, oral, anal, scissoring, strap-on, fingering and mutual masturbation, each described by what the bodies do.
- Named positions from the Wikipedia list written as physical placement: `adult_l5_position_*` and `adult_l6_position_*`.
- Kink panels: `kink_panel_wm/ww/mm/f/m` covering bondage, collars, impact play, chastity, strap-on, latex and leather.
- Clothed bulges at levels 2 and 3: the fabric stays unbroken and defines the raised shape, and level 3 covers are varied wraps.
- Semen is smaller and realistic: no spray or arcs; it falls or runs short distances.
- **Showcase and sample files:** the showcase files (40 prompts at 1024 and 1408 sizes, plus a key file) highlight what is new or changed in this version, while the 100 sample prompts are representative of everything the model can do. Both are in [docs/showcase/](docs/showcase/), built by `_tools/v105_showcase.py`.

The full list of v105 entry points is in `wildcards/v105_entry_points.txt`.

## What's New in v104

Penis stages and modifiers, physical fluid wording, masturbation by level and beauty and grooming objects ([docs/INDEX_v104.txt](docs/INDEX_v104.txt), research notes in [docs/RESEARCH_v104.txt](docs/RESEARCH_v104.txt)). Since v103 it adds:

- Penis stages: semi-erect and just-after-ejaculation forms, plus a separate circumcision modifier with physical foreskin wording and independent length, girth, shape, curve and lean pools.
- Ejaculation modifier (look, amount, after) and squirting described physically with single-stream and spray forms; structured scenes that keep every body part tied to its owner.
- Pubic hair stubble, patchy and shaved shapes; masturbation pools for levels 1 to 6.
- New Beauty and Grooming section: female and male hygiene, grooming, beauty and unisex care objects, about 575 descriptions.
- **Showcase and sample files:** the showcase files (40 prompts at 1024 and 1408 sizes, plus a key file) highlight what is new or changed in this version, while the 100 sample prompts are representative of everything the model can do. Both are in [docs/showcase/](docs/showcase/), built by `_tools/v104_showcase.py`.

The full list of v104 entry points is in `wildcards/v104_entry_points.txt`.

## Features

- **Large drop-in library.** One flat folder of 32,712 `.txt` files using the common `__name__` wildcard syntax. You need no Python to use it.
- **Women and men in one folder.** `f_` files are female, `m_` files are male and unprefixed files are shared. `any_` files are gender-neutral (they/their). At v74 there are 1,466 `f_`, 1,457 `m_` and 1,246 `any_` files.
- **Character creation system (v42).** `f_create_random_woman`, `m_create_random_man`, `any_create_random_person` and fixed identities (trans, intersex, non-binary, androgynous, in transition). It has three age modes (realistic, mismatched, unlinked), clothing states (none, `_w_clothes`, `_nude`, `_topless`, `_bottomless`), `_short` versions and an optional `_traits` suffix.
- **Conditioned layers.** In the master prompts the age bracket is chosen first. Body type, hair type, clothing, accessories, mobility aids, settings and poses then follow from it:
  - age layer: 9 brackets, 18–24 to 95–120
  - body-type layer: 8 archetypes plus severely obese
  - hair-type layer: straight, wavy, curly, coily
  - age and body conditioned clothing
  - frequency-weighted eye, hair and skin files
  - the men's set: facial hair, baldness that rises with age, grooming
- **Prompt templates.** These are nested master prompts (`f_/m_prompt_master_by_age`, `_random_clothing`, `_short`) and ready-made entry points for people, groups, outfits, places, animals, objects and food.
- **Subject families.** Each has its own entry points:
  - groups and relationships
  - occasions
  - shoes
  - accessories and wardrobe
  - adult-only accessories
  - poses, settings and interactions
  - furniture and household objects
  - containers and liquids
  - rooms
  - food and tableware
  - animals (by class, behaviour and farm animals)
  - plants and landscapes
  - architecture (`arch_`, `bld_`)
  - vehicles (`veh_`, `vx_`, interiors, paint and damage)
  - 104 manufacturer styles
  - 120 jobs
  - hobbies, music and sport
  - 30 world regions of dress and culture
  - 24 city types
  - 31 fantasy, sci-fi and history worlds
  - visual effects and extreme weather
  - art media, product shots and packaging
  - condition and damage
  - expressions in three intensity tiers
  - depth and occlusion
  - reading matter, signage and ads
  - creatures and powers
  - paper and print collections
- **Framing pack (v57).** `frame_*` files wrap any subject in a clarity opener, a square 1:1 frame and a composition that keeps the subject whole.
- **Model profiles.** Usage notes for natural-language, tag-style and token-limited models, plus test notes for MOSS-Image.
- **Python tools (optional).** `wildcards/_tools/` holds builders that regenerate the weighted layers, a test expander, a reference checker, consistency and contradiction checkers, the All Options Once builder and a browser-based prompt viewer. They need Python 3.8+ and no extra packages.
- **Release editions.** Each release is built as flat and folder editions (the folder edition uses `__family/name__`). Each also comes as an "All Options Once" (not proportional) edition, where every option appears once. The zips are not stored in this repository.

## Getting Started

### Requirements

- **An image tool that supports `__name__` wildcards.** The docs say only "your image tool" or "your front end". They do not name one specific extension. Put the folder wherever your tool reads wildcard files. The library uses only plain `__name__` references. In the current library no file uses `{a|b}` inline choices, `N::` weight prefixes or tool-specific syntax, and `_tools/check_build.py` treats pipes outside `{a|b}` and `(word:1.5)` weights as errors. Your tool reads only `.txt` files, so it ignores `_tools/`.
- **A text-to-image model.** The library targets natural-language models (Krea 2, MOSS-Image and similar). The project's MOSS-Image tests ([docs/MOSS_IMAGE_NOTES.txt](docs/MOSS_IMAGE_NOTES.txt)) were run in Forge, and the notes say MOSS-Image also runs in ComfyUI 0.42.0+.
- **Python 3.8 or newer: optional.** You need it only to rebuild generated files or run the checkers ([docs/HOW_TO_RUN.txt](docs/HOW_TO_RUN.txt)). On Windows, tick "Add python.exe to PATH" when you install it.

### Install

1. Get the files. Either clone this repository (`git clone https://github.com/Guyanonymous-x/guyanonymous_wildcards`) or download it as a ZIP from GitHub. `main` always holds the latest version. Each release also has a `release/vNN` branch (for example `release/v74`), so older git-tracked versions can be recovered.
2. Copy the contents of `wildcards/` into your image tool's wildcards folder. If you are upgrading from a release before the men's set, replace your old female files: they were renamed with an `f_` prefix. [docs/RENAME_MAP_old_to_new.csv](docs/RENAME_MAP_old_to_new.csv) lists every old to new name.
3. Leave `docs/` wherever is convenient. It is reference material only.

### Your first prompt

From [docs/QUICK_START_v55.txt](docs/QUICK_START_v55.txt):

1. Write `__file_name__` in a prompt. The tool replaces it with one random line from that file.
2. Start with a ready-made prompt file:

   | Subject | Try |
   |---|---|
   | A person | `__any_person_age35_44_w_clothes__` (bands 18_24, 25_34 … 95_120) or `__f_prompt_master_by_age__` / `__m_prompt_master_by_age__` |
   | A group | `__group_prompt__` |
   | An outfit | `__occasion_wedding_guest_outfit_prompt__` |
   | A place | `__setting_prompt__`, `__room_living_room_prompt_brief__`, `__city_prompt__`, `__land_prompt__` |
   | An animal | `__animal_prompt__`, `__animal_dogs_prompt__`, `__animal_aquatic_salt_prompt__` |
   | An object | `__obj_kitchen_prompt__`, `__tool_prompt__`, `__veh_prompt__`, `__arch_prompt__` |
   | Food | `__food_prompt__`, `__food_dish_prompt__`, `__table_setting_prompt__` |
   | New in v74 | `__reading_prompt__`, `__signage_prompt__`, `__cb_prompt__`, `__bld_prompt__` |

3. Build your own line from parts, for example:
   `__any_person_age45_54_w_clothes__ __pose_prompt__ __setting_prompt__ __food_drink_prompt__`
4. Add your own style or LoRA tags and negative prompt outside these files. The library never writes them.
5. If your tool reports a missing file, check the name against the index files. Names are lower case with underscores.

## Using the Features

### Wildcard syntax

- `__name__` is replaced by one random line from `name.txt`. Lines may contain further `__name__` references, so templates nest.
- The folder edition (shipped since v56) groups files into family folders: people, clothing, accessories, body, pose_camera_style, places, groups, objects, animals, nature_buildings_vehicles, food_tableware and other. References there are written `__family/name__`, for example `__animals/animal_dogs_prompt__`. Use the flat edition (this repository) if your tool does not support folder paths.
- Text meant to appear in the image is inside double quotation marks. `_fill` files hold quoted placeholders for you to replace.
- Since v73, file names no longer contain double underscores (`acc_x_display__material` became `acc_x_display_material`). A `__name__` parser could read the old names as two references.

### Folder layout and naming

```
wildcards/          the library: one .txt per wildcard (flat)
wildcards/_tools/   Python build and check tools, data, source templates (ignored by image tools)
docs/               per-version notes, indexes, layer READMEs, model notes, samples, showcase
```

Naming rules, from [docs/FILE_NAMING.txt](docs/FILE_NAMING.txt):

| Prefix | Meaning |
|---|---|
| `f_<name>` | female file (she/her) |
| `m_<name>` | male file (he/his) |
| `<name>` (no prefix) | shared: identical for both genders |
| `any_<name>` | neutral file (they/their, no gendered words) |

- Every layer is built twice, once for women and once for men. A file is kept once under its plain name only if both builds are byte-identical and it refers only to shared files. Otherwise it becomes `f_` and `m_` files, and each one's references point at its own gender. A gendered file therefore never silently serves the wrong gender.
- **Women-only:** makeup (`f_make_*`), `f_hair_baby`, female anatomy and `f_outfit_dress_style`.
- **Men-only:** `m_grooming` (replaces makeup), `m_facial_hair`, male anatomy and `m_outfit_suit_style`.
- **Common suffixes:**
  - `_prompt`: a whole assembled description
  - `_short` / `_brief`: compact versions
  - `_full`: long versions
  - `_phrase`: for use inside other sentences
  - `_random`: a per-type assembly
  - `_names`: lists of names
  - `_frame_prompt`: framed versions (see the framing pack)
  - `_fill`: editable placeholder text
- **Family prefixes:** these follow each version's notes, for example `furn_`, `room_`, `animal_`, `ani2_`, `vx_`, `maker_`, `job_`, `act_`, `culture_`, `city_`, `world_`, `fx_`, `wx_`, `cond_`, `frame_`, `book_`, `sign_`, `bld_`, `cb_` and `pw_`. See [docs/INDEX_v74.txt](docs/INDEX_v74.txt), [docs/INDEX_v66.txt](docs/INDEX_v66.txt) and [docs/INDEX_v55.txt](docs/INDEX_v55.txt).

### Prompt templates

[docs/README_prompt_templates.txt](docs/README_prompt_templates.txt) explains how the master prompts nest:

```
prompt_master            -> picks one of 3 section orders
  prompt_style           -> photo / documentary / (rarely) stylized medium
  prompt_char_physical   -> anchored (ethnic line supplies skin/hair/eye basics) or independent
    prompt_char_identity_*, prompt_char_face / _hair / _skin / _body / _details
  prompt_wardrobe        -> clothing pool + optional accessories
  prompt_pose_expression -> pose_* / facial expressions / poses
  prompt_setting         -> settings or env_*
  prompt_camera_light    -> cam_* + lite_*
```

**Person entry points** (swap `f_` for `m_`):

| File | What you get |
|---|---|
| `f_prompt_master_by_age` | Character and clothing conditioned on age and body. **Recommended.** |
| `f_prompt_master_by_age_random_clothing` | Conditioned character with completely random clothing |
| `f_prompt_master_random_clothing` | Nothing conditioned, random clothing |
| `f_prompt_master` | Nothing conditioned, realistic everyday clothing |
| `f_prompt_master_short` | About 120 words, for CLIP-limited models |

You can also use your own big templates: `f_WOMANprompt` / `f_character_female_basic` and `m_MANprompt` / `m_character_male_basic`. All LoRA tags were removed from these in v43.

**Character creation names** ([docs/README_v42_people.txt](docs/README_v42_people.txt)) are built as prefix + `create_random_` + who + mode + clothing + length + traits:

- **Mode:**
  - none: realistic, age drives the look
  - `_mismatched`: looks 10–30 years older or younger than the stated age
  - `_unlinked`: the age is independent of every other trait
- **Clothing:** none, `_w_clothes`, `_nude`, `_topless`, `_bottomless`.
- **Length:** full, or `_short` (about a quarter of the length).
- **Examples:** `f_create_random_woman_w_clothes`, `m_create_random_man_nude_short`, `any_create_random_person_unlinked`, `m_create_random_trans_man_w_clothes_traits`.
- `any_create_random_person` picks the identity at random. Cis men and women are weighted 3, every other identity 1.
- Ages are stated as number + age word + visible ageing features, because models tend to render older people too young.

**Other people entry points:**

- `any_person_age<band>_w_clothes` (+ `_short`) gives one age band.
- `group_<relationship>` and `group_prompt` (with `_any_ages`, `_same_decade` and `_multigenerational` variants) give groups. Relationships include couple, parent_child, three_generations, siblings, friends, colleagues, team, mentor_mentee, classmates and neighbours.
- The older group set is `grp_prompt_master`, `grp_prompt_master_2`, `grp_prompt_master_3` and `grp_2_mm` … `grp_3_mww`.
- Demographic prompts are `demo_prompt_master`, `demo_prompt_master_balanced` and `demo_<identity>_<orientation>`.

**Person, setting and pose are separate (v46).** Person files describe only the person and object files only the object. You combine them yourself. Examples:

- `__any_create_random_person_short__ __pose_sitting_w_seat__ __setting_prompt__`
- `__any_create_random_person_w_clothes__ __pose_prompt__ __room_gym_prompt_full__`

**Objects built from parts (v49–v50).** `<family>_prompt` assembles one description from components: material, colour, finish, features and condition. Every part is its own file and can be used alone. For example, `__furn_bed_built__` is a whole bed and `__furn_bed_headboard_prompt__` is just the headboard. To fix one detail, use that part file and leave the rest random.

**Entry point lists.** Most versions from v38 to v74 have a `vNN_entry_points` file in the library (for example `v47_entry_points` and `v74_entry_points`), and v49 has `v49_families`. [docs/MODEL_GUIDE_v66.txt](docs/MODEL_GUIDE_v66.txt) groups the main entry points by subject.

### Layers

Each layer has its own README in `docs/`. Those READMEs use the women's base names, so add `f_` (or `m_` for men) in the combined folder.

- **Age layer** ([docs/README_age_layer.txt](docs/README_age_layer.txt)):
  - The age bracket is picked first, weighted by population share.
  - Every age-linked attribute is then drawn from that bracket's own files, named `age<lo>_<hi>_<attribute>`: skin, face, eyes, lips, hair colour and texture, body, muscles, hands, pose, tattoo and eyewear.
  - Each option's weight is its base weight times an age kernel ("up", "down", "peak" or "flat").
  - The brackets are 18–24, 25–34, 35–44, 45–54, 55–64, 65–74, 75–84, 85–94 and 95–120.
- **Body layer** ([docs/README_body_layer.txt](docs/README_body_layer.txt)):
  - The age bracket picks a body archetype: thin, slim, avg, athl, curvy, heavy, musc or frail, plus vheavy for severely obese (added in v3).
  - Every body slot then comes from that archetype's files, `bt_<archetype>_<y|m|o>_<attribute>`.
  - This removed clashes such as "heavily overweight" with "chiseled abs".
- **Hair layer** ([docs/README_hair_layer.txt](docs/README_hair_layer.txt)):
  - Hair type (S straight, W wavy, C curly, K coily) is chosen once per prompt.
  - The type feeds both the ethnic identity line (`countries_ethnic_prompts_S/W/C/K`) and the hair paragraph (`hair_curl_<T>`, `hairtex_<T>`, `hairvol_<T>`, `hairstyle_<T>`, with age-bracket versions).
- **Clothing layer** ([docs/README_clothing_layer.txt](docs/README_clothing_layer.txt)):
  - `outfit_*` attribute lists, `outfit_cosplay` (630 costumes for women, 567 for men) and `age<lo>_<hi>_clothing_<archetype>`, which follows both age and body type.
  - `f_/m_clothing_random_mix` is completely random clothing.
  - The age and body conditioned files exclude near-nude options. `clothing_full` keeps them.
- **Men's set** ([docs/README_men.txt](docs/README_men.txt)):
  - The same pipeline as for women, with men's population shares.
  - Male build and height lists.
  - `m_facial_hair`, which follows age. Since v72 it uses plain physical descriptions, and prompts read "His lower face has …".
  - Male-pattern baldness that rises with age.
  - A separate male hairstyle grammar.
  - `m_grooming`.
  - 1,480 names in `m_names`.
  - Men's clothing lists and 2,500 outfit lines in `m_clothing_full`.
- **People system (v42) and bodies (v43)** ([docs/README_v42_people.txt](docs/README_v42_people.txt), [docs/README_v43_bodies.txt](docs/README_v43_bodies.txt)):
  - The `create_` prompts, described above.
  - Teeth by age and by dental-care access (`teeth_access_high/_mid/_low`).
  - Novelty tattoos (`tattoo_temporary`, `tattoo_henna`, `tattoo_bad`).
  - Optional clinical anatomy files. The `create_` prompts leave these out; you add them yourself, for example `__f_create_random_woman_nude__ __f_body_vulva__`. Files marked MANUAL ONLY are never called by another file.
- **Shoes** ([docs/SHOES.txt](docs/SHOES.txt)):
  - Six quality tiers, shoe classes, materials, construction and prices.
  - The footwear files now use the accessory naming `acc_shoe_*`, with tier names basic, practical, standard, fine, luxury and showpiece (renamed by `_tools/shoe_rename.py`).
  - Start from `acc_shoe_prompt_master` or `acc_shoe_prompt`.
- **Manufacturer styles** ([docs/MAKERS_v70.txt](docs/MAKERS_v70.txt)): 104 makers, each with decade, style, genre, prompt, scene and person files.

### Weighted files

- Likelihood is set by **repeating lines**, not by tool-specific weight syntax ([docs/README_pilot_weighted.txt](docs/README_pilot_weighted.txt)). For example, `eye_color` has 2,500 lines, and common colours appear many more times than rare ones. Every original option is kept at least once.
- Nested pointer files give weighted mixing. For example, a clothing pool can be 95% everyday outfits and 5% the full list.
- "None" options are not blank lines. Since v42 they are short positive sentences in the same proportion, and since v73 some are single-space lines. Tools that strip blank lines therefore keep the intended odds.
- The shares (age brackets, body types, hair types, facial hair, baldness, eyewear) are rough estimates, not cited data.
- The rebuild writes audit CSVs listing every option's weight to `_tools/audit/`. That folder is not committed to git.
- If you want every option equally likely, use the **All Options Once** edition, built by `_tools/simple_build.py`. Every distinct option appears once there, gendered and age-specific files are merged, and it has simple `aoo_prompt_*` templates.

### The `_tools` scripts

You do not need any tool to *use* the wildcards. Run them from the wildcards folder with Python 3.8+. They take no required arguments. On Windows use `py _tools\name.py`; on Mac or Linux use `python3 _tools/name.py`.

| Script | What it does |
|---|---|
| `build_all.py` | Rebuilds the generated layers for both genders and merges them. Each gender is built in its own workspace (`_tools/work/f`, `_tools/work/m`). Files identical for both stay shared and the rest become `f_`/`m_`. It ends with a reference check and takes about 1–2 minutes. **Back up first:** it rewrites every generated file. Options: `--list`, `--only age,body`, `--from hair`, `--gender m`, or a folder path. |
| `expand.py` | Test expander. `expand.py m_prompt_master_by_age` gives 3 samples. `expand.py f_prompt_master_by_age 5 42` gives 5 samples with seed 42. `expand.py --check` verifies that every `__reference__` resolves. |
| `check_build.py` | Standing pre-release check. It covers references, forbidden symbols (curly quotes, dashes, LoRA tags, weights, stray colons), blank lines, pronoun-led sentences, contradictions and a bare-name report. `--fail` sets the exit code. |
| `check_consistency.py` | Expands entry points many times and flags rule clashes, such as night with day wording, snow with summer or flightless birds flying. Usage: `check_consistency.py 200 7`, plus `--fail`. |
| `v51_check.py`, `v42_contra.py` | Contradiction and grammar samplers for entry points and for the `create_` prompts. |
| `check_vocab.py` | Option counts, forbidden characters and sample resolved prompts. |
| `simple_build.py` | Builds the All Options Once package. |
| `sample_prompts.py`, `v74_showcase.py` | Sample and showcase prompt generators. |
| `prompt_viewer.html` | Open it in a browser and click "Load wildcards folder". Type a start file name and press Generate. The prompt design appears in the left pane and sample output in the right. |
| `vNN_build.py` / `vNN_data.py` / `vNN_meta.py` | The build stages for each version's families (v40 to v74). |
| `v71_build.py`, `v72_*.py`, `v73_*.py` | Post-build passes that must be re-run after any rebuild, in order (see below). Each one takes `--restore` to undo. |
| `extern/` | Builders and expanders for the illustration and photostyle style packs. |

**What to edit for what** ([docs/HOW_TO_RUN.txt](docs/HOW_TO_RUN.txt)). Run the step in brackets afterwards.

| To change | Edit | Then run |
|---|---|---|
| Likelihood weights | `_tools/pilot_body.py` | `--only weights` |
| Women's clothing vocabulary | `_tools/data/outfit_vocab.json` | `--only outfits` |
| Men's clothing vocabulary | `_tools/male_outfits.py` | `--only outfits` |
| Cosplay | `cosplay_data_a/b/c.py` (women), `cosplay_data_m1/m2/m3.py` (men) | `--only outfits` |
| Conditioned clothing | `clothing_build.py` (women), `clothing_cat_m.py` (men) | `--only clothing` |
| Age curves, baldness and beard graying | `age_model.py` | `--from age` |
| Body types and shares | `body_model.py` | `--from body` |
| Hair types and hairstyles | `hair_model.py` | `--from hair` |
| Prompt wording | `_tools/data/src_templates/*.tpl` (women), `src_templates_m/*.tpl` (men) | `--from templates` |

**Run order after any rebuild** ([docs/README_v73.txt](docs/README_v73.txt)). All of these can be run more than once safely:

```
python _tools/v71_build.py ; python _tools/v72_facial_hair.py ; python _tools/v72_scars.py ;
python _tools/v73_cleanup.py ; python _tools/v73_consistency.py ; python _tools/v73_expressions.py ;
python _tools/v73_depth.py ; python _tools/v73_chastity_belt.py ; python _tools/v73_anchor2.py ;
python _tools/v73_rename_dunder.py ; python _tools/check_build.py
```

Maintainer's local working folder: `D:\!!!!!!!Dave's Apps - Wildcards\Guyanonymous' Wildcards`.

### Model-specific guidance

From [docs/MODEL_NOTES_v55.txt](docs/MODEL_NOTES_v55.txt), [docs/MODEL_PROFILES_v57.txt](docs/MODEL_PROFILES_v57.txt), [docs/MODEL_GUIDE_v66.txt](docs/MODEL_GUIDE_v66.txt) and [docs/MOSS_IMAGE_NOTES.txt](docs/MOSS_IMAGE_NOTES.txt):

- **Natural-language models (Krea 2, MOSS and similar):**
  - Use the full `_prompt` / `_full` files, or `frame_prompt` / `frame_<kind>_prompt` as they are.
  - Put the setting and light after the subject.
  - Keep one subject per line.
  - For groups, keep the "First person … Second person …" order.
- **Tag-style or short-prompt models:**
  - Use `_short` / `_brief` files, or join single part files with commas.
  - Add one line from `frame_person_full` or `frame_product`.
- **Token-limited models (about 75 tokens):**
  - Use `_short` files and `frame_person_prompt_short` / `frame_person_age<N>_prompt`.
  - Full person prompts can run over 1,000 characters.
- **Models that read the first words most strongly:** put the main subject first.
- **Framing:**
  - `frame_ratio` is square 1:1. Edit it for other ratios.
  - Full-body lines ask for head to toe with a margin on every side. If a model still crops, repeat the line or use a `_short` prompt.
  - `frame_animal_quad_prompt` and `frame_feature_grid_prompt` make four-panel images.
- **MOSS-Image test notes** (single seeds, not conclusive):
  - **Model:** a 5B diffusion transformer with a Qwen3.5-9B text encoder. It accepts prompts up to about 4,000 tokens.
  - **Settings:** CFG 3.0 is usually enough for long prompts. 50 steps showed no visible loss compared with 80. 1024×1024 and 1408×1408 (1.98M pixels) sit inside the recommended 2M.
  - **Wording:** use positive wording. Negations such as "no readable lettering" did not help, and words like "banner" invite lettering. Put text to render in quotation marks.
  - **Groups:** ordinal and position anchors bind outfits and actions to the right person, and an explicit count line held the people count. Skin tone can drift between scenes.
- **Known limits:** about 0.5% of random person prompts mix age words with build or hair words that do not fit. Re-roll those.
- **Krea 2:** the docs do not give model-specific settings, beyond listing it as a natural-language model.

## Full Changelog

Summarised from the notes in [docs/](docs/), newest first. Dates are shown only where the notes give one. All git commit dates (2026-11-04) are import dates, not release dates.

### v122
The comprehensive fix of v121: every Cokin filter and other makers' filters, real concept and test vehicles, more civic and industrial places, all 99 gangs of The Warriors, detailed descriptions of 179 religious figures, and longer lists throughout.

### v121
Franchise species in named, generic and look-only versions, camera views through things, lens filters, civic and industrial places, genre and concept vehicles, and home-made and genre weapons.

### v120
Detailed peoples, gods and cryptids, a random god maker, animals and the people who work with them, circus and stage shows from around the world, and vehicle special effects.

### v119
Beauty, world adornment and body jewelry, crafts and small shops, Rube Goldberg machines and practical jokes.

### v118
Food and drink: barbecues, desserts, chocolate and candy, cheese, dinner parties, waiters, bartenders, home cooking, kitchen mishaps, farmers' markets, and food from perfect to spoiled.

### v117
Couples on dates from the first to the fiftieth year, pairs of people, flea markets, laundromats, fast food, murals, plazas, rides, natural wonders, skateparks, rural landmarks, drug dealers, crime organizations, gangs, neighborhood patrols and advertising through the ages.

### v116
Mobility aids, sports fans, military life, bachelorette parties done right, picnics, camping, diving, mushrooms and foraging, insects close up, birds, police stations, jails and courtrooms.

### v115
Tattoo parlors, salons and barbers, hospitals, street food and plating, arcades and casinos, stations and vehicle interiors, protests, natural disasters, skies, letters, fan conventions, movie theatres and a clothing fit scale.

### v114
Street life, nightlife and theatres, pet costumes, postcards and greeting cards, drugs and implants, tomb raiders, crimes in action, pawn shops, cults and holy relics, revealing costumes, sleeping poses, world-wide homes, and fixes for ages, lairs and holiday scenes. See [What's New in v114](#whats-new-in-v114).

### v113
Tropes from film, TV, books, comics and advertising: camera tricks and lighting, visual metaphors, character archetypes, 29 genre packs, story moments, trope settings, movie posters, TV, film and print ads, covers, comics, a trope mixer, and more poachers. See [What's New in v113](#whats-new-in-v113).

### v112
Film styles, Muybridge motion studies, 99 holiday characters and holiday wear and decorations, novelty holidays, 200 villain and hero lairs, costumes, mascots and fursuits, 199 religious figures and symbols, cabinets of curiosity, shrunken heads, hides and taxidermy, ray guns, criminals, lost and legendary peoples, zoos, pop-up books and blueprints. See [What's New in v112](#whats-new-in-v112).

### v111
Things going wrong in 134 activities, bad snapshots that react, bigger awkward family photos, roller and inline skating by era, and dance: styles, steps, fads and how every generation dances. See [What's New in v111](#whats-new-in-v111).

### v110
3,755 location lines rewritten, heat shimmer, awkward family photos, bad snapshots, taxidermy, mounted heads, trophies, breakdancing, infrared and UV styles, ways of seeing people, glasses prescriptions, zombies, vampires, werewolves, fae, fairies and maps. See [What's New in v110](#whats-new-in-v110).

### v109
350-location conversion, object builders with era looks and fixtures, trading cards, card and board games, activities, medical scenes, quoted sportswear text. See [What's New in v109](#whats-new-in-v109).

### v108
Review fixes, level-6 endings for same-sex scenes, on-location activity photo styles, swimwear at wet places, navel file. See [What's New in v108](#whats-new-in-v108).

### v107
Areola and nipple size ladder, anal-area files for women and men, fuller yoga, dance-class and martial-arts lists. See [What's New in v107](#whats-new-in-v107).

### v106
Bulge classes by fabric, structured group, wrestling and location scenes, rewritten level panels, shallow chin dimple. See [What's New in v106](#whats-new-in-v106).

### v105
Full range of sexual acts at levels 5 and 6, kink panels, named positions, clothed bulges, realistic semen. See [What's New in v105](#whats-new-in-v105).

### v104
Penis stages (semi-erect and post-ejaculation), circumcision as a separate modifier, physical wording for ejaculation and squirting, masturbation by level, and a Beauty and Grooming object section. See [What's New in v105](#whats-new-in-v105).

### v103
v103: adult poses with people, places and light; age ladders and cleaner age pools; hand-condition and pubic-hair modifiers. See [What's New in v105](#whats-new-in-v105).

### v102
v102: commas inside object-first style text, randomised quiet motifs replace brand marks, extended marks. See [What's New in v105](#whats-new-in-v105).

### v101
v101: object-first brand styles, optional brand marks, object-neutral styles and samples of everything. See [What's New in v105](#whats-new-in-v105).

### v100
polish See [What's New in v105](#whats-new-in-v105).

### v99
brands of the past See [What's New in v105](#whats-new-in-v105).

### v98
unnamed brand cells, quoted badge text See [What's New in v105](#whats-new-in-v105).

### v97
library-wide text audit See [What's New in v105](#whats-new-in-v105).

### v96
positive text wording, no text denials See [What's New in v105](#whats-new-in-v105).

### v95
brand styles describe the object, no logos or brand names in prompts See [What's New in v105](#whats-new-in-v105).

### v94
fake name system, business cards, logos, caps and t-shirts See [What's New in v105](#whats-new-in-v105).

### v93
150 more image-checked brand styles, wider subjects, defined label text See [What's New in v105](#whats-new-in-v105).

### v92
object-only brand styles, 100 more brands See [What's New in v105](#whats-new-in-v105).

### v89
Vans, Converse, Land Rover product-neutral See [What's New in v105](#whats-new-in-v105).

### v88
25 more image-checked brand styles See [What's New in v105](#whats-new-in-v105).

### v87
male wrestling, brand fixes, deduplicated badges, lighting fit See [What's New in v105](#whats-new-in-v105).

### v86
pinback buttons, insignia, adult achievements, kilts, pony, torn clothing See [What's New in v105](#whats-new-in-v105).

### v85
v85: adult L6, modifiers, messy, wrestling, gear, kilts and tailoring, top brands image-checked See [What's New in v105](#whats-new-in-v105).

### v85
v85: adult L6, modifiers (scene-neutral), messy, wrestling, gear, kilts and tailoring, top brands image-checked See [What's New in v105](#whats-new-in-v105).

### v84
v84: adult levels and adult_ prefix, brand styles as design essence (style-only plus _named) See [What's New in v105](#whats-new-in-v105).

### v83
v83: 746 global brand styles across all eras and regions; richer illustration and photography style lists (59 files) See [What's New in v105](#whats-new-in-v105).

### v82
v82: art forms that are neither illustration nor photography: sculpture, craft, fibre and render/installation (96 forms, 1,158 files) See [What's New in v105](#whats-new-in-v105).

### v81
v81: robots (25 types), gadgets and tech devices (42 types) and maker reference files (801 new files) See [What's New in v105](#whats-new-in-v105).

### v80
v80: treasure, card, mineral, sound, screen, art and nature collections (571 new files) See [What's New in v105](#whats-new-in-v105).

### v79
Noir (`nr_`), pirate (`pt_`) and spy (`sy_`) genres, money (`mo_`) and metalware (`mt_`) collections, full descriptions for named e-reader and phone models, and screen text given in quotation marks. See [What's New in v105](#whats-new-in-v105).

### v78
Cyberpunk (`cy_`), steampunk (`sp_`) and western (`we_`) genres, steampunk phones (`spp_`) and home and decorative collections (`hd_`). See [What's New in v105](#whats-new-in-v105).

### v77
Fantasy (`fa_`), horror (`ho_`), people interacting (`pi_`), toys (`toy_`) and die-cast models (`dc_`). See [What's New in v105](#whats-new-in-v105).

### v76
Science fiction (`sf_`), e-reader and phone timelines, and eight timekeeping and instrument collections (`col_`). Showcase prompts and sample prompts in `docs/showcase/`. See [What's New in v76](#whats-new-in-v76).

### v75
Legendary creatures (`leg_`), sacred figure archetypes, the pilot conversion of 325 Location Inventory records (`loc_`) with tag indexes and anywhere pools, and 66 object builders (`ob_`). Showcase prompts and sample prompts for the release are in `docs/showcase/`. See [What's New in v76](#whats-new-in-v76).

### v74
"Foundation release": reading matter, signage and lettering engine, ads and labelled containers, vehicle interiors (`vint2_`), architecture upgrade (`bld_`), creature body-plan and hybrid builders, powers, paper and print collections, and `_fill` placeholder files. Also the showcase prompts and the first git-tracked version. See [What's New in v76](#whats-new-in-v76).

### v73 (2026-11-03)
- **Expression intensity tiers:** 68 emotions × mild, strong and extreme, each described physically. `facialExpressionsFor_v10` and `pose_emotion` were rebuilt, and `expr_mild` / `expr_strong` / `expr_extreme` were added.
- **Consistency pass:**
  - City time and weather are drawn as consistent pairs.
  - Penguins and flightless birds got their own groups and never fly.
  - Clothing condition prompts no longer carry their own wear state.
  - The new `check_consistency.py` went from 182 flags to 0–1 per run.
- **Depth and occlusion family:** `depth_*`, `depth_prompt`.
- **Anchoring phase 2:** 6,568 lines in 448 person piece files now start with "The woman's", "The man's" or "The person's".
- **Cleanup:** 272 double-underscore file names were renamed. Blank padding became single-space lines, curly quotes and dashes were removed, and a new `chastity_belt` group was added.
- **Tools:** `check_build.py` is the standing build check. `simple_build.py` now builds into a temporary folder and refuses to finish if the file count falls by more than 1%.

### v72 (applied 2026-11-03)
- **Facial hair:** all 303 lines in `m_facial_hair` and the age files were rewritten as plain descriptions of where hair grows and where skin is bare, after tests showed named beard styles are weak. Person templates now say "His/Their lower face has …".
- **Scars:** the parametric scar lines in `mark_scars` and `skin_scars` became physical descriptions with colour, relief and length.
- Released together with the v71 anchor pass.

### v71 (2026-11-03)
No separate notes file. The anchor pass is described in README_v72:
- furniture "It has…" chains were merged
- room openers use the room noun
- person templates became one chained sentence per person
- ageing summaries use "The man", "The woman" or "This person"

### v70
Manufacturer styles: 104 makers × decade, style, genre, prompt, scene and person files, plus the mixes `maker_style_any`, `maker_names` and `maker_decades`. Real brand names are used only in `maker_*`.

### v69
Vehicles:
- 157 genres (`vx_<genre>_*`)
- vehicle poses (`vs_*`)
- paint (`vpaint_*`)
- damage (`vdmg_*`, `vxd_*`)
- interiors (`vint_*`)
- entry points `vx_prompt` and `vxs_prompt`

### v68
Patch release with no new entry points:
- fixed condition part lists
- new `ani_sessile_*` family for jellyfish, corals and similar
- reworded `world_<name>_place_prompt`
- object condition prompts limited to hand and power tools

### v67
Visual and special effects in nine domains (`fx_*`), photographic effects (`fx_photo_*`) and extreme weather (`wx_*`) with sky, land, people, things, animals, plants and light parts.

### v66
Fantasy, sci-fi and history worlds: 31 worlds × dress, props, setting and action (`world_*`). Added [INDEX_v66.txt](docs/INDEX_v66.txt) and [MODEL_GUIDE_v66.txt](docs/MODEL_GUIDE_v66.txt).

### v65
Cities and public places: 24 city types × layout, surface, detail, activity and sign, plus shared style, time, weather and crowd files (`city_*`).

### v64
Hobbies, music and sport: per-activity clothes, equipment, setting and action (`act_*`).

### v63
Global dress and culture: 30 regions × garment, headwear, adornment, hair, setting, event and outfit (`culture_*`).

### v62
- **Art media:** `medium_*`.
- **Product shots and packaging:** `prod_*`, `pack_*`.
- **Signs:** `sign_*`.
- **Condition system:** `cond_<kind>_<family>_<strength>` for buildings, vehicles, furniture, clothing, objects, signs, books and statues, with `condition_*_prompt` entry points.

### v61
Animals 2:
- behaviour, group, young and detail pools for 18 families (`ani_*`, `ani2_*`)
- 14 farm animals (`farm_*`)
- `farm_person_prompt` and `pet_person_prompt`

### v60
Nature and landscapes: 28 landscape types in parts (`land_*`), flora by 8 biomes (`flora_*`), and shared season, time, sky and water files.

### v59
Professions and roles: 120 jobs × outfit, tool, workplace and action (`job_*`), grouped by sector.

### v58
- Outerwear and accessories built from parts: `wear_*`, 58 types across outerwear, hats, bags, scarves, gloves and belts.
- `frame_animal_quad_prompt` rewritten.

### v57
Framing and clarity pack: `frame_*` files and entry points, plus [MODEL_PROFILES_v57.txt](docs/MODEL_PROFILES_v57.txt).

### v56
- **Grammar pass:** a/an corrected in 4,093 lines across 712 files.
- **First folder edition:** 12 family folders, with references written `__family/name__`.

### v55
- **Food:** `food_*` for cheese, fruit, vegetable, bread, dessert, dish, drink and snack.
- **Tableware:** `ware_*`.
- **Table settings:** `table_*`, `meal_prompt`.
- **Docs:** added [INDEX_v55.txt](docs/INDEX_v55.txt), [QUICK_START_v55.txt](docs/QUICK_START_v55.txt) and [MODEL_NOTES_v55.txt](docs/MODEL_NOTES_v55.txt).

### v54
- **Animals:** 36 classes, insects, and salt and fresh water animals (`animal_*`).
- **Nature:** plants and `nature_prompt`.
- **Buildings:** 9 building types (`arch_*`).
- **Vehicles:** 12 vehicle types (`veh_*`, `machinery_prompt`).

### v53
- **Wardrobe by occasion:** 20 occasions × parts (`occasion_*`).
- **Bad-taste set:** clothing, tattoos and jewellery in ugly, tacky, crude and gross variants (`badtaste_*`).
- **New rule:** item descriptions no longer contain `: `.

### v52
- **Groups and relationships:** `group_<relationship>` with age-gap modes.
- **One age band per prompt:** `any_person_age<bracket>_w_clothes`.
- **Consistent settings:** `setting_exterior`, plus hot and cold variants. Everyone is 18 to 120.

### v51
- **Prompt-quality checker:** `v51_check.py`.
- **Build pass:** `v51_build.py` removes repeated words, fixes a/an and removes baldness/styled-hair clashes.
- **Tool assemblies:** `tool_<trade>_random` / `_phrase`.
- **Room wording fixes.**

### v50
Furniture and appliances built from parts (`furn_<item>_built`, `furn_<item>_<part>`), matching bed boards, shared part materials and group mix phrases.

### v49
Random assembly for every new object family: `<family>_prompt` / `_random` / `_phrase`, built from shared `comp_*` components, covering 89 families.

### v48
Rooms and locations: 35 room types (`room_<type>_prompt_brief` / `_full`), room modifiers and `gear_*` files. Rooms describe the space only.

### v47
Furniture, household and office objects, containers (bottles, closures, perfume) and liquids (`furn_*`, `home_*`, `bottle_*`, `liquid_*`).

### v46
Setting, pose and interaction were split into separate files:
- poses with and without supports
- seats, surfaces and lean supports
- two- and three-person interactions
- place/light/weather settings

### v45
Adult-only accessories, each described as an object only:
- chastity devices split by anatomy
- merkins and pasties
- adult toys

### v44
Accessories and wardrobe:
- eyewear and wraps
- wearable tech (retro to far future)
- pins and patches
- earrings
- plastic and novelty ranges
- costume teeth
- balls and sport equipment
- garment-fit files

### v43
- **LoRA tags removed** from all files.
- **Clinical anatomy files:** optional, never called by the `create_` prompts.
- **Teeth:** follow age and dental-care access.
- **Novelty tattoos:** temporary, henna and badly done.

### v42
- **Character creation system:** the `create_random_*` names, identities, age modes, clothing states and `_short`.
- **Weights to wording:** emphasis weights became plain wording.
- **Blank lines:** blank "none" lines became positive sentences.
- **Hair:** bald styles were separated from other hairstyles.
- **Checker:** a contradiction checker (`v42_contra.py`) cut the flag rate from 20–28% to about 3–7%.

### v4–v41
No release notes exist in `docs/`. (`_tools/NEXT_ROUND.txt` mentions some v38–v41 work items, and `_tools/` has build scripts from v40 and v41.)

### v3
From [README_v3_changes.txt](docs/README_v3_changes.txt):
- **Eyewear:** 5,000-line eyewear files with age-based shares.
- **Ages and bodies:** 9 age brackets and a "severely obese" body type.
- **Objects:** new `obj_*` objects; rubber ducks reduced.
- **Groups:** groups of 2 and 3 (`grp_*`).
- **Demographics:** demographic identity files (`demo_*`).
- **Shoes:** the shoe system (`shoe_*`, now `acc_shoe_*`).
- **Age and body conditioning:** accessories, aids, settings and poses now follow age and body type.
- **Wording fixes:** colour-neutral skin modifiers, and plain-word hair curls replacing the 1A–4C codes.
- **Viewer:** `prompt_viewer.html`.

### Undated foundation builds (before the numbered notes)
[CHANGELOG_cleanup.txt](docs/CHANGELOG_cleanup.txt) and the layer READMEs record the early builds:
- **Cleanup:** removed ages under 18, and removed child and gender nouns from the ethnic lines.
- **Weighting and templates:** the frequency-weighted pilot and the unified prompt templates.
- **Layers:** the age, body-type, hair and clothing layers.
- **Men's build:** added male files, with female files renamed `f_` and shared files kept plain (see [RENAME_MAP_old_to_new.csv](docs/RENAME_MAP_old_to_new.csv)).
- **Tools:** moved into `wildcards/_tools` with `build_all.py`.

## Credits

Guyanonymous' Wildcards by Guyanonymous. The repository includes no license file.
