# Era descriptions for era-sensitive objects (user 2026-11-06). Keys are object builder names (ob_<key>_*). Periods: before_1800, 1800s, 1900_1945,
# 1946_1979, 1980_1999, 2000_present; an object lists only the periods in which it existed. Each line describes how the object looked in that period,
# with its period, form, material and colour, written from general knowledge of design history.
ERA = {
 'telephone': {
  '1800s': ['an 1890s wall-mounted wooden telephone box with a hand crank on the side, a separate earpiece on a cord and a mouthpiece on a short arm',
            'a late Victorian magneto telephone in polished walnut with nickel-plated bells on top and a side crank'],
  '1900_1945': ['a 1920s black candlestick telephone, an upright stem with a mouthpiece at the top and a separate earpiece hanging on a hook',
                'a 1930s black Bakelite desk telephone with a heavy rounded body, a cradle on top and a chrome-ringed rotary dial'],
  '1946_1979': ['a 1950s cream Bakelite rotary telephone with a coiled cloth-covered cord and a curved handset',
                'a 1970s slimline telephone in avocado green plastic with a rotary dial and a coiled cord',
                'a 1960s two-tone wall telephone in ivory plastic with a rotary dial and a long curly cord'],
  '1980_1999': ['a 1980s push-button telephone in beige plastic with square grey keys and a coiled cord',
                'a 1990s cordless telephone, a grey handset with a stubby aerial standing in its charging base'],
  '2000_present': ['a 2000s cordless DECT telephone in silver plastic with a small glowing screen, standing in its dock',
                   'a 2010s smartphone, a thin black glass slab with a large touchscreen and rounded corners'],
 },
 'kettle': {
  'before_1800': ['an eighteenth-century copper kettle with a domed lid, a curved spout and a swing handle, blackened from hanging over an open fire'],
  '1800s': ['a Victorian cast-iron kettle with a round squat body, a short spout and a heavy hinged handle',
            'a nineteenth-century copper and brass kettle with a riveted body and a turned wooden grip on the handle'],
  '1900_1945': ['a 1930s chrome-plated electric kettle with a rounded body, a black Bakelite handle and a cloth-covered flex',
                'an enamelled steel stovetop kettle in cream with a green rim and a whistle on the spout'],
  '1946_1979': ['a 1950s chrome electric kettle with a curved Bakelite handle and a separate plug-in cord',
                'a 1970s orange enamel stovetop kettle with a whistling spout and a wooden knob on the lid'],
  '1980_1999': ['a 1980s white plastic jug kettle with a water gauge window on the side and a coiled cord',
                'a 1990s cordless jug kettle in white plastic sitting on a round power base'],
  '2000_present': ['a 2000s brushed stainless steel cordless kettle with a blue-lit water window',
                   'a 2010s matt black dome kettle with a stainless steel spout, standing on its power base'],
 },
 'lamp': {
  'before_1800': ['an eighteenth-century brass oil lamp with a single wick, a round reservoir and a looped handle',
                  'a pewter candle lamp with a glass chimney on a turned base'],
  '1800s': ['a Victorian paraffin lamp with a tall glass chimney, an etched glass globe and a brass reservoir',
            'a nineteenth-century Argand lamp in brass with a frosted glass shade and a hanging prism fringe'],
  '1900_1945': ['an Art Deco table lamp with a chrome stem and a stepped frosted glass shade',
                'a 1920s brass desk lamp with a green glass shade over a single bulb',
                'an Arts and Crafts lamp with a mica shade on a hammered copper base'],
  '1946_1979': ['a 1950s tripod floor lamp with splayed wooden legs and a cone-shaped fabric shade',
                'a 1970s mushroom lamp in glossy orange plastic',
                'a 1960s spring-balanced desk lamp with an angled metal arm and a round metal shade'],
  '1980_1999': ['a 1980s halogen uplighter on a tall black metal stem with a wide flat bowl at the top',
                'a 1990s lava lamp with slow coloured wax blobs in a tapered glass body on a silver base'],
  '2000_present': ['a 2000s brushed steel arc floor lamp with a large dome shade',
                   'a 2010s slim LED desk lamp with a thin white folding arm and a flat light panel'],
 },
}

# Batches a-f hold the remaining era-sensitive objects; merge them here (base entries win on a clash).
import v109_era_data_a, v109_era_data_b, v109_era_data_c, v109_era_data_d, v109_era_data_e, v109_era_data_f, v109_era_data_g
for _m in (v109_era_data_a, v109_era_data_b, v109_era_data_c, v109_era_data_d, v109_era_data_e, v109_era_data_f, v109_era_data_g):
    for _k, _v in _m.ERA.items():
        ERA.setdefault(_k, _v)
