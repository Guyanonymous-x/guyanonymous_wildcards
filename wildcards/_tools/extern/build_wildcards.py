import os, shutil, zipfile

ROOT = "illustration_wildcards"
NS = "illustration"  # wildcard namespace -> __illustration/<category>/<variable>__

D = {}  # category -> {variable: [values]}

D["medium"] = {
 "production_method": ["a traditional hand-made illustration", "a digital raster painting", "a crisp digital vector illustration", "a 3D-rendered illustration", "a hybrid of scanned traditional work and digital painting", "a photo-collage illustration", "a generative procedural artwork"],
 "dry_media": ["graphite pencil", "colored pencil", "vine charcoal", "compressed charcoal", "conte crayon", "soft pastel", "oil pastel", "wax crayon", "chalk", "silverpoint", "ballpoint pen", "alcohol marker", "water-based marker", "felt-tip pen", "fineliner technical pen"],
 "wet_media": ["watercolor", "gouache", "sumi ink wash", "dip pen and ink", "brush pen", "acrylic paint", "oil paint", "egg tempera", "casein paint", "airbrush", "spray paint", "coffee and tea stain", "encaustic wax"],
 "printmaking": ["woodcut print", "linocut print", "wood engraving", "etching", "drypoint", "aquatint", "mezzotint", "lithograph", "screen print", "risograph print", "monotype", "letterpress print", "cyanotype", "stencil print"],
 "cut_and_constructed": ["cut paper", "layered paper shadow box", "torn paper", "collage", "fabric applique", "embroidery", "felt craft", "plasticine claymation", "papercraft origami", "found-object assemblage", "mosaic", "stained glass"],
 "digital_tool": ["a hard round digital brush", "a soft airbrush", "a textured dry digital brush", "a pixel brush", "clean bezier vector paths", "gradient mesh", "lasso-cut flat fills", "smudge-blended digital paint", "photobashing", "paint-over on a 3D base", "voxels"],
 "substrate": ["bright white paper", "toned kraft paper", "rough cold-press watercolor paper", "smooth hot-press paper", "canvas", "a wood panel", "newsprint", "graph paper", "black paper", "translucent vellum", "cardboard", "a painted wall mural", "a clean digital canvas"],
 "media_mix": ["a single medium", "a combination of two media", "mixed media", "digital media imitating a traditional medium"],
 "tool_visibility": ["seamless invisible marks", "subtle visible tool marks", "evident tool marks", "expressive, celebrated brush marks"],
}

D["line"] = {
 "presence": ["no outlines, shapes only", "implied edges defined only by color changes", "selective outlines on key edges only", "outline-only drawing", "full line art", "line-dominant drawing where line carries everything"],
 "weight": ["hairline-thin lines", "thin lines", "medium-weight lines", "bold lines", "heavy chunky lines", "thick outer contours with thin inner lines"],
 "weight_variation": ["uniform monoline strokes", "tapered stroke ends", "pressure-sensitive swelling strokes", "calligraphic angled-nib strokes", "lines thicker on the shadow side", "lines thicker in the foreground"],
 "quality": ["clean confident lines", "smooth vector lines", "sketchy searching lines", "scratchy lines", "wobbly naive lines", "shaky jittery lines", "loose gestural lines", "rough dry-brush lines", "broken dashed lines", "dotted lines", "hatched lines"],
 "stroke_caps": ["rounded stroke ends", "square stroke ends", "pointed tapered stroke ends", "blunt brush stroke ends", "splattered stroke ends"],
 "corners": ["sharp mitered corners", "rounded line joins", "beveled corners", "overshooting lines that cross at the corners"],
 "closure": ["fully closed shapes", "open gapped lines", "lines stopping short of each other", "lost-and-found edges"],
 "line_color": ["black lines", "near-black lines", "lines in a single accent color", "colored lines matched to each object", "lines a darker shade of the fill", "lines lighter than the fill", "white reversed-out lines", "gradient lines"],
 "line_fill_registration": ["perfectly registered fills", "slightly misregistered offset fills", "fills that overflow the lines", "lines floating over loose color"],
 "interior_lines": ["contour lines only", "cross-contour lines", "fold and wrinkle lines only", "fully detailed interior lines", "speed and motion lines", "no interior lines"],
 "hatching": ["no hatching", "parallel hatching", "crosshatching", "contour hatching", "scribble hatching", "stippling", "engraving-style hatching", "Ben-Day dot shading"],
 "line_count": ["a single continuous line", "minimal lines", "a moderate number of lines", "dense masses of lines"],
 "construction": ["hidden construction lines", "faint construction lines left visible", "a visible sketch underlayer", "blueprint guide lines"],
}

D["shape"] = {
 "shape_language": ["circular rounded shapes", "square blocky shapes", "triangular angular shapes", "organic blobby shapes", "mixed geometric shapes", "tubular rubber-hose shapes", "crystalline faceted shapes", "spiky shapes", "biomorphic bone-and-cell forms", "biomechanical forms of flesh fused with machinery", "melting drooping forms"],
 "geometry_source": ["freehand shapes", "shapes built from geometric primitives", "grid-built shapes", "isometric-grid construction", "smooth bezier curves", "pixel-grid shapes", "low-poly polygonal facets"],
 "edge_quality": ["hard edges", "soft edges", "feathered edges", "rough deckled edges", "hard foreground edges with soft background edges"],
 "corner_radius": ["sharp corners", "slightly eased corners", "rounded corners", "fully rounded pill-shaped corners"],
 "simplification": ["hyper-detailed forms", "realistic forms", "moderately simplified forms", "iconic simplified forms", "pictogram-level simplification", "abstract marks"],
 "stylization": ["naturalistic stylization", "caricatured, exaggerated stylization", "geometric abstraction", "ornamental, decorative stylization", "distorted expressionist stylization", "cubist multi-view stylization", "surreal morphing stylization"],
 "exaggeration": ["no exaggeration", "subtle exaggeration", "moderate exaggeration", "strong exaggeration", "extreme cartoon-physics exaggeration"],
 "silhouette": ["incidental silhouettes", "readable silhouettes", "strong silhouette-first design"],
 "shape_contrast": ["uniform shape sizes", "a clear big-medium-small shape hierarchy", "extreme scale contrast between shapes"],
 "straights_vs_curves": ["all straight lines", "mostly straight lines", "straights balanced against curves", "mostly curved forms", "all curved forms"],
 "mass": ["light airy forms", "balanced mass", "solid bottom-heavy forms", "top-heavy forms", "elastic squash-and-stretch forms"],
 "symmetry": ["strict bilateral symmetry", "radial symmetry", "kaleidoscopic mandala symmetry", "near symmetry", "asymmetry", "deliberately lopsided forms"],
 "overlap": ["separated non-overlapping shapes", "simple overlapping shapes", "interlocking shapes", "transparent multiply overlaps", "knockout negative-space overlaps"],
 "fill_shapes": ["color shapes that follow the objects", "abstract color shapes independent of the objects", "posterized value shapes"],
 "metamorphosis": ["stable forms", "forms that subtly echo each other", "forms morphing into other forms", "a visible transformation sequence", "total fluidity where everything becomes everything else"],
}

D["color"] = {
 "color_mode": ["black and white", "grayscale", "single-hue tonal color", "duotone", "tritone", "a limited palette of four to six colors", "a moderate palette of seven to twelve colors", "full color", "spot colors only"],
 "harmony": ["monochromatic harmony", "analogous colors", "complementary colors", "split-complementary colors", "triadic colors", "tetradic square colors", "a single accent on neutrals", "discordant clashing colors", "vibrating equal-value complementary colors"],
 "saturation": ["desaturated greyed color", "muted color", "moderate saturation", "saturated color", "neon fluorescent color", "a muted base with saturated accents"],
 "value_range": ["high-key light values", "mid-key values", "low-key dark values", "a full value range", "compressed narrow values", "high contrast", "low contrast"],
 "temperature": ["a cool color temperature", "a neutral color temperature", "a warm color temperature", "warm light with cool shadows", "cool light with warm shadows"],
 "palette_character": ["a pastel palette", "an earthy palette", "a jewel-tone palette", "a candy palette", "a faded vintage palette", "a primary-color palette", "a neon synthwave palette", "a sepia palette", "a natural local-color palette", "a corporate brand palette", "a seasonal palette", "a muddy tonalist palette"],
 "local_vs_expressive": ["true local color", "slightly shifted local color", "arbitrary expressive color", "symbolic color coding"],
 "application": ["flat color fills", "hard-stepped cel color", "soft gradients", "linear and radial gradients", "blended painterly color", "broken color", "optical color mixing with dots", "glazed transparent layers", "gradient-mapped color"],
 "black_usage": ["pure black", "rich colored black", "dark colors instead of black", "no black at all"],
 "white_usage": ["the white of the paper left showing", "off-white cream tones", "pure white highlights", "no pure white"],
 "background_color": ["a white background", "an off-white paper background", "a solid color background", "a gradient background", "a dark background", "a plain isolated background", "a full scene background"],
 "accent": ["a single pop of accent color", "color accents on a grayscale image", "spot-color highlights", "no accent color"],
 "color_line_relationship": ["color kept inside the lines", "color independent of the lines", "colored lines with no fill", "fills with no lines"],
 "print_simulation": ["a CMYK offset-print look", "limited riso inks", "misregistered print layers", "halftone dots", "overprinted multiply inks", "glowing RGB screen color", "no print simulation"],
 "transparency": ["opaque color", "semi-transparent color layers", "watercolor transparency", "multiply-blended overlapping color"],
}

D["light"] = {
 "shading_method": ["flat with no shading", "hard one-step cel shading", "two-to-three tone shading", "soft gradient shading", "painterly blended shading", "hatched shading", "stippled shading", "halftone-dot shading", "grain-texture shading", "ambient occlusion only", "full realistic rendering"],
 "value_steps": ["one value step", "two value steps", "three value steps", "four to five value steps", "continuous tonal gradation"],
 "light_source": ["ambient light", "a single key light", "a key light with rim light", "multiple light sources", "strong backlighting into silhouette", "top-down light", "eerie underlighting", "a spotlight", "diffuse overcast light"],
 "light_consistency": ["physically consistent lighting", "loosely consistent lighting", "decorative shading for form rather than light", "lighting ignored entirely"],
 "shadow_shape": ["accurate cast shadows", "simplified geometric shadows", "graphic abstract shadow shapes", "long dramatic shadows", "drop shadows", "contact shadows only", "no shadows"],
 "shadow_color": ["shadows a darker shade of the same hue", "hue-shifted blue-purple shadows", "neutral gray shadows", "black shadows", "complementary-colored shadows", "transparent multiply shadows"],
 "highlights": ["specular highlight dots", "shaped highlights", "rim light", "glints and sparkles", "white line highlights", "glow and bloom highlights", "no highlights"],
 "bounce_light": ["no bounce light", "subtle reflected light", "pronounced colored bounce light"],
 "special_light": ["a soft glow", "bloom", "god rays", "lens flare", "neon emissive light", "bioluminescence", "warm firelight", "water caustics", "no special light effects"],
 "chiaroscuro": ["no chiaroscuro", "mild chiaroscuro", "strong chiaroscuro", "extreme tenebrism"],
 "form_rendering": ["flat forms", "suggested volume", "simplified volume", "fully modeled volume"],
}

