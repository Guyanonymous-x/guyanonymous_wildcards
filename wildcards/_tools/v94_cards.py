"""v94 business cards: positioned, fully defined text. Company data (name, web, email, phone, address) is baked in per line so it stays consistent."""
import random
R = random.Random(9402)
NOMORE = ' No other words or letters appear on the card.'
TITLES = ['Managing Director', 'Sales Manager', 'Chief Executive', 'Account Executive', 'Head of Operations', 'Senior Engineer', 'Architect', 'Photographer', 'Consultant', 'Veterinary Nurse', 'Accountant', 'Solicitor', 'Dentist', 'Plumber', 'Electrician', 'Carpenter', 'Chef', 'Baker', 'Florist', 'Landscape Gardener', 'Interior Designer', 'Graphic Designer', 'Marketing Director', 'Estate Agent', 'Insurance Broker', 'Financial Adviser', 'Personal Trainer', 'Massage Therapist', 'Hairdresser', 'Tattoo Artist', 'Mechanic', 'Taxi Driver', 'Locksmith', 'Piano Tuner', 'Tutor', 'Translator', 'Editor', 'Author', 'Musician', 'DJ', 'Event Planner', 'Wedding Photographer', 'Property Manager', 'Owner', 'Founder', 'Partner', 'Director of Sales', 'Customer Service Lead', 'Quality Inspector', 'Site Foreman']
STOCK = ['printed on thick cream card stock with a slightly textured surface', 'printed on smooth white card stock with a matte finish', 'printed on heavy black card stock with silver lettering', 'printed on kraft brown card with dark ink', 'printed on glossy white card with a coloured band along one edge', 'printed on pale grey card with embossed lettering that catches the light', 'printed on ivory card with letterpress lettering pressed slightly into the surface', 'printed on thin recycled card with flecks of fibre showing', 'printed on white card with a gold foil edge', 'printed on pale blue card with dark navy lettering', 'printed on soft green card with white lettering', 'printed on warm yellow card with black lettering', 'printed on red card with white lettering', 'printed on clear plastic with white lettering']
SCENE = ['A single business card lying flat on a polished wooden desk, photographed from directly above.', 'A single business card held between two fingers in front of a softly blurred office.', 'A small stack of business cards in a brass holder on a reception counter, the top card facing the viewer.', 'A business card propped against a coffee cup on a cafe table.', 'Three business cards fanned out on a dark slate surface.', 'A business card tucked under the edge of a laptop on a desk.', 'A business card pinned to a cork board among small paper notes with no readable text.', 'A business card lying on a shop counter beside a small plant.', 'A business card in a clear display stand on a trade show table.', 'A business card resting on an open notebook with blank pages.', 'A close view of a business card on a marble tabletop with a pen beside it.']
LAYOUT = {
 'top_left': 'In the top left corner the company name "{co}" is printed in bold letters. In the centre of the card the name "{{PERSON}}" is printed in large letters with the job title "{{TITLE}}" on the line below it in smaller letters. Along the bottom edge are three lines: "{tel}", "{mail}" and "{web}".',
 'centered': 'Everything is centred. The company name "{co}" is at the top in capital letters, the name "{{PERSON}}" is in the middle in large letters, the job title "{{TITLE}}" is directly beneath it, and the bottom of the card has two lines reading "{tel}" and "{web}".',
 'split': 'The card is split into two halves. On the left half the name "{{PERSON}}" is printed on the first line, the job title "{{TITLE}}" on the second line and the company name "{co}" on the third line. On the right half, from top to bottom, are the lines "{addr}", "{tel}" and "{mail}".',
 'minimal': 'A minimal design with plenty of empty space. The name "{{PERSON}}" is printed small in the lower left corner, and the company name "{co}" is printed small in the upper right corner. Nothing else is printed on the front.',
 'corporate': 'A corporate layout. The company name "{co}" is printed across the top edge in large letters. Below it on the left are the name "{{PERSON}}" and the job title "{{TITLE}}". Below it on the right are the lines "{tel}", "{mail}" and "{addr}". At the bottom edge is the line "{web}".',
 'vertical': 'The card is turned to portrait orientation. The company name "{co}" is printed at the top, the name "{{PERSON}}" is printed in the middle, the job title "{{TITLE}}" is printed below the name, and at the bottom are the lines "{tel}" and "{mail}".',
 'back_front': 'The front of the card has only the company name "{co}" in the centre. The back of the card, seen beside it, has the name "{{PERSON}}" on the first line, the job title "{{TITLE}}" on the second line, and "{tel}" and "{mail}" on the following lines.',
 'tradesperson': 'A trade card. The top line reads "{co}" in bold letters. The line beneath reads "{{TITLE}}". In the middle the name "{{PERSON}}" is printed in large letters, and at the bottom are the lines "{tel}" and "{addr}".',
}
def companies(P, n):
    out = []; seen = set()
    stems = P['name_stem_latin'] + P['name_stem_tech'] + P['name_stem_german'] + P['name_stem_nordic'] + P['name_stem_japanese']
    corp = ['Industries', 'Logistics', 'Systems', 'Labs', 'Foods', 'Motors', 'Consulting', 'Studio', 'Design', 'Partners', 'Group', 'Solutions', 'Engineering', 'Media', 'Supply', 'Services', 'Law', 'Dental', 'Realty', 'Plumbing', 'Electrical', 'Landscapes', 'Catering', 'Photography', 'Print']
    suf = ['Inc.', 'Ltd.', 'LLC', 'Co.', 'GmbH', '']
    while len(out) < n:
        st = R.choice(stems); slug = st.lower()
        if slug in seen: continue
        seen.add(slug)
        co = (st + ' ' + R.choice(corp) + ' ' + R.choice(suf)).strip()
        web = 'www.' + slug + '.example'
        mail = R.choice(['info', 'hello', 'contact', 'sales', 'office']) + '@' + slug + '.example'
        tel = 'Tel 555 0' + str(R.randint(100, 199))
        addr = '%d %s %s' % (R.randint(2, 98), R.choice(['High', 'Mill', 'Station', 'Market', 'Harbour', 'Queen', 'Canal', 'Orchard', 'Bridge', 'Park']), R.choice(['Street', 'Road', 'Lane', 'Avenue', 'Square', 'Way']))
        out.append(dict(co=co, web=web, mail=mail, tel=tel, addr=addr))
    return out
def build(P):
    G = {}
    G['name_job_title'] = TITLES
    G['name_card_stock'] = STOCK
    G['name_card_scene'] = SCENE
    cos = companies(P, 120)
    for k, t in LAYOUT.items():
        lines = []
        for c in cos:
            s = t.format(**c).replace('{PERSON}', '__name_person__').replace('{TITLE}', '__name_job_title__')
            lines.append(s)
        G['name_card_layout_' + k] = lines
    G['name_card_layout'] = ['__name_card_layout_%s__' % k for k in LAYOUT]
    G['name_business_card_prompt'] = ['__name_card_scene__ The card is __name_card_stock__. __name_card_layout__' + NOMORE]
    G['name_business_card_simple_prompt'] = ['A business card __name_card_stock__. __name_card_layout__' + NOMORE]
    G['v94cards_entry_points'] = ['name_business_card_prompt', 'name_business_card_simple_prompt']
    return G
