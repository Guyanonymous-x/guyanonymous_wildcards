Guyanonymous' Wildcards v46 - setting, pose and interaction
============================================================
Person files describe only the person. Object files describe only the object. Setting, pose and interaction are separate files you combine yourself.

Poses            pose_free, pose_sitting, pose_lying, pose_leaning, pose_floating (no furniture implied)
                 pose_sitting_w_seat (+_short), pose_lying_w_surface (+_short), pose_leaning_w_support (+_short) - each describes its own seat/surface/support
                 pose_prompt (all), pose_prompt_no_support (safe in any setting)
Supports         seat_prompt, surface_lie_prompt, support_lean_prompt (also usable alone as objects); seat_phrase / seat_short for use in other prompts
Interactions     interact_two_prompt, interact_three_prompt, interact_object (positional wording: left, middle, right)
Settings         setting_prompt, setting_interior, setting_exterior (place + light + weather only)
Audit            _tools/audit/AUDIT_setting_pose_v46.txt
Entry points     v46_entry_points
Example          __any_create_random_person_short__ __pose_sitting_w_seat__ __setting_prompt__