D["texture"] = {
 "overall_texture": ["perfectly clean surfaces", "subtle grain", "moderate texture", "heavy texture", "texture-dominant surfaces"],
 "grain_type": ["film grain", "paper tooth", "pencil grain", "smudged charcoal", "airbrush speckle", "digital noise", "dithering", "halftone grain", "riso grain", "sandy stipple"],
 "brush_texture": ["smooth brushwork", "dry brush texture", "bristle streaks", "thick impasto", "sponge texture", "paint splatter", "watercolor blooms and bleeds", "pigment granulation", "salt texture", "wax resist"],
 "texture_placement": ["texture overlaid globally", "texture in the shadows only", "texture in the fills only", "texture on the edges only", "texture on selected objects only"],
 "surface_texture": ["object surfaces left untextured", "surface textures suggested with pattern hints", "fully rendered material textures"],
 "pattern": ["fill patterns of stripes and dots", "decorative ornament", "repeating motifs", "textile folk patterns", "fractal recursive patterns", "moire concentric line fields", "tessellating interlocking figures", "obsessive dot fields", "no patterns"],
 "imperfection": ["precise flawless execution", "a subtle wobble", "visible drips and ink blots", "smudges and fingerprints", "distressed worn surfaces", "digital glitches"],
 "finish": ["a matte finish", "a satin finish", "a glossy finish", "a metallic finish", "an iridescent finish", "a glassy finish", "a plastic vinyl-toy finish"],
 "edge_texture": ["crisp edges", "deckled edges", "bleeding edges", "chalky edges", "pixel-stepped edges", "torn edges"],
 "aging": ["pristine condition", "slightly aged", "a faded print", "a scratched surface", "folded and creased paper", "vintage paper stains"],
}

D["dimension"] = {
 "dimensional_feel": ["flat 2D", "flat layered 2D", "2.5D stacked parallax planes", "pseudo-3D", "full 3D", "toon-shaded 3D that looks 2D"],
 "projection": ["an orthographic elevation view", "isometric projection", "dimetric projection", "trimetric projection", "oblique cabinet projection", "one-point perspective", "two-point perspective", "three-point perspective", "curvilinear fisheye perspective", "reverse perspective", "multi-viewpoint perspective", "a top-down map view"],
 "perspective_accuracy": ["technically exact perspective", "loose but believable perspective", "intuitive naive perspective", "deliberately broken perspective", "impossible paradoxical space"],
 "camera_angle": ["an eye-level view", "a low worm's-eye view", "a high bird's-eye view", "an overhead flat-lay view", "a Dutch tilt", "an over-the-shoulder view", "a side-on profile view"],
 "lens": ["wide-angle distortion", "a normal lens", "compressed telephoto", "a macro close-up"],
 "depth_cues": ["overlapping forms", "diminishing scale", "atmospheric perspective", "values fading with distance", "cooler colors receding", "focus blur", "detail falloff with distance", "line weight falloff with distance", "no depth cues"],
 "depth_of_field": ["everything in focus", "shallow depth of field with bokeh", "tilt-shift miniature blur", "stylized blurred layers"],
 "ground_plane": ["figures floating with no ground", "a simple ground line", "a ground shadow only", "a full environment ground"],
 "layers": ["a single flat plane", "distinct foreground, midground and background", "many parallax layers"],
 "scale_logic": ["realistic scale", "hierarchical scale where important figures are larger", "miniature diorama scale", "surreal giant-and-tiny scale", "the subject small within a dominant habitat", "the subject filling the frame"],
}

D["composition"] = {
 "framing": ["a spot illustration with no frame", "a vignette fading out", "full bleed", "a bordered frame", "contained within a circle or badge", "comic panel framing", "figures breaking the frame", "a circular tondo", "an ornamental border frame"],
 "cropping": ["full figures with lots of air", "a medium crop", "a tight crop", "an extreme close-up", "an unexpected cut-off crop"],
 "density": ["a minimal composition", "a sparse composition", "a balanced composition", "a busy composition", "a maximalist horror-vacui composition"],
 "negative_space": ["dominant negative space", "active negative space that forms shapes", "moderate negative space", "almost no negative space"],
 "balance": ["centered symmetrical balance", "rule-of-thirds placement", "asymmetric balance", "off-balance tension", "radial balance"],
 "focal_strategy": ["a single focal point", "multiple focal points", "focal hierarchy by contrast", "focal hierarchy by color", "leading lines to the focal point", "no focal point, an all-over pattern"],
 "structure": ["a free composition", "a grid structure", "a diagonal structure", "a triangular structure", "a circular spiral structure", "a golden-ratio structure", "a Z-shaped reading path", "a tiled repeat structure", "a kaleidoscopic structure", "a fractal recursive structure", "a hidden-object scatter"],
 "viewpoint_distance": ["a macro view", "a close view", "a medium view", "a wide establishing view", "a panoramic view", "a cutaway cross-section", "an exploded view"],
 "narrative_structure": ["a single moment", "sequential comic panels", "a simultaneous narrative with several moments in one image", "an infographic flow", "a map"],
 "figure_ground": ["clear figure-ground separation", "ambiguous reversible figure-ground", "figures camouflaged into the ground"],
 "rhythm": ["repeated motifs", "pattern rhythm", "visual echoes", "no repetition"],
 "multi_panel_format": ["a single image", "a diptych", "a triptych", "a polyptych altarpiece", "a comic page", "a comic strip", "a handscroll", "a wraparound gatefold cover"],
}

D["character"] = {
 "figure_realism": ["photoreal figures", "realistic figures", "semi-realistic figures", "stylized figures", "cartoon figures", "chibi super-deformed figures", "stick-figure pictograms", "abstract figures"],
 "head_to_body_ratio": ["chibi proportions one to two heads tall", "cute proportions three to four heads tall", "cartoon proportions five to six heads tall", "realistic proportions seven heads tall", "heroic fashion proportions eight to nine heads tall", "elongated proportions ten heads tall"],
 "body_proportions": ["accurate body proportions", "elongated limbs", "big heads on small bodies", "oversized hands and feet", "tiny heads on large bodies", "bean-shaped barrel bodies", "heroic inverted-triangle torsos", "noodly rubber-hose limbs"],
 "body_type_range": ["a single idealized body type", "varied, diverse body types", "exaggerated body types", "identical uniform figures"],
 "anatomy": ["accurate muscles and bones", "simplified anatomy", "boneless fluid anatomy", "geometric construction anatomy"],
 "face": ["fully featured faces", "simplified faces", "minimal dot faces", "faceless figures", "mask-like symbolic faces"],
 "eyes": ["realistic eyes", "large anime eyes", "dot eyes", "bean-shaped eyes", "pie-cut eyes", "button eyes", "closed arc eyes", "glossy multi-highlight eyes", "no eyes"],
 "nose": ["realistic noses", "simple hooked line noses", "dot noses", "triangle noses", "no noses", "bulbous noses"],
 "mouth": ["realistic mouths", "simple line mouths", "open shape mouths", "cat-shaped mouths", "no mouths"],
 "hair": ["strand-rendered hair", "clumped locks of hair", "solid shape hair", "spiky anime hair", "flat silhouette hair", "pattern-filled hair"],
 "hands": ["realistic five-finger hands", "simplified hands", "four-fingered cartoon hands", "mitten hands", "white-gloved cartoon hands", "hidden hands"],
 "expression": ["neutral stoic expressions", "subtle expressions", "a full range of expressions", "elastic exaggerated expressions", "symbolic manga emotion marks"],
 "pose": ["static stiff poses", "natural poses", "dynamic poses", "exaggerated action poses", "poses driven by a strong line of action", "iconic frontal poses"],
 "skin_tone": ["naturalistic skin tones", "flat stylized skin tones", "unrealistic purple or blue skin", "unpainted line-only skin"],
 "clothing": ["fully rendered clothing", "simplified clothing folds", "flat-shape clothing", "patterned clothing", "clothing reduced to silhouettes"],
 "species": ["humans", "anthropomorphic animals", "animals", "creatures and monsters", "robot or object characters", "plant or food characters", "composite figures built from other objects"],
 "creature_design": ["accurately drawn real animals", "stylized animals", "classic fantasy creatures like dragons and griffins", "grotesque human-animal-object hybrids", "demons and chimeras", "biomechanical creatures", "xenomorphic aliens", "body-horror creatures", "cute monsters"],
}

D["environment"] = {
 "background_presence": ["no background", "a solid color field background", "an abstract shape background", "a suggested setting with only props", "a simplified scene", "a fully detailed environment"],
 "background_treatment": ["a background in the same style as the subject", "a less detailed background", "a softer blurred background", "a background in a different medium from the subject", "a desaturated background", "a silhouetted background"],
 "setting": ["an interior", "an urban exterior", "a natural landscape", "a fantasy world", "a science-fiction world", "an underwater scene", "outer space", "an abstract void", "a dreamscape"],
 "architecture": ["realistic architecture", "simplified block architecture", "wonky crooked architecture", "geometric architecture", "ornate architecture", "brutalist architecture", "organic architecture"],
 "nature_rendering": ["botanically accurate plants", "stylized trees and clouds", "lollipop trees", "patterned foliage", "silhouetted vegetation"],
 "sky": ["a flat color sky", "a gradient sky", "painted clouds", "stylized swirling clouds", "a patterned starry sky", "dramatic weather in the sky"],
 "atmosphere": ["haze and fog", "rain", "snow", "floating dust particles", "smoke", "light shafts", "clear air"],
 "time_of_day": ["dawn", "daytime", "golden hour", "blue-hour dusk", "night"],
 "props": ["no props", "a few key props", "lived-in detail", "overflowing hidden-object clutter"],
}

D["detail"] = {
 "realism": ["photorealistic", "hyperreal", "realistic", "semi-realistic", "stylized", "highly stylized", "abstract", "non-representational"],
 "detail_level": ["minimal detail", "low detail", "medium detail", "high detail", "obsessive intricate detail"],
 "detail_distribution": ["detail spread evenly everywhere", "detail concentrated at the focal point", "simplified edges", "detailed faces with everything else simple", "detailed backgrounds with simple figures"],
 "finish": ["a thumbnail sketch", "a rough sketch", "a loose finish", "a clean finish", "a highly polished glossy finish"],
 "abstraction_method": ["simplification", "geometric reduction", "fragmentation", "distortion", "color abstraction", "symbolic substitution"],
 "accuracy_intent": ["scientifically accurate", "documentary", "interpretive", "expressive", "fantastical"],
 "information_density": ["purely decorative", "lightly labeled", "annotated and diagrammatic", "data-dense"],
 "polish": ["labored and refined", "a balance of polish and spontaneity", "spontaneous alla prima", "deliberately unfinished"],
}

