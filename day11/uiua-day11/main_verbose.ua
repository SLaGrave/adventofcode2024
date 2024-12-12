ListToInt  ← ⋕/◇⊂°⋕
SplitInt   ← ↘2[⍥(⊃(⌊÷10)(◿10))∞]
EvenDigits ← ¬◿2⧻SplitInt
SplitValue ← ⊂⊃(ListToInt↙÷2⧻.)(ListToInt↘÷2⧻.)SplitInt
CondThree  ← × 2024
CondTwo    ← ⨬(CondThree)(SplitValue)EvenDigits .
CondOne    ← ⨬(CondTwo)(1)=0 .
Logic      ← CondOne
PartOne    ← ⧻◌:⍥(:⍥(:⊂⊙:Logic°⊂)⧻.)25:[]

[125 17]

⊂"Part one: "°⋕PartOne
