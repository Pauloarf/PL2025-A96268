# Class T
- \#idfk
- Date: 2025-03-07 11:00 


# Notes

- ABC optional.
- 3+1 Worlds:
    - INITIAL:
        - Marked with `==>`
    - Metadata
        - Transitions to ABC with `<abc>`
        - Transitions to Poem with `\n\n`
        - Circles back with a KVP.
    - ABC
        - Transitions to Poem with `</abc>`
        - Circles back with a KVP.
    - Poem
        - Transitions to ABC with `<abc>`
        - Transitions to INITIAL with `==`
    - Represented in ply with `states`.

## PLY
- Define states with `states = [(name, kind)]`
- Use states with `t_STATE_TOKEN`.
- Define tokens for any state with `t_ANY_TOKEN`
- Starts with state `INITIAL`.