D["typography"] = {
 "text_presence": ["no text", "small labels and captions", "title lettering", "integrated text on signs and packaging", "type-led illustrated typography"],
 "lettering": ["hand lettering", "brush script", "clean sans-serif type", "classic serif type", "decorative display lettering", "a pixel font", "stencil lettering", "blackletter", "comic book lettering", "psychedelic warped lettering that fills its shape", "graffiti tags", "scrawled crossed-out handwriting"],
 "text_integration": ["text separate from the image", "text overlaid on the image", "text wrapped inside shapes", "text built into the scene", "text forming the image", "dense handwriting used as texture"],
 "graphic_devices": ["speech balloons", "onomatopoeia sound effects", "speed lines", "emanata like sweat drops and hearts", "arrows and callouts", "icons", "badges and stickers", "banners and ribbons", "no graphic devices"],
 "decorative_elements": ["sparkles and stars", "confetti", "floral borders", "decorative frames", "dividers", "ornament", "doodles", "no decoration"],
 "info_graphics": ["labels with leader lines", "charts", "maps with legends", "step diagrams", "cross-section callouts", "no infographic elements"],
 "iconography": ["line icons", "filled icons", "duotone icons", "glyph icons", "skeuomorphic icons"],
}

D["mood"] = {
 "emotional_tone": ["joyful", "cozy and warm", "calm and serene", "whimsical", "nostalgic", "melancholic", "mysterious", "eerie and unsettling", "dark and grim", "tense and dramatic", "epic and heroic", "romantic", "energetic", "sterile and clinical", "dreamy", "ecstatic and transcendent", "hallucinatory", "filled with dread", "mundane and neutral"],
 "humor": ["serious with no humor", "gentle humor", "witty clever humor", "slapstick humor", "absurd surreal humor", "satirical humor", "dark humor", "deadpan humor"],
 "intensity": ["quiet and understated", "moderately intense", "loud and bold", "overwhelming"],
 "audience": ["made for toddlers", "made for children", "made for young adults", "made for a general audience", "made for adults", "made for experts"],
 "narrative_approach": ["literal", "metaphorical and conceptual", "symbolic", "allegorical", "purely decorative", "ambiguous and open-ended"],
 "conceptual_device": ["direct depiction", "a visual pun", "juxtaposition", "scale play", "hybrid objects", "a visual metaphor", "a negative-space trick"],
 "era_feel": ["timeless", "antique", "Victorian", "mid-century", "1970s", "1980s", "1990s", "Y2K", "contemporary", "retro-futurist", "futurist"],
 "cultural_tone": ["universal", "regional", "folk vernacular", "punk", "skate culture", "rave culture", "corporate"],
 "viewer_relationship": ["observational", "intimate", "confrontational with a direct gaze", "voyeuristic", "instructional"],
 "subject_matter": ["everyday life", "natural history and wildlife", "portraiture", "landscape", "religious themes", "moral allegory", "mythology", "fantasy", "science fiction", "horror", "romance", "political satire", "history", "spiritual and cosmic themes", "pure form with no subject"],
 "strangeness": ["mundane and ordinary", "ordinary with one odd detail", "uncanny", "calmly impossible magic realism", "surreal dream logic", "a coherent fantastic invented world", "hallucinatory", "chaotic and incoherent"],
 "comfort": ["wholesome", "safe and neutral", "edgy", "grotesque", "disturbing"],
}

D["lineage"] = {
 "historical_movements": ["medieval illuminated manuscript", "Early Netherlandish painting", "Italian Renaissance", "Mannerism", "Baroque", "Romanticism", "Pre-Raphaelite", "Symbolism", "Impressionism", "Post-Impressionism", "Art Nouveau", "Arts and Crafts", "Expressionism", "Fauvism", "Cubism", "Futurism", "Constructivism", "Dada", "Metaphysical painting", "Surrealism", "Magic realism", "Fantastic realism", "Bauhaus", "Art Deco", "Social realism", "Abstract Expressionism", "Pop Art", "Op Art", "1960s psychedelic poster art", "Visionary art", "Minimalism", "Memphis design", "Postmodernism"],
 "illustration_eras": ["Golden Age of Illustration", "Victorian engraving", "pulp magazine art", "WPA poster art", "mid-century modern illustration", "UPA cartoon style", "1960s-70s editorial illustration", "1970s fantasy prog-rock album art", "1980s airbrush illustration", "1990s grunge illustration", "2000s Flash vector art", "2010s flat design", "corporate Memphis", "new ugly anti-design"],
 "comics_and_animation": ["ligne claire", "Franco-Belgian comics", "American superhero comics", "underground comix", "newspaper comic strip", "shonen manga", "shojo manga", "seinen manga", "anime cel style", "manhwa webtoon", "rubber-hose animation", "golden-age animation", "UPA limited animation", "cartoon modern", "adult animation", "storybook watercolor animation"],
 "east_asian": ["ukiyo-e woodblock", "sumi-e ink painting", "Chinese gongbi", "Chinese xieyi freehand painting", "Korean minhwa folk painting", "Japanese emaki scroll painting"],
 "south_and_west_asian": ["Mughal miniature", "Rajput painting", "Persian miniature", "Madhubani painting", "Kalighat painting", "Gond art", "Warli art", "Ottoman illumination"],
 "african_and_diasporic": ["Ndebele geometric painting", "Adinkra-inspired graphics", "Tingatinga painting", "Afrofuturism"],
 "americas": ["Mexican papel picado", "Mexican muralism", "Latin American folk art", "Huichol yarn painting"],
 "european_folk": ["Scandinavian folk art", "Polish wycinanki paper cut", "Russian lubok print", "Palekh lacquer miniature", "Hungarian folk embroidery", "Pennsylvania Dutch folk art"],
 "contemporary_digital": ["flat vector illustration", "isometric illustration", "low-poly art", "8-bit pixel art", "16-bit pixel art", "vaporwave", "synthwave", "lo-fi illustration", "kawaii", "Y2K chrome", "claymorphism", "glassmorphism", "neo-brutalism", "painterly concept art", "hand-painted game art", "die-cut sticker art", "Pop Surrealism"],
 "technical_and_scientific": ["botanical illustration", "zoological illustration", "wildlife naturalist painting", "medical anatomical illustration", "patent drawing", "architectural rendering", "technical exploded-view drawing", "cartographic illustration", "infographic illustration"],
 "vernacular": ["naive children's drawing", "outsider art", "traditional tattoo flash", "neo-traditional tattoo", "fine-line tattoo", "blackwork tattoo", "graffiti", "DIY zine art", "sketchbook doodles", "chalkboard art", "hand-painted signage", "generic clip art", "wordless assembly-instruction diagrams"],
}

D["context"] = {
 "purpose": ["an editorial illustration", "an advertising illustration", "a brand mascot", "a packaging illustration", "a book cover", "a picture book spread", "a children's educational illustration", "a graphic novel page", "concept art", "a game asset", "an app spot illustration", "an empty-state illustration", "an infographic", "a scientific plate", "a medical illustration", "a technical manual diagram", "a fashion illustration", "a poster", "an album cover", "a t-shirt graphic", "a tattoo flash sheet", "a fine art print", "a storyboard frame", "a social media post"],
 "reproduction": ["unlimited color", "designed for limited spot-ink printing", "designed for one-color printing", "embroidery-friendly", "vinyl-cut friendly with no gradients", "pixel-grid ready"],
 "size_legibility": ["readable at icon size", "a small spot illustration", "a half-page illustration", "a full-page spread", "a large-format billboard"],
}

D["childart"] = {}
# ---- additions from the 475-illustrator stress test ----
def add(cat, var, vals):
    D[cat].setdefault(var, [])
    for v in vals:
        if v not in D[cat][var]:
            D[cat][var].append(v)

add("medium", "dry_media", ["carbon dust"])
add("medium", "wet_media", ["gilding and metal leaf"])
add("medium", "printmaking", ["pochoir stencil coloring", "scratchboard"])
add("medium", "cut_and_constructed", ["black silhouette cut-outs"])
add("medium", "digital_tool", ["pen plotter lines"])
add("medium", "production_method", ["a drawing completed by real photographed objects", "a painting combined with photographed handmade puppets and models", "traced and collaged found imagery combined with watercolor"])
add("medium", "substrate", ["fabric calico"])
add("line", "hatching", ["feathered brush inking"])
add("light", "shading_method", ["large graphic spot blacks", "manga screentone shading"])
add("light", "special_light", ["crackling black energy dots"])
add("texture", "brush_texture", ["planar faceted brushstrokes"])
add("character", "body_proportions", ["chubby cherubic proportions"])
add("character", "pose", ["contorted fashion-model poses"])
add("character", "hair", ["hair as a massive dominant graphic shape"])
add("character", "idealization", ["unflattering and grotesque", "honest and observed", "flattering", "idealized", "sentimental and saccharine"])
add("dimension", "projection", ["a bent panorama blending bird's-eye view and horizon", "a schematic diagram with abstracted distances"])
add("composition", "structure", ["a timeline procession", "a comparison plate with specimens aligned", "a montage of floating heads"])
add("composition", "multi_panel_format", ["a single gag panel with a caption", "a character model sheet turnaround", "a sketchbook spread", "a die-cut lift-the-flap book page"])
add("composition", "framing", ["wrapped to the contour of a body or object"])
add("composition", "reveal_technique", ["a cutaway", "a cross-section", "an x-ray transparent view", "an ecorche view of flayed layers", "peel-back flaps", "an exploded view", "a skeleton inside the body silhouette", "a layered bone, muscle and skin reconstruction", "no reveal"])
add("composition", "panel_layout", ["a regular panel grid", "irregular panels", "borderless panels", "a splash page", "inset panels", "a whole page designed as one decorative image"])
add("composition", "repeat_type", ["a block repeat", "a half-drop repeat", "a brick repeat", "a mirror repeat", "a tossed scatter repeat", "a border stripe repeat"])
add("environment", "background_treatment", ["a photo-traced background behind simple characters"])
add("environment", "nature_rendering", ["anthropomorphized trees with faces in the bark"])
add("environment", "entourage", ["no scale figures", "ghosted silhouette scale figures", "simplified scale figures and trees", "fully rendered people, trees and vehicles"])
add("detail", "specimen_presentation", ["a specimen isolated on white", "a specimen with dissection details around it", "a life cycle shown on the host plant", "a specimen in its natural habitat", "a herbarium-pressed specimen", "several specimens aligned for comparison"])
add("detail", "accuracy_intent", ["reportage drawn on location"])
add("mood", "conceptual_device", ["absurd elaborate contraptions", "hidden embedded names and objects"])
add("typography", "lettering", ["copperplate calligraphy", "character-specific lettering styles"])
add("typography", "decorative_elements", ["shojo sparkle and flower backgrounds", "historiated initials and marginal drolleries"])
add("color", "print_simulation", ["split-fountain ink gradients"])
add("shape", "geometry_source", ["algorithmic rule-based shapes"])
add("lineage", "east_asian", ["shin-hanga woodblock", "Japanese irezumi"])
add("lineage", "americas", ["Northwest Coast formline", "Woodlands School painting", "Inuit printmaking", "Mexican broadsheet calavera print"])
add("lineage", "contemporary_digital", ["Superflat", "designer vinyl toy art", "generative plotter art"])
add("lineage", "technical_and_scientific", ["Isotype pictograms", "field-guide plate", "astronomical space art"])
add("lineage", "vernacular", ["courtroom sketch", "screen-printed gig poster"])
add("context", "genre", ["a children's picture book illustration", "a vintage children's portrait illustration", "a Golden Age storybook plate", "an architectural rendering", "a botanical plate", "a medical anatomical plate", "a paleoart reconstruction", "a field-guide wildlife plate", "an infographic cutaway", "a superhero comic page", "a European bande dessinee page", "a manga page", "a newspaper comic strip", "animation design", "an editorial conceptual illustration", "a political caricature", "a fashion illustration", "a vintage advertising poster", "a painted movie poster", "a paperback book cover", "fantasy concept art", "video game key art", "Indigenous-inspired folk art", "a fine-art woodblock print", "street art", "a courtroom reportage sketch", "outsider art", "tattoo flash", "a textile repeat pattern", "a screen-printed gig poster", "a propaganda poster", "astronomical space art", "designer toy character art", "an illuminated manuscript page", "generative plotter art", "a hand-lettered typographic illustration"])

