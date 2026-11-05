"""v94 fake logos and printed/embroidered merchandise (caps, t-shirts, hoodies, bags, mugs) with defined text."""
import random
NOMORE = ' No other words or letters appear.'
SYMBOL = ['a circle containing two overlapping triangles that form a mountain peak', 'a simple sun made of a half circle with seven short straight rays', 'a crescent moon beside one small five-pointed star', 'a stylised wave made of three curved parallel lines', 'a hexagon with a smaller hexagon cut out of its centre', 'a flame shape made of one teardrop inside a larger teardrop', 'a pair of crossed wrenches', 'a shield outline with a single vertical stripe down the middle', 'a leaf with a single centre vein and two side veins', 'a tree drawn as a trunk with a round crown made of overlapping circles', 'a key with a round head and two teeth', 'a lighthouse seen from the front with a lit lamp and two stripes', 'a gear with eight teeth and a round hole in the centre', 'a diamond shape divided into four smaller diamonds', 'a lightning bolt inside a circle', 'a compass rose with four long points and four short points', 'an anchor with a rope looped around its shaft', 'a ship wheel with eight handles', 'a wheat ear with six pairs of grains', 'a cog and a leaf joined side by side', 'an open book seen from the front with a small star above it', 'a bridge with three arches over two wavy lines', 'a bell with a small round clapper', 'a crown with five points and a small circle on each point', 'a mountain range of three peaks with a sun between the two tallest', 'a paper plane folded from a triangle', 'a letter M built from two tall triangles', 'a letter K built from straight lines meeting at a point', 'a spiral made of one thick line turning four times', 'a lantern with a square frame and a flame in the centre', 'a thistle flower with a round head and two leaves', 'a fish skeleton drawn with a long spine and five pairs of ribs', 'a ring of twelve small dots around a larger solid dot', 'a barn outline with a tall peaked roof and a cross on the door', 'a pair of wings spread out either side of a small circle', 'a castle tower with three battlements and an arched door', 'a stack of three horizontal bars of different lengths', 'a hand-drawn star with an uneven outline', 'a plus sign inside a rounded square', 'a mushroom with a spotted dome cap', 'a cup of steaming coffee seen from the side', 'a pair of overlapping rings like a Venn diagram', 'a lotus flower with eight petals', 'a pine cone drawn as overlapping scales', 'a roof outline above a small square window', 'a kite shape with a long tail of three bows', 'a rose drawn as a spiral of petals', 'a windmill with four sails', 'a hammer and a feather crossed', 'a pyramid with an eye-shaped circle above it', 'a maple-like leaf with five rounded points', 'a snowflake with six arms and small branches', 'a rocket pointing upwards with two small fins', 'a cat-eye shaped ring with a dot at the centre', 'an arrowhead pointing up inside a circle', 'a bottle outline with a round label', 'a wheel with six spokes and a thick rim', 'a simple house made of a square and a triangle with a round door', 'an hourglass with sand in the lower half', 'a bird in flight drawn with five curved lines', 'a chevron stack of three upward-pointing arrows', 'a keyhole shape inside a circle', 'a spoon and a fork crossed over a round plate', 'a hexagonal nut with a round hole', 'an oak leaf with an acorn beside it', 'a trident with a short handle', 'an eight-pointed star made of two squares', 'a comet with a round head and a long curved tail', 'a thread needle drawn as a long thin loop', 'an arch of five bricks with a keystone', 'an open hand with the fingers spread', 'a mountain lake drawn as a triangle above two wavy lines']
LOGO_STYLE = ['drawn in one flat colour with clean thick lines', 'drawn as a bold solid silhouette', 'drawn in thin elegant lines of equal thickness', 'drawn inside a round badge with a double border', 'drawn inside a square badge with rounded corners', 'drawn in two flat colours with no outlines', 'drawn as a retro stamp with a slightly worn edge', 'drawn in a hand-painted brush style with slightly uneven edges', 'drawn in a geometric style using only circles and straight lines', 'drawn as a vintage engraving with fine hatching', 'drawn as a modern minimal mark with a lot of empty space around it', 'drawn as a collegiate crest with a banner beneath']
LOGO_COLOUR = ['in navy blue on white', 'in black on white', 'in white on black', 'in forest green on cream', 'in deep red on cream', 'in mustard yellow on dark brown', 'in burnt orange on white', 'in sky blue on navy', 'in white on deep green', 'in gold on black', 'in teal on white', 'in charcoal grey on pale grey', 'in white on burgundy', 'in cream on navy', 'in pink on dark purple', 'in black on yellow']
LOGO_LAYOUT = ['with the symbol above the wordmark', 'with the symbol to the left of the wordmark', 'with the wordmark curved around the top of the symbol', 'with the wordmark inside a banner beneath the symbol', 'with the wordmark in a straight line across the middle of the symbol', 'with the symbol alone', 'with the wordmark only in a stylised lettering and no symbol', 'with the wordmark in capital letters beneath the symbol and a small line of text "__name_established__" beneath that']
FONT = ['heavy blocky capital letters', 'thin elegant serif capital letters', 'rounded friendly lowercase letters', 'tall narrow capital letters', 'flowing script lettering', 'slab serif capital letters', 'clean geometric sans-serif letters', 'hand-lettered brush capitals', 'stencil-cut capital letters', 'condensed bold letters with a slight slant']
TEES = ['white', 'black', 'heather grey', 'navy blue', 'forest green', 'faded red', 'sand', 'washed-out blue', 'charcoal', 'mustard yellow', 'cream', 'burgundy']
CAPS = ['black', 'navy blue', 'white', 'khaki', 'red', 'forest green', 'grey', 'faded denim blue', 'cream', 'mustard yellow', 'burgundy', 'orange']
SLOGANS = ['Take it easy', 'Good things take time', 'Out of office', 'Stay curious', 'Keep it simple', 'Less talk more coffee', 'Run wild', 'Home sweet home', 'Be kind', 'Nothing to see here', 'Dream big', 'Low and slow', 'Sunday best', 'Weekend mode', 'Hello again', 'Better days ahead', 'Just add water', 'Made in the shade', 'The long way round', 'Good vibes only']
def build(final=None):
    G = {}
    G['name_logo_symbol'] = SYMBOL; G['name_logo_style'] = LOGO_STYLE; G['name_logo_colour'] = LOGO_COLOUR; G['name_logo_layout'] = LOGO_LAYOUT; G['name_logo_font'] = FONT
    G['name_tee_colour'] = TEES; G['name_cap_colour'] = CAPS
    G['name_merch_slogan'] = SLOGANS
    # a complete logo description with the wordmark defined
    G['name_logo_description'] = [
        'a design of __name_logo_symbol__, __name_logo_style__ __name_logo_colour__, __name_logo_layout__, with the wordmark "__name_brand_invented__" in __name_logo_font__',
        'a design of __name_logo_symbol__, __name_logo_style__ __name_logo_colour__, with the wordmark "__name_brand_upper__" in __name_logo_font__ beneath it',
        'a design of __name_logo_symbol__, __name_logo_style__ __name_logo_colour__, with the wordmark "__name_company__" in __name_logo_font__ to its right',
        'a wordmark design reading "__name_brand_invented__" in __name_logo_font__ __name_logo_colour__, with no symbol',
        'a design of __name_logo_symbol__ __name_logo_style__ __name_logo_colour__ as a purely pictorial mark']
    G['name_logo_prompt'] = [
        'A flat design sheet showing __name_logo_description__, centred on a plain background.' + NOMORE,
        'A large logo centred on a plain pale background, being __name_logo_description__.' + NOMORE,
        'A printed letterhead with __name_logo_description__ at the top and the rest of the page blank.' + NOMORE,
        'A shopfront sign carrying __name_logo_description__.' + NOMORE,
        'A rubber stamp pressed onto paper, showing __name_logo_description__.' + NOMORE,
        'A metal badge screwed to a wall, showing __name_logo_description__.' + NOMORE,
        'A brand board with __name_logo_description__ in the centre and two smaller versions beside it in different colours.' + NOMORE]
    # merchandise
    G['name_cap_prompt'] = [
        'A __name_cap_colour__ baseball cap seen from the front, with the words "__name_brand_invented__" embroidered in __name_logo_font__ on the front panel.' + NOMORE,
        'A __name_cap_colour__ baseball cap seen from the front, with __name_logo_description__ embroidered on the front panel.' + NOMORE,
        'A __name_cap_colour__ trucker cap with a mesh back, a foam front panel printed with the words "__name_shop__" in capital letters.' + NOMORE,
        'A __name_cap_colour__ baseball cap seen from the side, with the words "__name_brand_upper__" embroidered on the side panel and a plain front.' + NOMORE,
        'A __name_cap_colour__ baseball cap seen from behind, with the words "__name_town__" embroidered above the adjustable strap and a plain front.' + NOMORE,
        'A __name_cap_colour__ baseball cap with a flat brim, the front panel embroidered with the single letter "__name_hero_letter__" in __name_logo_font__.' + NOMORE,
        'A __name_cap_colour__ baseball cap with a small patch on the front showing __name_logo_symbol__ and no words or letters.',
        'A row of three baseball caps on a shelf, each with the words "__name_brand_invented__" on the front in a different colour of thread.' + NOMORE,
        'A __name_cap_colour__ baseball cap with a curved brim, the front panel printed with "__name_merch_slogan__" in capital letters.' + NOMORE,
        'A __name_cap_colour__ wool cap with a folded cuff, a woven label sewn on the cuff reading "__name_brand_invented__".' + NOMORE]
    G['name_tshirt_prompt'] = [
        'A __name_tee_colour__ t-shirt laid flat, with the words "__name_brand_invented__" printed across the chest in __name_logo_font__.' + NOMORE,
        'A __name_tee_colour__ t-shirt laid flat, with __name_logo_description__ printed in the centre of the chest.' + NOMORE,
        'A __name_tee_colour__ t-shirt laid flat, with a small logo on the left chest showing __name_logo_symbol__ and no words, and the words "__name_brand_invented__" printed small across the upper back.' + NOMORE,
        'A __name_tee_colour__ t-shirt laid flat, with the slogan "__name_merch_slogan__" in __name_logo_font__ across the chest.' + NOMORE,
        'A __name_tee_colour__ t-shirt seen from behind, with the words "__name_band__" in large letters across the shoulders and "__name_town__" beneath them.' + NOMORE,
        'A __name_tee_colour__ t-shirt laid flat, with a tour design: the words "__name_band__" on the first line, "__name_town__" on the second line, and a list of three places on the lines beneath reading "__name_town__", "__name_town__" and "__name_town__".' + NOMORE,
        'A __name_tee_colour__ work shirt with a chest pocket and the words "__name_company__" embroidered on the pocket and a name tag stitched above it reading "__name_first__".' + NOMORE,
        'A __name_tee_colour__ t-shirt on a hanger, with a printed picture of __name_logo_symbol__ and the words "__name_merch_slogan__" beneath it.' + NOMORE,
        'A __name_tee_colour__ sports shirt with the words "__name_town__" across the chest and the number "__name_number_small__" large on the back.' + NOMORE,
        'A folded stack of three t-shirts, the top one printed with the words "__name_brand_invented__" and the others plain.' + NOMORE,
        'A __name_tee_colour__ hooded sweatshirt with the words "__name_brand_upper__" across the chest and a small line "__name_established__" beneath.' + NOMORE]
    G['name_merch_other_prompt'] = [
        'A canvas tote bag hanging from a hook, printed with __name_logo_description__.' + NOMORE,
        'A ceramic mug on a desk, printed with the words "__name_shop__" and "__name_phone__".' + NOMORE,
        'A paper cup with a cardboard sleeve printed with __name_logo_description__.' + NOMORE,
        'A keyring tag on a hook with the words "__name_company__" stamped into it.' + NOMORE,
        'A pennant flag hanging on a wall with the words "__name_town__" on it in large letters.' + NOMORE,
        'A badge pinned to a jacket lapel showing __name_logo_symbol__ and no words or letters.',
        'A sticker on a laptop lid showing __name_logo_description__.' + NOMORE,
        'An apron hanging on a hook with the words "__name_restaurant__" embroidered on the chest.' + NOMORE,
        'A uniform jacket with a patch on the chest reading "__name_company__" and a name patch reading "__name_first__".' + NOMORE]
    G['name_merch_prompt'] = ['__name_cap_prompt__', '__name_tshirt_prompt__', '__name_merch_other_prompt__']
    G['v94merch_entry_points'] = ['name_logo_prompt', 'name_cap_prompt', 'name_tshirt_prompt', 'name_merch_other_prompt', 'name_merch_prompt', 'name_logo_description']
    return G
