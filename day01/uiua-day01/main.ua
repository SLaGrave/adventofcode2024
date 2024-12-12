PartOne ← /+⌵/-≡⍆⍉
# Part two works on small input but not large... :(
PartTwo ← /+×⟜⊏:⊙⊢◌◌⍥(⊙(⊙⊂:/+⌕:,):°⊂)⊸⧻⇌⇡+1/↥.⊣,[]⍉

# File Read as String
&fras "../input.txt"
# Make it a 2d array
⊜(⊜⋕⊸≠@ )⊸≠@\n

⊂"Part one: "°⋕PartOne