SIGNATURES = [
 "frames that grow larger as the fantasy grows", "crosshatched night skies", "anatomically true small animals wearing tidy clothes",
 "hand-painted streaked tissue papers cut into shapes", "eyes sliding sideways to deliver a deadpan joke", "a small white dog hidden in the scene",
 "splayed spiky fingers and flailing scratchy limbs", "watercolor washes that ignore the lines", "no straight lines anywhere, droopy curved buildings",
 "color reserved only for the imaginary elements", "marbled paper collage", "a packed town scene with every object labeled",
 "mother-and-child intimacy", "children dressed in miniature adult finery", "each fairy costume matching a real flower species",
 "fairies with dragonfly wings against black silhouettes", "faces hidden in gnarled tree roots", "deep night blues with gold lantern glow",
 "elongated wind-swept figures in vast negative space", "stained-glass jewel color with minute patterning", "peacock-feather patterns in flat black and white",
 "a tiny figure before huge trolls in a mossy dark forest", "ornate folk-pattern borders framing the scene", "setback skyscrapers emerging from night fog and searchlights",
 "tiny precisely placed people giving architectural scale", "buildings dissolving into wet light", "endless stairs in an imaginary prison",
 "a building shown as a cutaway future ruin", "fragmented exploded planes seen from several viewpoints at once", "insect life cycles on their host plant",
 "dissected floral parts arranged around the specimen", "a single decaying leaf with every flaw shown", "specimens set against dramatic Romantic landscapes",
 "flayed muscle figures posing in landscapes", "skeletons posed beside a rhinoceros", "skin peeled open like wings",
 "names lettered directly on each structure", "the body drawn as an industrial factory", "creatures tiny in vast luminous landscapes",
 "a side-view skeleton inside a black body silhouette", "birds in identical poses with arrows to field marks", "hummingbirds gleaming with metallic leaf",
 "hundreds of tiny people working inside a cross-section", "a step-by-step construction sequence", "repeated identical icons counting quantities",
 "charts shaped like their subject", "black energy dot fields crackling around power", "fists thrust toward the viewer in extreme foreshortening",
 "pure black and white with one spot color", "huge flat black shadow shapes", "title lettering built into buildings and rain",
 "tangled chains and capes filling the page", "simple faces against meticulously researched backgrounds", "symmetrical crowds like Persian miniatures",
 "drawn in ballpoint on lined notebook paper", "a borderless page laid out as one decorative whole", "sparkles and flowers floating behind characters",
 "photo-traced backgrounds behind simple characters", "vast empty megastructures with tiny figures", "desert backgrounds that change every panel",
 "each character speaking in its own lettering", "tiny figures in vast detailed cityscapes", "vertical patterned stylized trees",
 "Celtic knotwork and circular motifs", "black jointed silhouette puppets on colored grounds", "a drawing completed by a real photographed object",
 "a negative-space double image", "a hidden name woven into the linework", "a thick black brushstroke contour with a single red accent",
 "hair as a massive flowing black shape", "a woman framed by a halo circle and hair arabesques", "one figure popping off a black background",
 "faceted planar brushstrokes and glossy hair", "a montage of floating heads with white pencil highlights", "spaceships with hazard stripes",
 "floating islands with organic flowing lettering", "robots in mundane countryside", "a character model sheet on white",
 "heavy black formlines exposing inner spirits", "owls with radiating plumes", "dot-and-dash fills inside flat silhouettes",
 "dressed-up skeletons", "rain as fine straight lines", "visible wood grain in the print",
 "energy lines radiating from flat figures", "x-ed out eyes", "smiling flowers and eyeball swarms",
 "crowns and crossed-out words", "enlarged Ben-Day dots with thick outlines", "drawings annotated with hand-lettered notes",
 "the artist drawn into the scene as a witness", "figures traced from magazines into epic panoramas", "surfaces covered in handwritten sermons",
 "a full-body composition flowing with the body's contours", "dense twining vines in a half-drop repeat", "flying eyeballs",
 "red wedges and hard diagonals", "a figure pointing straight at the viewer", "a mouthless minimal cute character",
 "interlace and spirals filling a giant initial", "gray grisaille with comic marginal drolleries", "trompe-l'oeil torn parchment",
 "disordered squares in pen plotter lines", "flow fields of thin parallel lines", "lettering built from physical objects",
]

# ---- additions from stress test 2 (250 new illustrators) ----
add("medium", "printmaking", ["prints stamped with doilies, sponges and found objects"])
add("medium", "cut_and_constructed", ["a painted story quilt with fabric borders"])
add("medium", "substrate", ["white line patterns painted on skin"])
add("medium", "production_method", ["a costume sketch with real fabric swatches pinned on", "a creature edited into a found photograph"])
add("medium", "digital_tool", ["a deliberately crude default paint program"])
add("line", "quality", ["deliberately awkward bad drawing", "raw ratty punk lines"])
add("line", "construction", ["direct ink with no underdrawing"])
add("shape", "stylization", ["product glamorization with stretched, lowered forms"])
add("character", "body_proportions", ["canonical proportions on a sacred iconometric grid"])
add("color", "color_mode", ["1-bit pure black and white pixels"])
add("color", "background_color", ["a gold-leaf ground"])
add("light", "special_light", ["hyper-luminous anime skies", "concentric translucent rings of light"])
add("texture", "imperfection", ["palimpsest traces of erased and redrawn charcoal"])
add("composition", "narrative_structure", ["a sequential zoom across pages", "a numbered narrative panel series"])
add("composition", "multi_panel_format", ["a color script of small thumbnails", "a chapter-head vignette", "a tailpiece vignette"])
add("composition", "structure", ["a cabinet of curiosities arrangement"])
add("composition", "puzzle_mechanic", ["no puzzle element", "a seek-and-find target hidden in the crowd", "hidden objects to find", "a maze", "a spot-the-difference pair", "an optical illusion with an ambiguous figure", "an infinite zoom", "a busy jigsaw-ready scene"])
add("dimension", "render_look", ["not 3D", "a toon-shaded 3D render", "a clay 3D render", "a soft pastel minimal 3D render", "a low-poly flat-shaded render", "an isometric 3D diorama", "a voxel render", "a photoreal cinematic 3D render", "a glossy product-studio render"])
add("detail", "accuracy_intent", ["historically reconstructed"])
add("mood", "conceptual_device", ["a scene built from everyday objects"])
add("mood", "sacred_conventions", ["no sacred conventions", "halos", "a mandorla of light", "deities with multiple arms", "blue-skinned deities", "figures holding symbolic attributes", "a hieratic frontal pose", "small donor figures kneeling at the edges"])
add("environment", "map_conventions", ["no map conventions", "a decorative cartouche", "a compass rose", "sea monsters in the ocean", "hachured mountains", "small story vignettes in the border", "pictorial landmarks", "a map made entirely of lettering"])
add("typography", "lettering", ["an illegible symmetrical black-metal logotype"])
add("context", "purpose", ["jigsaw puzzle art", "model-kit box art", "trading card art", "a skateboard deck graphic", "an airline safety card"])
add("context", "genre", ["a seek-and-find puzzle book spread", "a webcomic", "a horror book illustration", "a vintage pin-up calendar illustration", "a pulp paperback cover", "a Western art painting", "a military history plate", "an automotive advertising illustration", "a fantasy trading card", "a metal album cover", "an animation background painting", "a tech brand illustration", "a 3D illustration", "a costume design sketch", "a devotional icon", "an Indian calendar print", "a Tibetan thangka", "a fantasy map", "a satirical humor magazine page", "an old-master etching", "a nature journal page", "a pictogram system", "a wordless instruction manual"])
add("lineage", "comics_and_animation", ["webcomic", "Wimmelbuch", "MAD-style humor magazine"])
add("lineage", "illustration_eras", ["vintage pin-up", "pulp paperback noir", "punk flyer", "metal album art"])
add("lineage", "historical_movements", ["danse macabre", "Harlem Renaissance", "Byzantine Orthodox icon"])
add("lineage", "south_and_west_asian", ["Indian calendar art", "Tibetan thangka"])
add("lineage", "african_and_diasporic", ["Congolese popular painting", "Ethiopian icon painting"])
add("lineage", "east_asian", ["Japanese City Pop illustration"])
add("lineage", "americas", ["Argentine historieta", "American Western art"])
add("lineage", "technical_and_scientific", ["military history plate", "Olympic pictogram system", "costume design sketch"])
add("lineage", "contemporary_digital", ["fantasy trading card art", "analog horror"])

