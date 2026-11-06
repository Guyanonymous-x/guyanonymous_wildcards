"""v109 fixes: negations removed from the v57 framing pack (frame_* files), and negated quality defects (blur, haze, noise, grain,
softness) removed from illustration, photo-style and light files.
The v57 clarity opener ended "and no blur, haze, noise or compression artefacts"; MOSS_IMAGE_NOTES (line 48) found that Moss training
captions annotate exactly those defects, so naming them, even negated, may invite them. The same pack's composition lines used
"nothing cropped", "no part of the body", "nobody cropped", "no people in frame". Each line now says what is there instead.
fix(G) takes {file name: list of lines} and returns it repaired. Applied at the end of v109_build, and once directly to the working library."""
REPL = {
    'frame_clarity': [
        ('Ultra-sharp, high-resolution image with crisp focus throughout, fine detail, clean edges, accurate natural colour and no blur, haze, noise or compression artefacts.',
         'Ultra-sharp, high-resolution image with crisp focus throughout, fine detail, clean edges and accurate natural colour.'),
        ('Razor-sharp, high-resolution image with fine detail, clean edges, natural colour and no blur, noise or artefacts.',
         'Razor-sharp, high-resolution image with fine detail, clean edges and natural colour.'),
        ('Crisp, high-definition image, sharply focused from front to back, with clear edges, true colours and fine texture and no blur or digital noise.',
         'Crisp, high-definition image, sharply focused from front to back, with clear edges, true colours and fine texture.'),
        ('Extremely sharp, detailed, high-resolution image with clean lines, accurate colour and no softness, haze or artefacts.',
         'Extremely sharp, detailed, high-resolution image with clean lines and accurate colour.')],
    'frame_person_full': [
        ('Wide-angle environmental portrait with the entire person visible from head to toe, with clear space above the head and below the feet and nothing cut off at any edge of the frame.',
         'Wide-angle environmental portrait with the entire person visible from head to toe, with clear space above the head and below the feet, the whole body well inside the edges of the frame.'),
        ('Wide environmental portrait with the complete figure centred, head to toe, and no part of the body touching or cropped by the frame edges.',
         'Wide environmental portrait with the complete figure centred, head to toe, the whole body well inside the frame with open space on every side.'),
        ('Full-body shot from a comfortable distance, the whole person and a good amount of the surroundings in frame, nothing cropped.',
         'Full-body shot from a comfortable distance, the whole person from head to feet and a good amount of the surroundings in frame.')],
    'frame_group_full': [
        ('Wide environmental group portrait with every person visible from head to toe, nobody cropped or cut off by any edge, and people arranged so that no one hides another.',
         'Wide environmental group portrait with every person visible from head to toe, the whole group well inside the edges of the frame, and people spaced apart so that every face and body is clearly seen.')],
    'frame_room': [
        ('Wide interior view straight on, the whole space visible with nothing cropped, even natural light, architectural magazine style.',
         'Wide interior view straight on, the whole space visible from wall to wall and floor to ceiling, even natural light, architectural magazine style.')],
    'frame_landscape': [
        ('Wide-angle landscape with a clear foreground, middle ground and background and no people in frame, natural light of the stated time and weather, rich tonal range.',
         'Wide-angle landscape with a clear foreground, middle ground and background, the land open, empty and still, natural light of the stated time and weather, rich tonal range.')],
    'frame_animal_quad_prompt': [
        ('the whole animal entirely inside its own panel and nothing cut off by the panel edges,',
         'the whole animal entirely inside its own panel with open space around it,')],
    # The same negated quality defects (blur, haze, noise, grain, softness) in illustration, photo-style and light files.
    # Technique negations such as "no anti-aliasing", "no gloss" or "no volumetric light" are left for a separate decision.
    'illustration_texture_edge_texture': [
        ('sharply defined clean boundaries between shapes, no blur or bleed, high clarity,', 'sharply defined clean boundaries between shapes, high clarity,')],
    'illustration_texture_overall_texture': [
        ('perfectly clean surfaces, smooth even colour with no grain, no noise, flat clear shapes,', 'perfectly clean surfaces, smooth even colour, flat clear shapes,')],
    'illustration_medium_digital_tool': [
        ('crisp-edged uniform strokes with no softness,', 'crisp-edged, hard uniform strokes,')],
    'photostyle_grain_texture': [
        ('clean digital smoothness with no grain at all, perfectly smooth gradients,', 'clean digital smoothness, perfectly smooth gradients,'),
        ('crisp tiny textures, smooth gradations, no noise, sharp edges,', 'crisp tiny textures, smooth, clean gradations, sharp edges,'),
        ('a silky, grainless surface like a large-format contact print,', 'a silky, glass-smooth surface like a large-format contact print,')],
    'illustration_texture_surface_texture': [
        ('smooth flat colour on every object, no grain or material detail,', 'smooth flat colour on every object, plain bare surfaces,')],
    'photostyle_era': [
        ('glass and concrete spaces, crisp edges with no grain,', 'glass and concrete spaces, crisp, clean edges,')],
    'photostyle_process_bw': [
        ('neutral grey tonal range, noiseless shadows,', 'neutral grey tonal range, deep, clean shadows,'),
        ('modern crisp clarity, no grain', 'modern crisp clarity')],
    'photostyle_process_color': [
        ('neutral accurate color, no grain, smooth gradients,', 'neutral accurate color, smooth gradients,')],
    'photostyle_sig_early_modernist': [
        ('even light, grainless clarity,', 'even light, smooth, glassy clarity,')],
    # Shared object detail pools (v75) that imply printed or stamped text.
    'ob_glass_detail': [('a printed measuring scale', 'a moulded pouring lip')],
    'ob_metal_detail': [("a stamped maker's plate", 'a riveted plain steel plate'), ('a hand-written tab', 'a small loop of wire'), ('a small hinge that no longer lines up', 'a small hinge set slightly askew')],
    'ob_paper_detail': [('a stamped date', 'a torn corner'), ('a rubber-stamped mark', 'a faint ink smudge'), ('a hand-written note in the margin', 'a pencil line in the margin'), ('a sticky-note flag', 'a coloured paper flag')],
    'ob_paper_wear': [('written over in pencil', 'shaded over in pencil')],
    'ob_paper_mat': [('thin newsprint', 'thin grey pulp paper')],
    'ob_wood_detail': [('a hand-lettered tab', 'a small brass tab')],
    'ob_plastic_detail': [('a peeling sticker', 'a scuffed plastic clip')],
    'ob_appliance_detail': [('a hum and a faint light', 'a small glowing indicator light'), ('a sticker with a service number', 'a small vent grille')],
    'ob_appliance_wear': [('covered in magnets and notes', 'covered in fridge magnets')],
    'ob_fabricated_detail': [('a plaque', 'a carved stone ledge')],
    'lite_volum': [
        (' clear air with no haze ', ' crystal-clear air '),
        ('clear crisp light with zero haze', 'clear crisp light in crystal-clear air')],
}
def fix(G):
    for k, pairs in REPL.items():
        if k not in G: raise KeyError('v109_stage: %s not loaded' % k)
        for old, new in pairs:
            hits = [i for i, l in enumerate(G[k]) if old in l]
            if not hits and not any(new in l for l in G[k]): raise ValueError('v109_stage: text not found in %s: %s' % (k, old[:60]))
            for i in hits: G[k][i] = G[k][i].replace(old, new)
    return G
