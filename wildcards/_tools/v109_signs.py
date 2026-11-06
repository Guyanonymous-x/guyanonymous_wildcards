"""v109: city signage with defined text. The 24 city_<type>_sign files (v65, made text-free by the v97 audit as "lit panel" wording) are
completed by "Signage is ..." in every city_<type>_prompt, which mentions signage without saying what it reads (text rule 3).
Each line now keeps its original sign type and gives the text in quotes, one line each with its position, from the matching
name-system generator (NAME_SYSTEM.txt). text_* files already carry their own quotes; name_* files do not, so they are quoted here."""
SIGN = {
 'city_airport_sign': [
  'large hanging direction signs with white arrows, the first line reading "Gate __name_number_small__" and the second line reading "Baggage Reclaim"',
  'a departures board, the top line reading "Departures" and the line beneath reading "__name_town__"'],
 'city_alley_sign': [
  'a hand-painted house number beside a door reading "__name_number_small__"',
  'a small painted shop sign over a doorway reading "__name_shop__"'],
 'city_arcade_sign': [
  'a shop name painted in gold on the glass reading "__name_shop__"',
  'a small projecting sign over a shop door reading "__name_record_store__"'],
 'city_bridge_sign': [
  'an iron name plate at the end of the bridge, the first line reading "__name_town__ Bridge" and the second line reading "__name_year__"',
  'a small direction sign on a post reading "__name_town__"'],
 'city_bus_stop_sign': [
  'a route sign on a pole, the first line reading "__name_number_small__" and the second line reading "__name_street__ __name_street_type__"',
  'a timetable in a frame headed "__name_town__ Buses"'],
 'city_campus_sign': [
  'a building name carved above a door reading "__name_surname__ Hall"',
  'a noticeboard with one large printed notice reading "Open Day"'],
 'city_canal_sign': [
  'a painted house number on a door reading "__name_number_small__"',
  'a small boat-hire sign on the towpath, the first line reading "Boat Hire" and the second line reading "__name_hours__"'],
 'city_construction_sign': [
  'a yellow hazard sign on the fence reading "Hard Hats Required"',
  'a hand-painted board on the fence, the first line reading "__name_company__" and the second line reading "Site Entrance"'],
 'city_festival_sign': [
  'hand-painted cloth pennants strung overhead with one long banner reading "__name_town__ Festival"',
  'a schedule board, the first line reading "Main Stage" and the second line reading "__name_band__"'],
 'city_food_street_sign': [
  'a bright hand-painted menu board, the first line reading "__name_restaurant__" and the second line reading __text_menu_item__',
  'a hanging red lantern sign over a stall reading "__name_restaurant__"'],
 'city_harbour_sign': [
  'a boat name painted on a hull reading "__name_ship__"',
  'a faded harbour office sign reading "Harbour Office"'],
 'city_library_sign': [
  'a small sign above one shelf reading "History"',
  'a desk plaque reading "Enquiries"'],
 'city_market_sign': [
  'a handwritten price board reading "__name_price__"',
  'a painted wooden stall sign reading "__name_grocery__"'],
 'city_metro_sign': [
  'the station name in large letters on the wall reading "__name_town__"',
  'a lit sign over a stairway reading "Platforms"',
  'arrows pointing to the exits with the words "Way Out"'],
 'city_museum_sign': [
  'a small card beside one display reading "__name_year__"',
  'a wall sign beside a doorway reading "Gallery __name_number_small__"'],
 'city_night_sign': [
  'a glowing neon sign reading "__name_bar__"',
  'a lit crossing sign reading "WAIT"'],
 'city_park_sign': [
  'a wooden board at the entrance reading "__name_surname__ Park"',
  'a small sign by the lake reading "Boats for Hire"'],
 'city_plaza_sign': [
  'a plaque on the plinth, the first line reading "__name_person__" and the second line reading "__name_year__"',
  'a small cafe sign reading "__name_cafe__"'],
 'city_residential_sign': [
  'house numbers on the doors, one reading "__name_number_small__"',
  'a faded corner shop sign reading "__name_grocery__"'],
 'city_rooftop_sign': [
  'a small painted sign by the door reading "__name_company__"'],
 'city_skyline_sign': [
  'one lit name at the top of the tallest tower reading "__name_brand_upper__"'],
 'city_stadium_sign': [
  'a gate number above an entrance reading "Gate __name_number_small__"',
  'a scoreboard, the first line reading "__name_town__" and the second line reading "__name_number_small__"'],
 'city_station_sign': [
  'a large clock face with a sign beneath it reading "__name_town__"',
  'a direction sign hanging from the roof reading "Platforms"',
  'a platform number plate reading "Platform __name_number_small__"'],
 'city_street_sign': [
  'a painted shop sign above a window reading "__name_shop__"',
  'a small hanging sign over a door reading "__name_cafe__"',
  'a street name plate on a corner reading __text_street__'],
}
def fix(G):
    for k, v in SIGN.items(): G[k] = list(v)
    return G