SIGNATURES += [
 "wool and fabric textures that make figures fuzzy", "kaleidoscopic patches of color inside animal shapes", "monumental low-angle portraits with a dignified gaze",
 "ink splats layered over pencil studies", "a field guide to invented creatures", "hundreds of drawings zooming in like a camera",
 "hundreds of tiny figures and one striped target to find", "every page zooming out to reveal a picture within a picture",
 "featureless stick people beside precise graphs", "each character colored a single body hue", "a calm dog in a burning room",
 "dripping, stringy, half-dissolved ghouls", "huge thin monsters edited into real photographs", "bulbous rounded bodies in lurid color",
 "a wholesome caught-in-the-moment pin-up scenario", "chrome robot figures reflecting their surroundings",
 "horses at full gallop with every hoof off the ground", "uniform and equipment accuracy as the point",
 "cars stretched lower and longer than real", "aircraft cutaways with every part numbered", "a tiny mouse hidden in the painting",
 "mossy twiggy faeries with goblin faces", "dragon skin like leathery stone", "gilded patterns on trading card art",
 "cryptic handwritten captions on punk drawings", "toxic green zombies", "illegible branching band logos", "jazz musicians drawn in one looping line",
 "misty forests suggested in a few strokes", "hyper-luminous skies with lens flare", "color blocks with no outlines",
 "tiny figures in vast soft gradient landscapes", "vintage photographs cut with flat geometric shapes",
 "mix-and-match modular people", "vivid gradients on a dark navy background", "palette color cycling that animates water",
 "isometric rooms like tiny dioramas", "costume sketches with fabric swatches pinned on", "dresses made of real flower petals",
 "round-headed children voicing world-weary politics", "wordless gags with bulbous noses",
 "paintings bordered with fabric and handwritten text", "concentric translucent rings of light over silhouettes", "white line patterns painted on skin",
 "empty pools, palms and cloudless skies", "cats with many eyes", "huge panoramas drawn in ink with no sketch",
 "reverse perspective on a gold ground", "glossy blue-skinned deities with halos", "deities drawn on a strict proportional grid",
 "map borders filled with little story scenes", "a sea crowded with monsters", "a map made entirely of hand-painted words",
 "hinged, flopping feet", "micro-cartoons squeezed into the page margins", "handwritten text and doodles on a legal pad",
 "nightmare creatures in smoky aquatint", "text and image etched together on one plate", "skeletons intruding on everyday life", "floating eyeballs in velvety black",
 "erased-and-redrawn charcoal traces left visible", "crude drawings with crossed-out deadpan text", "natural-history plates with violent narratives",
 "crowded species catalogs on one canvas", "tiny wood-engraved tailpiece vignettes",
 "athletes on a strict 45-degree pictogram grid", "a blank-faced figure assembling furniture", "calm faces during an emergency", "icons on a 32-pixel grid",
]

# ---- additions from stress test 3 (1,000 new illustrators) + children's art ----
add("medium", "substrate", ["old ledger paper with printed ruled lines and handwriting", "black oilcloth"])
add("medium", "printmaking", ["katazome stencil-dyed print", "reduction linocut built up color by color", "raised relief print", "chromolithograph with embossed gold", "printed tin lithography like an old toy", "thumbprint and fingerprint drawings"])
add("medium", "cut_and_constructed", ["chiseled wall relief carved into plaster", "paper quilling of rolled paper strips"])
add("medium", "wet_media", ["bark painting with fine crosshatched lines", "painted ceramic tile glaze", "henna and pigment on stretched leather", "reverse painting on glass", "mud-dyed cloth", "paint made from mud and earth pigments", "soft misty layered washes", "hand-painted dyed textile"])
add("medium", "production_method", ["real objects embedded in clear resin", "photographic cut-outs isolated on white with labels"])
add("line", "quality", ["wavy rippling outlines", "automatic drawing that wanders without a plan"])
add("line", "construction", ["figures built step by step from simple shapes"])
add("texture", "brush_texture", ["grid-mosaic painting made of tiny squares", "frottage rubbings of wood grain and leaves", "decalcomania blotted paint textures", "grattage scraped paint"])
add("dimension", "render_look", ["an ink-wash shaded 3D render"])
add("context", "purpose", ["a tarot card"])
add("composition", "puzzle_mechanic", ["an interactive press-here book page", "a maze built into a 3D cityscape"])
add("environment", "setting", ["a microscopic world of cells and molecules"])
add("composition", "structure", ["overlapping multiple exposures of motion", "a motion-sequence grid of frames"])
add("typography", "decorative_elements", ["hot-rod pinstriping"])
add("typography", "graphic_devices", ["rubber stamps and official seals"])
add("typography", "lettering", ["interlocking wildstyle graffiti letters"])
add("typography", "text_integration", ["tiny handwritten jokes and asides crammed into every gap"])
add("color", "color_mode", ["grayscale like a 3D depth map"])
add("color", "palette_character", ["a neon rainbow airbrushed palette"])
add("character", "body_proportions", ["inflated, voluminous rounded bodies"])
add("texture", "pattern", ["beadwork-style floral patterns", "curling Maori kowhaiwhai patterns", "interlocking Islamic geometric star tiles", "jigsaw-like cells filled with stripes"])
add("environment", "map_conventions", ["a flattened topographic miniature city seen from above"])
add("light", "special_light", ["jagged stylized flame and explosion shapes"])
add("detail", "mixed_rendering", ["one consistent rendering style", "cartoon characters on photo-realistic backgrounds", "realistic faces set in flat gold ornament", "each story layer drawn in a different style", "photographed real objects mixed with drawing", "one highly rendered focal object in a simple drawing"])
add("typography", "symbol_systems", ["no symbol system", "invented alphabets and cosmic symbols", "occult sigils", "esoteric diagrams with dense handwritten text", "Nsibidi-like symbols", "calligraphy shaped into animals", "unreadable asemic scribble writing", "hieroglyph-like pictograms"])
add("childart", "stage", [
 "a toddler's random scribbles in crayon, no recognizable shapes",
 "looping spiral scribbles and repeated dots by a three-year-old",
 "circular scribbles a four-year-old has named, a few closed shapes",
 "a five-year-old's drawing with tadpole people, objects floating on the page and arms coming out of heads",
 "a seven-year-old's drawing with a strip of blue sky at the top and everything standing on a green ground line",
 "a ten-year-old's careful pencil drawing with overlapping figures and the sky meeting the ground",
 "a young teen's shaded pencil drawing copying manga eyes, with uneven perspective",
 "a skilled teenager's sketchbook page with practiced shading and a personal style"])
add("childart", "ability", ["drawn with very little control, simpler than typical for the age", "typical for the child's age", "bold and confident, filling the whole page", "advanced for the age, with early proportion and shading", "precociously gifted, with adult-like observation but a child's choices"])
add("childart", "conventions", ["tadpole people with arms growing from the head", "a smiling sun with rays in the top corner", "a strip of blue sky with white space below", "a green ground line along the bottom", "lollipop trees", "a triangle-roof house with a chimney and curly smoke", "M-shaped birds in the sky", "a rainbow arch", "stick figures with circle hands and spiky fingers", "the whole family lined up in a row by height", "an x-ray view showing inside the house", "a fold-over road with trees lying flat on both sides", "the most important person drawn biggest", "the child's name in wobbly capitals with a backwards letter", "coloring that goes over the lines", "heavy waxy crayon pressure", "a favorite color used for everything"])
add("childart", "tools", ["wax crayons", "washable markers", "colored pencils", "poster paint with a thick brush", "finger paint", "sidewalk chalk", "a school watercolor set", "glitter glue", "construction-paper collage", "potato and sponge stamps", "handprints and fingerprints", "ballpoint pen on lined paper", "crayon on the back of a worksheet"])
add("lineage", "historical_movements", ["Nordic National Romanticism", "British Neo-Romanticism", "visionary paper architecture", "Symbolism and decadence"])
add("lineage", "comics_and_animation", ["Marcinelle atom-style comics", "josei manga", "gekiga manga", "Garo alternative manga", "Showa-era grotesque manga", "lianhuanhua picture-story books", "wuxia ink comics", "1980s anime OVA", "mecha design"])
add("lineage", "european_folk", ["Soviet avant-garde children's books", "Ukrainian folk painting", "Hlebine naive painting"])
add("lineage", "east_asian", ["Rinpa painting", "yokai bestiary woodblocks", "Chinese New Year nianhua prints", "sosaku hanga creative prints"])
add("lineage", "contemporary_digital", ["semi-realistic anime digital painting", "Kustom Kulture hot-rod art", "tiki art", "trash polka tattoo", "Chicano black-and-grey tattoo", "1980s toy-line art", "greeting card art"])
add("lineage", "illustration_eras", ["Polish School of Posters", "Swiss International Style", "Sachplakat object posters", "Grosvenor School linocut", "gothic romance paperback"])
add("lineage", "americas", ["Taller de Grafica Popular linocut", "Brazilian cordel woodcut", "Mixtec codex", "ledger art", "ayahuasca visionary painting"])
add("lineage", "south_and_west_asian", ["Amar Chitra Katha comics", "Pattachitra scroll painting", "Phad scroll painting", "Pakistani truck art", "Qajar painting"])
add("lineage", "african_and_diasporic", ["hand-painted Ghanaian movie posters"])
add("context", "genre", ["a child's drawing", "a children's art class project", "a toddler's scribble", "a Polish film poster", "a Swiss design poster", "a Kustom Kulture hot-rod flyer", "a lianhuanhua picture-story page", "a mecha design sheet", "a tarot card", "a greeting card"])

SIGNATURES += [
 "a dress that merges into the background", "glowing cobalt skies over columned idylls", "one purple crayon line drawing the whole world",
 "collage on old ledger paper", "light paint scraped over a dark ground", "cartoon monsters on photo-realistic backgrounds", "a grid-mosaic of tiny painted squares",
 "trolls that are also mountains", "a hedgehog lost in multiplane fog", "salami and junk scattered across the page",
 "wavy rippling outlines", "each story layer drawn in a different style", "bodies sliced along geometric lines", "motion drawn as solid lines",
 "jagged stylized flames and explosions", "sumi-e brushstrokes on 3D forms", "loose dabbed spaceships with glowing lights",
 "photographic cut-outs on white with labels", "overlapping exposures of a figure in motion", "hyperreal animals fading into blank paper",
 "an endless grid monument laid over landscapes", "rubber stamps, fingerprints and fake documents", "a tiny mouse commenting in every cartoon",
 "a barefoot child seen only from behind", "hand-cut shapes with scrawled type", "letters formed by human bodies",
 "pills and leaves embedded in resin", "frottage rubbings and blotted paint", "bone-like forms on an infinite plain",
 "bulging-eyed hot-rod monsters", "grayscale depth-map figures", "portraits chiseled into wall plaster", "six-line stick figures",
 "swirling motion in linocut", "crosshatched bark painting", "drawings on antique ledger pages", "reflective ornamented truck art",
 "letters shaped into animals", "bright figures painted on the back of glass", "paper quilling portraits", "invented alphabets and cosmic symbols",
 "inflated voluminous bodies", "Mixtec codex profile figures", "a realistic face set in flat gold-leaf ornament", "occult sigils",
 "jungles with every leaf outlined", "figures painted on black oilcloth", "jigsaw-like cells filled with stripes",
 "animals built from simple shapes step by step", "thumbprint creatures", "pages crowded with tiny people and handwritten gags", "a maze built into a 3D city",
 "tadpole people with arms from the head", "a smiling sun in the top corner", "the family lined up by height",
]

SUBJECTS = [

"a fox sleeping under a tree", "a lighthouse on a stormy coast", "a woman reading in a cafe", "a city street at rush hour", "an old fisherman mending nets", "a giant whale floating over a village", "a cup of coffee on a desk", "a knight facing a dragon", "a child flying a kite", "a bowl of fruit", "an astronaut in a garden", "a crowded night market", "a cat on a windowsill", "a mountain cabin in winter", "a robot watering plants", "a musician playing cello", "an owl in a forest at night", "a family dinner", "a ship in a bottle", "a botanical specimen of a fern"]

