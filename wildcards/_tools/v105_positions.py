"""v105 - named sex positions (from the Wikipedia 'Sex position' list), written as physical placement. L5/L6 pools by family."""
PF='a woman __apose_person_f__,'; PM='a man __apose_person_m__,'
TAIL=' The scene is in __apose_place__. The light is __apose_light__. '
CAM='The shot is from the side showing both bodies.'
P={
'man_on_top':[
 "{W} lies on her back on a bed with her legs raised straight up and resting against the chest of {M}, who kneels between her thighs. His erect penis is inside her vagina and his hands hold her ankles.",
 "{W} lies on her back with her knees drawn up against her chest and {M} kneels in front of her pressing her thighs close to her body. His erect penis is inside her vagina.",
 "{W} lies on her back with her ankles crossed behind her head and {M} lies full length on top of her. His erect penis is inside her vagina.",
 "{W} lies on her back on a bed with her legs apart and {M} lies on top of her facing her, his forearms on the mattress beside her head. His erect penis is inside her vagina.",
 "{W} lies on her back with a pillow under her hips, and {M} stands at the end of the bed lifting her pelvis with both hands, her legs resting on his shoulders. His erect penis is inside her vagina.",
 "{W} lies face down on a bed with her legs together and {M} lies on top of her back with his legs either side of hers, his hands beside her shoulders. His erect penis is inside her vagina from behind."],
'woman_on_top':[
 "{M} lies on his back on a bed and {W} squats over his hips facing him with her feet flat on the mattress and her hands on his chest. His erect penis is inside her vagina.",
 "{M} lies on his back and {W} straddles his hips facing him, leaning back with her hands on the mattress behind her. His erect penis is inside her vagina and her breasts and stomach face the ceiling.",
 "{M} lies on his back on a bed and {W} kneels astride his hips facing away from him, her hands on his shins and her back arched. His erect penis is inside her vagina.",
 "{M} lies on his back with his upper back resting on a low sofa and his feet flat on the floor, and {W} straddles him facing him with her feet on the floor either side of him. His erect penis is inside her vagina."],
'side_by_side':[
 "{W} and {M} lie on their sides facing the same way, her back against his chest and his arm under her neck. His erect penis is inside her vagina from behind.",
 "{W} lies on her side on a bed and {M} kneels behind her holding her upper thigh raised. His erect penis is inside her vagina.",
 "{W} lies on her back with her knees up and apart and {M} lies on his side at right angles to her with his hips under her raised thighs, forming a T. His erect penis is inside her vagina.",
 "{W} lies on her side on the edge of a bed and {M} stands behind her holding her hip. His erect penis is inside her vagina from behind."],
'rear_entry':[
 "{W} kneels on all fours on a bed with her chest lowered toward the mattress at an angle and {M} kneels behind her holding her hips. His erect penis is inside her vagina.",
 "{W} lies face down with her legs together and {M} straddles the backs of her thighs, his hands on the mattress either side of her waist. His erect penis is inside her vagina.",
 "{W} kneels upright on a bed with her wrists held gently behind her back by {M}, who kneels behind her. His erect penis is inside her vagina.",
 "{W} stands bent forward at the waist with her palms flat on a table and {M} stands behind her holding her hips. His erect penis is inside her vagina."],
'standing':[
 "{W} and {M} stand facing each other, her arms around his neck and one of her feet raised onto a chair, his hand holding her raised thigh. His erect penis is inside her vagina.",
 "{M} stands holding {W} against a wall, her legs wrapped around his waist and her arms around his neck. His erect penis is inside her vagina.",
 "{W} lies on her back on the edge of a bed with her hips raised and {M} stands above her holding her legs. His erect penis is inside her vagina."],
'sitting':[
 "{M} sits cross-legged on a bed and {W} sits on his lap facing him with her legs wrapped around his back and her arms around his shoulders. His erect penis is inside her vagina.",
 "{M} sits in an armchair and {W} sits across his lap sideways with her back against one armrest and her legs over the other. His erect penis is inside her vagina.",
 "{M} sits on the edge of a bed with his feet apart and {W} lies on the floor facing up with her legs over his thighs. His erect penis is inside her vagina."],
'oral_extra':[
 "{W} kneels on all fours over {M}, who lies on his back beneath her with his face between her thighs, his hands on her hips and his tongue on her vulva.",
 "{W} sits on the face of {M}, who lies on his back, her knees either side of his head and her hands on the headboard, his tongue on her vulva.",
 "{M} stands upright and {W} kneels in front of him, her hands on his thighs, his erect penis in her mouth, while she looks up at him.",
 "{W} lies on her back with her legs over the shoulders of {M}, who kneels on the floor at the edge of the bed with his face at her vulva."],
'anal_extra':[
 "{W} lies on her side on a bed with her top leg raised and {M} lies behind her, his arm around her waist. His erect penis is inside her anus.",
 "{M} sits on a bed and {W} sits on his lap facing away from him, her feet flat on the mattress either side of his hips and her hands on his knees. His erect penis is inside her anus."],
'group':[
 "{W} kneels on all fours on a bed, with {M} kneeling behind her, his erect penis inside her vagina, and a second man __apose_person_m__, kneeling in front of her with his erect penis in her mouth, her hands on the mattress.",
 "{M} lies on his back on a bed with {W} straddling his hips facing him, his erect penis inside her vagina, and a second man __apose_person_m__, kneeling behind her holding her hips, his erect penis inside her anus."]}
def build(final):
    G={}
    for fam,lst in P.items():
        lines=[]
        for t in lst:
            s=t.format(W=PF,M=PM)
            nude=' All of them are nude.' if fam=='group' else ' Both are nude.'
            lines.append(s+nude+TAIL+CAM)
        for L in (5,6): G['adult_l%d_position_%s'%(L,fam)]=list(lines)
    G['adult_l5_position_all']=[x for f in P for x in G['adult_l5_position_%s'%f]]
    G['adult_l6_position_all']=list(G['adult_l5_position_all'])
    return G
if __name__=='__main__':
    G=build('')
    for k,v in G.items(): open('/home/claude/w/wildcards/%s.txt'%k,'w').write('\n'.join(v)+'\n')
    print({k:len(v) for k,v in G.items() if k.startswith('adult_l6')})