# 30 presets derived from the stress test, described by variables only (no artist names)
PRESETS = [
 "an Early Netherlandish oil painting on panel in triptych format, horror vacui crowded with tiny grotesque human-animal-object hybrids, a high bird's-eye view, a simultaneous narrative of many small scenes, moral allegory, hallucinatory dream logic, luminous glazed color, fine detail",
 "outsider art in colored pencil, horror vacui, ornamental bands, dense handwriting and musical notation used as texture, flat saturated color, obsessive intricate detail",
 "a cat rendered with kaleidoscopic mandala symmetry, fractal recursive ornament, saturated vibrating color, flat decorative patterning, hallucinatory",
 "a 1960s psychedelic concert poster, screen printed, vibrating equal-value complementary colors, psychedelic warped lettering that fills its shape, flat fills, swirling organic forms",
 "visionary art in acrylic, x-ray anatomical figures showing nerves and energy, radiant geometric grids, kaleidoscopic symmetry, glowing color, ecstatic and transcendent, hyper-detailed",
 "a 1970s fantasy prog-rock album cover, fine brush and airbrush, biomorphic forms morphing into landscape, metamorphosis, glowing jewel-tone color, fantastic realism, hyper-detailed",
 "a biomechanical airbrush painting, near-monochrome gray, flesh fused with machinery, repeating ribbed patterns, low-key values, disturbing and grotesque",
 "a bleak oil painting, low-key warm palette, decaying architecture that resembles bodies, vast scale, no narrative, filled with dread",
 "horror manga in black ink, realistic faces, spiral motifs, body-horror creatures, high contrast, eerie and unsettling",
 "a Mannerist oil portrait in profile, the head built entirely from fruit, vegetables and flowers, composite figure, witty, realistic rendering",
 "a Surrealist oil painting with an academic polished finish, melting drooping forms, a deep empty plain, long hard shadows, surreal dream logic",
 "a monochrome lithograph of tessellating interlocking figures, impossible paradoxical space, precise flawless execution, cool and cerebral",
 "a Pop Surrealism oil painting, smooth glossy finish, big-eyed children, kitsch symbols, pastel palette, cute and creepy",
 "chaotic ink splatter and loose gestural lines, grotesque caricature, satirical, edgy, expressive celebrated marks",
 "a magic realist oil painting, fine detail, elongated figures, alchemical machines, muted warm palette, calmly impossible",
 "obsessive dot fields covering everything, saturated primary colors, all-over pattern, no focal point",
 "symbolic abstraction in tempera, diagrammatic spiritual symbols, pastel and primary colors, spiritual and cosmic themes",
 "non-representational abstraction, geometric and organic shapes in musical rhythm, saturated color, dynamic diagonals",
 "realistic oil painting of a coherent fantastic invented world, plein-air lighting, believable dinosaurs and architecture, warm natural light",
 "clean ink linework leaning to ligne claire, vast desert science-fiction landscape, soft flat color, wide establishing view",
 "fine pen crosshatching, Edwardian costume, deadpan dark humor, black and white, macabre and quiet",
 "a dramatic wood engraving, extreme tenebrism, epic scale, dense engraving-style hatching, biblical and literary",
 "a Renaissance engraving with contour hatching, black and white, precise anatomy, hyper-detailed",
 "a scientific lithograph plate of specimens in radial symmetry, ornamental arrangement, scientifically accurate, hyper-detailed",
 "a natural history watercolor and pastel of life-size birds on a white background, dynamic pose, scientifically accurate",
 "a realistic acrylic wildlife painting, the animal small and camouflaged within a dominant habitat, muted natural color, detail spread evenly across the scene, calm",
 "a realistic oil illustration of everyday small-town life, gentle humor, detailed props, warm natural light",
 "precise ligne claire comics, diagrammatic page layout, muted flat color, melancholic and deadpan",
 "minimal mid-century geometric wildlife illustration, flat vector-like shapes, no outlines, limited palette",
 "a minimal picture-book illustration with thick black outlines, primary colors, frontal pose, dot eyes, white background",
 "generic flat vector clip art, monoline icons, neutral mood, white background, instructional",
]

# ---- Plain-language glosses for text encoders (Krea 2 / Qwen3-VL): term kept, visual meaning spelled out ----
GLOSS = {
 # medium
 "conte crayon": "conte crayon, a hard chalky drawing stick in red or black",
 "silverpoint": "silverpoint, delicate pale gray metal-stylus lines",
 "carbon dust": "carbon dust technique, soft velvety gray tones brushed from powdered charcoal",
 "casein paint": "casein paint with a flat, chalky matte finish",
 "encaustic wax": "encaustic hot wax paint with thick translucent layers",
 "egg tempera": "egg tempera with fine hatched brushstrokes and a luminous matte surface",
 "sumi ink wash": "sumi ink wash, black ink diluted into soft gray brush washes",
 "gilding and metal leaf": "gilding with shiny gold and metal leaf",
 "bark painting with fine crosshatched lines": "ochre paint on bark with fine crosshatched lines",
 "hand-painted dyed textile": "hand-painted and dyed cotton cloth with ink outlines",
 "drypoint": "drypoint etching with soft, fuzzy burred lines",
 "aquatint": "aquatint etching with grainy tonal areas like ink wash",
 "mezzotint": "mezzotint with velvety blacks and soft glowing highlights",
 "monotype": "monotype print, a painterly one-off ink transfer",
 "risograph print": "risograph print with grainy bright spot inks and slight misregistration",
 "cyanotype": "cyanotype, white silhouettes on deep Prussian blue",
 "pochoir stencil coloring": "pochoir, crisp hand-stenciled flat watercolor layers",
 "scratchboard": "scratchboard, fine white lines scratched out of a black surface",
 "katazome stencil-dyed print": "katazome stencil-dyed print with flat colors and white resist outlines",
 "raised relief print": "embossed raised relief print with sculpted texture",
 "chromolithograph with embossed gold": "vintage chromolithograph with rich colors and embossed gold",
 "lithograph": "lithograph with soft crayon-textured tones",
 "letterpress print": "letterpress print with bold inked wood type",
 "wood engraving": "wood engraving with fine white lines cut into solid black",
 "gradient mesh": "smooth vector gradient-mesh shading",
 "lasso-cut flat fills": "sharp lasso-cut flat color shapes",
 "photobashing": "photobashing, paint blended over photo fragments",
 "voxels": "voxels, tiny 3D cubes like building blocks",
 "clean bezier vector paths": "clean, smooth vector curves",
 "pen plotter lines": "thin even pen-plotter lines drawn by a machine",
 "a generative procedural artwork": "a generative artwork made by code, with rule-based repeated marks",
 # line
 "lost-and-found edges": "lost-and-found edges where outlines fade in and out",
 "sharp mitered corners": "sharp pointed line corners",
 "beveled corners": "clipped, beveled line corners",
 "Ben-Day dot shading": "Ben-Day dot shading, evenly spaced printed dots like vintage comics",
 "feathered brush inking": "feathered brush inking, tapering parallel brushstrokes in the shadows",
 "contour hatching": "contour hatching, lines curving around the form",
 "cross-contour lines": "cross-contour lines wrapping around forms like a wireframe",
 "engraving-style hatching": "engraving-style swelling parallel lines like banknote art",
 "raw ratty punk lines": "raw, ratty, deliberately ugly punk lines",
 "stippling": "stippling, shading built from thousands of tiny dots",
 "scribble hatching": "scribbled loops used as shading",
 # shape
 "tubular rubber-hose shapes": "tubular rubber-hose limbs like 1930s cartoons",
 "posterized value shapes": "posterized flat value shapes, like a reduced-color photo",
 "knockout negative-space overlaps": "overlaps cut out as empty negative space",
 "cubist multi-view stylization": "cubist stylization showing several viewpoints at once",
 "biomorphic bone-and-cell forms": "biomorphic forms like bones, cells and seed pods",
 "crystalline faceted shapes": "crystalline faceted shapes with flat angled planes",
 # color
 "duotone": "duotone, two ink colors only",
 "tritone": "tritone, three ink colors only",
 "spot colors only": "flat spot colors only, no blending",
 "analogous colors": "analogous colors, neighboring hues on the color wheel",
 "split-complementary colors": "split-complementary colors, one hue with the two neighbors of its opposite",
 "triadic colors": "triadic colors, three evenly spaced hues",
 "tetradic square colors": "two pairs of opposite colors",
 "high-key light values": "high-key, mostly pale light tones",
 "mid-key values": "mostly middle tones",
 "low-key dark values": "low-key, mostly dark tones",
 "compressed narrow values": "a narrow range of similar values",
 "a muddy tonalist palette": "a muted tonalist palette of hazy browns and grays",
 "broken color": "broken color, separate visible dabs of different hues",
 "gradient-mapped color": "gradient-mapped color with shadows and highlights in different hues",
 "hard-stepped cel color": "hard-edged cel color like animation cels",
 "true local color": "true local color, every object in its real color",
 "a CMYK offset-print look": "an offset-printed magazine look with visible CMYK dots",
 "limited riso inks": "limited bright risograph inks",
 "overprinted multiply inks": "overprinted transparent inks that darken where they overlap",
 "split-fountain ink gradients": "split-fountain rainbow ink gradients from screen printing",
 "vibrating equal-value complementary colors": "vibrating complementary colors of equal brightness that seem to buzz",
 "grayscale like a 3D depth map": "smooth grayscale like a 3D depth map, near things white and far things black",
 # light
 "ambient occlusion only": "soft contact shadows only where forms meet",
 "large graphic spot blacks": "large solid black shadow shapes",
 "manga screentone shading": "manga screentone shading with gray dot patterns",
 "hard one-step cel shading": "hard cel shading with one sharp shadow tone",
 "bloom": "soft light bloom around bright areas",
 "water caustics": "rippling water caustic light patterns",
 "crackling black energy dots": "crackling clusters of black dots around energy",
 "extreme tenebrism": "extreme tenebrism, figures emerging from near-total darkness",
 "strong chiaroscuro": "strong chiaroscuro, dramatic contrast of light and dark",
 "mild chiaroscuro": "mild chiaroscuro, gentle light and dark modeling",
 "jagged stylized flame and explosion shapes": "jagged, angular stylized flames and explosions like 1980s anime effects",
 # texture
 "thick impasto": "thick impasto paint ridges",
 "pigment granulation": "grainy pigment granulation in watercolor",
 "salt texture": "starry salt-sprinkled watercolor texture",
 "wax resist": "wax resist, crayon marks repelling watercolor",
 "decalcomania blotted paint textures": "decalcomania, blotted paint with spongy organic textures",
 "grattage scraped paint": "grattage, layers of paint scraped through",
 "frottage rubbings of wood grain and leaves": "frottage, pencil rubbings of wood grain and leaves",
 "paper tooth": "visible paper tooth texture",
 "dithering": "pixel dithering patterns",
 "riso grain": "risograph print grain",
 "moire concentric line fields": "moire patterns of concentric lines",
 "tessellating interlocking figures": "tessellating figures that interlock with no gaps",
 "curling Maori kowhaiwhai patterns": "curling red, black and white Maori kowhaiwhai scroll patterns",
 "palimpsest traces of erased and redrawn charcoal": "ghostly traces of erased and redrawn charcoal",
 "deckled edges": "deckled torn-paper edges",
 # dimension
 "dimetric projection": "dimetric projection, an angled technical 3D view",
 "trimetric projection": "trimetric projection, an angled technical 3D view with unequal axes",
 "oblique cabinet projection": "oblique projection with a flat front face and depth drawn at an angle",
 "reverse perspective": "reverse perspective where far edges get wider, like an icon",
 "an orthographic elevation view": "a flat orthographic front elevation with no perspective",
 "a schematic diagram with abstracted distances": "a schematic map like a subway diagram",
 "a Dutch tilt": "a Dutch tilt with a tilted horizon",
 "atmospheric perspective": "atmospheric perspective, distant things paler and bluer",
 "2.5D stacked parallax planes": "2.5D, flat layers stacked at different depths",
 # composition
 "a maximalist horror-vacui composition": "a maximalist horror-vacui composition with every inch filled",
 "a circular tondo": "a circular tondo painting",
 "full bleed": "a full-bleed image running to every edge",
 "a polyptych altarpiece": "a multi-panel altarpiece",
 "a handscroll": "a long horizontal handscroll",
 "a color script of small thumbnails": "a color script, a grid of small color thumbnails",
 "a chapter-head vignette": "a small chapter-head vignette above the text",
 "a tailpiece vignette": "a small tailpiece vignette ending a chapter",
 "an ecorche view of flayed layers": "an ecorche view showing the muscles beneath the skin",
 "a block repeat": "a simple block repeat pattern",
 "a half-drop repeat": "a half-drop repeat pattern offset by half a tile",
 "a brick repeat": "a brick-offset repeat pattern",
 "an infinite zoom": "an infinite zoom where the scene contains itself",
 "a splash page": "a full-page comic splash panel",
 "a montage of floating heads": "a movie-poster montage of floating heads",
 "a sequential zoom across pages": "a sequence zooming closer frame by frame",
 "a cabinet of curiosities arrangement": "a cabinet-of-curiosities arrangement of many specimens on shelves",
 "ambiguous reversible figure-ground": "an ambiguous figure-ground where shapes flip between object and background",
 # character
 "chibi super-deformed figures": "chibi super-deformed figures with huge heads and tiny bodies",
 "pie-cut eyes": "pie-cut eyes, black ovals with a wedge cut out like 1930s cartoons",
 "symbolic manga emotion marks": "manga emotion marks like sweat drops and anger veins",
 "canonical proportions on a sacred iconometric grid": "strict sacred proportions like Tibetan thangka deities",
 "xenomorphic aliens": "eyeless, elongated alien creatures",
 "emanata like sweat drops and hearts": "cartoon emanata like sweat drops, hearts and stars around heads",
 # mood
 "a hieratic frontal pose": "a hieratic, rigid frontal pose like a religious icon",
 "a mandorla of light": "an almond-shaped mandorla of light around the whole body",
 "uncanny": "uncanny, almost normal but subtly wrong",
 # environment
 "a decorative cartouche": "a decorative cartouche frame holding the map title",
 "hachured mountains": "mountains drawn with hachures, short parallel strokes",
 "brutalist architecture": "brutalist raw concrete architecture",
 "ghosted silhouette scale figures": "pale ghosted silhouettes of people for scale",
 # detail
 "spontaneous alla prima": "spontaneous alla prima, painted wet in one sitting",
 "a herbarium-pressed specimen": "a flattened, pressed plant specimen on herbarium paper",
 "hyperreal": "hyperreal, sharper than a photograph",
 # typography
 "historiated initials and marginal drolleries": "an ornate decorated initial letter with tiny comic creatures in the margins",
 "hot-rod pinstriping": "hot-rod pinstriping, symmetrical swooping thin lines",
 "blackletter": "blackletter gothic type",
 "copperplate calligraphy": "flowing copperplate script",
 "an illegible symmetrical black-metal logotype": "an illegible, symmetrical, spiky black-metal band logo",
 "skeuomorphic icons": "skeuomorphic icons that look like real objects",
 "glyph icons": "solid single-color glyph icons",
 "occult sigils": "occult sigils, abstract magical symbols",
 "Nsibidi-like symbols": "Nsibidi-like West African ideographic symbols",
 "onomatopoeia sound effects": "big drawn sound-effect words like BAM and POW",
 # lineage: comics & animation
 "ligne claire": "ligne claire comics, clean even outlines, flat colors and no hatching",
 "underground comix": "1960s underground comix, crude crosshatched satirical cartooning",
 "UPA limited animation": "UPA-style 1950s limited animation with flat graphic shapes",
 "UPA cartoon style": "1950s UPA cartoon style with flat angular shapes",
 "cartoon modern": "1950s cartoon modern, angular stylized design",
 "rubber-hose animation": "1930s rubber-hose animation with bendy limbs and pie-cut eyes",
 "Wimmelbuch": "Wimmelbuch, a wordless busy picture book teeming with tiny people",
 "Marcinelle atom-style comics": "Belgian atom-style comics with rubbery figures and 1950s boomerang furniture",
 "josei manga": "josei manga, elegant comics for adult women",
 "gekiga manga": "gekiga, gritty realistic 1960s Japanese comics",
 "Garo alternative manga": "Garo-style alternative manga, raw dreamlike ink",
 "lianhuanhua picture-story books": "lianhuanhua, small Chinese picture-story books with fine line drawings and captions",
 "wuxia ink comics": "Chinese martial-arts wuxia ink comics",
 "1980s anime OVA": "1980s anime OVA cel style",
 "seinen manga": "seinen manga for adult readers",
 "manhwa webtoon": "Korean webtoon with clean digital color",
 "MAD-style humor magazine": "1960s humor magazine satire cartooning",
 # lineage: contemporary
 "lo-fi illustration": "lo-fi illustration, cozy soft anime-style scenes",
 "claymorphism": "claymorphism, soft puffy 3D shapes",
 "glassmorphism": "glassmorphism, frosted translucent glass panels",
 "neo-brutalism": "neo-brutalist graphics with thick black outlines and flat bright blocks",
 "Superflat": "Superflat, flat anime pop art",
 "analog horror": "analog horror, degraded VHS-like eerie imagery",
 "trash polka tattoo": "trash polka tattoo, red and black collage",
 "Chicano black-and-grey tattoo": "fine-line Chicano black-and-grey tattoo",
 "corporate Memphis": "corporate Memphis, flat figures with tiny heads and huge limbs",
 "new ugly anti-design": "new ugly anti-design, deliberately clashing crude graphics",
 "Y2K chrome": "Y2K chrome, glossy liquid-metal shapes",
 "vaporwave": "vaporwave, pink and teal 1990s computer nostalgia",
 "designer vinyl toy art": "designer vinyl toy art, glossy simplified collectible figures",
 "Kustom Kulture hot-rod art": "Kustom Kulture hot-rod art with bug-eyed monsters",
 "generative plotter art": "generative plotter art, thin machine-drawn lines",
 # lineage: east asian
 "Chinese gongbi": "Chinese gongbi, meticulous fine-line color painting",
 "Chinese xieyi freehand painting": "Chinese xieyi, loose expressive freehand ink",
 "Korean minhwa folk painting": "Korean minhwa folk painting with flat bright tigers and magpies",
 "Japanese emaki scroll painting": "Japanese emaki narrative scroll painting",
 "shin-hanga woodblock": "shin-hanga, early 20th-century Japanese woodblock with soft gradients",
 "Japanese irezumi": "Japanese irezumi tattoo art with waves, koi and wind bars",
 "Japanese City Pop illustration": "1980s Japanese City Pop illustration with clean pools, palms and blue skies",
 "Rinpa painting": "Rinpa, bold decorative Japanese painting on gold",
 "yokai bestiary woodblocks": "Edo-period yokai bestiary woodblocks",
 "Chinese New Year nianhua prints": "Chinese New Year nianhua, bright red folk prints",
 "sosaku hanga creative prints": "sosaku hanga, bold self-carved Japanese prints",
 # lineage: south & west asian
 "Rajput painting": "Rajput miniature painting",
 "Madhubani painting": "Madhubani painting, double outlines with hatched and patterned fills",
 "Kalighat painting": "Kalighat painting, bold sweeping outlines and flat color",
 "Gond art": "Gond art, figures filled with dots and dashes",
 "Warli art": "Warli art, white stick figures on earthy red",
 "Ottoman illumination": "Ottoman illumination with gold floral borders",
 "Indian calendar art": "glossy Indian calendar art",
 "Amar Chitra Katha comics": "Amar Chitra Katha Indian myth comics",
 "Pattachitra scroll painting": "Pattachitra cloth painting with ornate borders",
 "Phad scroll painting": "Phad, a long Rajasthani epic scroll painting",
 "Pakistani truck art": "Pakistani truck art, dense ornament and bright reflective color",
 "Qajar painting": "Qajar Persian painting with lacquer-glossy figures",
 # lineage: africa
 "Ndebele geometric painting": "Ndebele painting, bold black-outlined geometric color blocks",
 "Adinkra-inspired graphics": "West African Adinkra symbol graphics",
 "Tingatinga painting": "Tingatinga painting, glossy flat-colored animals",
 "Congolese popular painting": "Congolese popular painting with written captions",
 "Ethiopian icon painting": "Ethiopian icon painting with large almond eyes",
 # lineage: americas
 "Huichol yarn painting": "Huichol yarn painting, bright yarn pressed into wax",
 "Northwest Coast formline": "Northwest Coast formline, ovoids and U-shapes in black and red",
 "Woodlands School painting": "Woodlands School painting, bold black lines and bright flat color",
 "Mexican broadsheet calavera print": "Mexican broadsheet prints of dressed-up skeletons",
 "Argentine historieta": "Argentine historieta comics",
 "Taller de Grafica Popular linocut": "Mexican Taller de Grafica Popular political linocut",
 "Brazilian cordel woodcut": "Brazilian cordel woodcut, bold black folk prints",
 "Mixtec codex": "Mixtec codex, flat profile figures on a bright ground",
 "ledger art": "Plains ledger art drawn on antique ledger pages",
 # lineage: european folk & history
 "Polish wycinanki paper cut": "Polish wycinanki, symmetrical folk paper cut",
 "Russian lubok print": "Russian lubok folk print",
 "Palekh lacquer miniature": "Palekh, tiny gold-detailed figures on black lacquer",
 "Hlebine naive painting": "Hlebine naive painting on the back of glass",
 "Metaphysical painting": "metaphysical painting, empty arcades and long shadows",
 "Fantastic realism": "Vienna School fantastic realism, jewel-like detailed visions",
 "danse macabre": "danse macabre, skeletons dancing with the living",
 "Byzantine Orthodox icon": "Byzantine icon, gold ground and flat solemn figures",
 "British Neo-Romanticism": "British Neo-Romanticism, moody English landscapes",
 "Memphis design": "1980s Memphis design, squiggles and clashing shapes",
 "Op Art": "Op Art optical patterns",
 "Early Netherlandish painting": "Early Netherlandish painting, glowing detailed oil on panel",
 "Mannerism": "Mannerism, elongated elegant figures",
 "visionary paper architecture": "visionary paper architecture, unbuildable dreamlike buildings",
 # lineage: eras & technical
 "WPA poster art": "1930s WPA silkscreen posters",
 "Sachplakat object posters": "Sachplakat object posters, a single product and its name",
 "Swiss International Style": "Swiss International Style, grids and sans-serif type",
 "Grosvenor School linocut": "1930s Grosvenor School linocut with swirling motion",
 "Polish School of Posters": "Polish School of Posters, painterly surreal film posters",
 "Isotype pictograms": "Isotype pictograms, repeated icons counting quantities",
 "patent drawing": "black-line patent drawing with numbered parts",
 # context
 "a lianhuanhua picture-story page": "a Chinese lianhuanhua picture-story page",
 "a European bande dessinee page": "a European comic album page",
 "a paleoart reconstruction": "a paleoart reconstruction of prehistoric life",
 "tattoo flash": "a tattoo flash sheet",
 "an empty-state illustration": "an app empty-state illustration",
}

ALLVALS = {v for c in D.values() for vs in c.values() for v in vs}
_missing = [k for k in GLOSS if k not in ALLVALS]
assert not _missing, _missing

def w(cat, var):
    return f"__{NS}_{cat}_{var}__"

def medium_any():
    return "{" + "|".join(w("medium", v) for v in ["dry_media", "wet_media", "printmaking", "cut_and_constructed"]) + "}"

def lineage_any():
    keys = list(D["lineage"].keys())
    return "{" + "|".join(w("lineage", k) for k in keys) + "}"

def cat_sentence(cat):
    return ", ".join(w(cat, v) for v in D[cat])

LABELS = {
 "medium": "Medium", "line": "Linework", "shape": "Shapes and forms", "color": "Color",
 "light": "Light and shading", "texture": "Texture and surface", "dimension": "Space and perspective",
 "composition": "Composition", "character": "Figures", "environment": "Setting",
 "detail": "Detail and fidelity", "typography": "Text and graphic elements", "mood": "Mood and narrative",
 "lineage": "Lineage", "context": "Use", "childart": "Child artist",
}

def category_block(cat):
    if cat == "medium":
        return (f"Medium: {w('medium','production_method')} in {medium_any()}, "
                f"using {w('medium','digital_tool')}, on {w('medium','substrate')}, "
                f"{w('medium','media_mix')}, with {w('medium','tool_visibility')}.")
    if cat == "lineage":
        return f"Lineage: in the tradition of {lineage_any()}."
    return f"{LABELS[cat]}: {cat_sentence(cat)}."

SUBJ = f"__{NS}_subject__"

def core_prompt():
    return (f"An illustration of {SUBJ}. "
            f"{w('medium','production_method')} in {medium_any()}, in the tradition of {lineage_any()}. "
            f"{w('line','presence')}, {w('line','quality')}, {w('line','weight')}. "
            f"{w('shape','shape_language')}, {w('shape','simplification')}. "
            f"{w('color','color_mode')}, {w('color','palette_character')}, {w('color','saturation')}, {w('color','application')}. "
            f"{w('light','shading_method')}, {w('light','light_source')}. "
            f"{w('texture','overall_texture')}, {w('dimension','dimensional_feel')}, {w('dimension','camera_angle')}. "
            f"{w('composition','density')}, {w('detail','detail_level')}. "
            f"The mood is {w('mood','emotional_tone')} and {w('mood','strangeness')}.")

def build():
    if os.path.exists(ROOT):
        shutil.rmtree(ROOT)
    base = ROOT
    os.makedirs(ROOT)
    count = 0; nvals = 0
    for cat, vars_ in D.items():
        for var, vals in vars_.items():
            for v in vals:
                assert not any(c in v for c in "|{}") and "__" not in v, v
            out = [GLOSS.get(v, v) for v in vals]
            for v in out:
                assert "(" not in v and ")" not in v and "[" not in v, v
            with open(os.path.join(base, f"{NS}_{cat}_{var}.txt"), "w") as f:
                f.write("\n".join(out) + "\n")
            count += 1; nvals += len(vals)
    with open(os.path.join(base, f"{NS}_subject.txt"), "w") as f:
        f.write("\n".join(SUBJECTS) + "\n")
    with open(os.path.join(base, f"{NS}_presets_stress_test_styles.txt"), "w") as f:
        f.write("\n".join(PRESETS) + "\n")
    with open(os.path.join(base, f"{NS}_presets_signature_devices.txt"), "w") as f:
        f.write("\n".join(SIGNATURES) + "\n")
    for s in SIGNATURES + PRESETS + SUBJECTS:
        assert not any(c in s for c in "|{}") and "__" not in s, s

    P = ROOT
    def save(name, text):
        with open(os.path.join(P, "prompt_" + name), "w") as f:
            f.write(text.strip() + "\n")

    STYLE_CATS = [c for c in D if c != "childart"]
    # master: every variable (reference; longer than Krea 2's 512-token limit)
    master = [f"An illustration of {SUBJ}."] + [category_block(c) for c in STYLE_CATS]
    save("00_master_all_variables.txt", "\n".join(master))
    # master split into parts that each fit a 512-token text encoder
    PARTS = [("a", ["medium", "line", "shape"]), ("b", ["color", "light"]), ("c", ["texture", "dimension"]),
             ("d", ["composition"]), ("e", ["character"]), ("f", ["environment", "detail"]),
             ("g", ["typography", "mood", "lineage", "context"])]
    for tag, cats in PARTS:
        save(f"00{tag}_master_part_{'_'.join(cats)}.txt", "\n".join([f"An illustration of {SUBJ}."] + [category_block(c) for c in cats]))
    save("01_core.txt", core_prompt())

    # one focused prompt per category: core + every variable in that category
    for i, cat in enumerate(STYLE_CATS, start=2):
        save(f"{i:02d}_focus_{cat}.txt", core_prompt() + "\n" + category_block(cat))

    n = 1 + len(STYLE_CATS)
    # spectrum prompts (fixed anchors + wildcards for the rest)
    spectrum = {
     "realistic_hyperdetailed": "An illustration of {S}. {M}, photorealistic, obsessive intricate detail, accurate muscles and bones, {L}, {SH}, technically exact perspective, a full value range, {T}, {MOOD}, labored and refined.",
     "surreal_insane": "An illustration of {S}. {M}, {SHAPE_LANG}, forms morphing into other forms, {CREATURE}, impossible paradoxical space, a maximalist horror-vacui composition, vibrating equal-value complementary colors, hallucinatory, chaotic and incoherent, {L}.",
     "abstract": "A non-representational illustration inspired by {S}. {M}, geometric reduction, {SHAPE_LANG}, {HARM}, {APP}, no focal point, an all-over pattern, pure form with no subject.",
     "minimal_boring": "An illustration of {S}. A crisp digital vector illustration, generic clip art, iconic simplified forms, uniform monoline strokes, flat color fills, a limited palette of four to six colors, a white background, flat with no shading, a minimal composition, mundane and neutral, safe and neutral.",
    }
    fill = {"S": SUBJ, "M": f"{w('medium','production_method')} in {medium_any()}", "L": lineage_any().join(["in the tradition of ", ""]),
            "SH": w('light','shading_method'), "T": w('texture','overall_texture'), "MOOD": w('mood','emotional_tone'),
            "SHAPE_LANG": w('shape','shape_language'), "CREATURE": w('character','creature_design'),
            "HARM": w('color','harmony'), "APP": w('color','application')}
    for k, t in spectrum.items():
        n += 1
        out = t
        for key, val in fill.items():
            out = out.replace("{" + key + "}", val)
        save(f"{n:02d}_spectrum_{k}.txt", out)

    # random style generator: picks 1 value from a random subset of categories (Dynamic Prompts N$$ syntax)
    n += 1
    all_vars = [w(c, v) for c in STYLE_CATS for v in D[c] if c != "lineage"] + [lineage_any()]
    save(f"{n:02d}_random_8_variables.txt", f"An illustration of {SUBJ}, " + "{8$$, $$" + "|".join(all_vars) + "}.")
    n += 1
    save(f"{n:02d}_random_16_variables.txt", f"An illustration of {SUBJ}, " + "{16$$, $$" + "|".join(all_vars) + "}.")
    n += 1
    save(f"{n:02d}_preset_styles.txt", f"An illustration of {SUBJ}, {w('presets','stress_test_styles')}.")
    n += 1
    save(f"{n:02d}_genre_plus_signatures.txt",
         f"{w('context','genre')} of {SUBJ}, featuring {w('presets','signature_devices')} and {w('presets','signature_devices')}" +
         f", {w('medium','production_method')} in {medium_any()}, {w('color','palette_character')}, {w('mood','emotional_tone')}.")
    n += 1
    save(f"{n:02d}_genre_core.txt", f"{w('context','genre')} of {SUBJ}. " + core_prompt().split('. ', 1)[1])
    n += 1
    save(f"{n:02d}_child_art.txt", f"A real child's drawing of {SUBJ}: {w('childart','stage')}, {w('childart','ability')}, made with {w('childart','tools')}.")
    n += 1
    CHILD_STAGES = [
     "by a two-year-old, random back-and-forth crayon scribbles running off the edge of the paper, no recognizable shapes, one or two colors",
     "by a three-year-old, looping spiral scribbles and stabbed dots in thick washable marker, a few wobbly closed circles",
     "by a four-year-old, a big circle head with legs and arms sticking straight out, objects floating at random on the page, wax crayon",
     "by a five-year-old, tadpole people with arms coming out of their heads, a smiling sun with rays in the top corner, a purple dog because purple is her favorite, heavy crayon",
     "by a seven-year-old, a strip of blue sky at the top with white space below, everything standing on a green ground line, a triangle-roof house with curly chimney smoke, lollipop trees and M-shaped birds, markers and colored pencils",
     "by an eight-year-old, the whole family lined up in a row by height, an x-ray view showing people inside the house, a fold-over road with trees lying flat on both sides, poster paint",
     "by a ten-year-old, careful pencil outlines colored in with colored pencils, overlapping figures, the sky finally meeting the ground, a little stiff and self-conscious",
     "by a thirteen-year-old, a shaded graphite drawing with manga-style eyes copied from comics, uneven perspective, crosshatching tried for the first time, on lined notebook paper",
     "by a talented fifteen-year-old, a sketchbook page with confident observational drawing, practiced shading and a personal style still finding itself",
    ]
    save(f"{n:02d}_child_art_by_stage.txt", "A real child's drawing of " + SUBJ + ", " + "{" + "|".join(CHILD_STAGES) + "}" + ".")
    return count, nvals

if __name__ == "__main__":
    c, v = build()
    print(c, "variable files,", v, "values")
