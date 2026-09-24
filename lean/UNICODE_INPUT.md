# Typing Lean's Unicode symbols

In VS Code (with the Lean 4 extension), type `\` followed by an abbreviation; it is replaced
by the symbol when you press space or Tab. Many abbreviations are the LaTeX names.

**Unknown symbol?** Hover over it in VS Code — the tooltip shows how to type it.

The abbreviations below are taken from the extension's
[abbreviations.json](https://github.com/leanprover/vscode-lean4/blob/master/lean4-unicode-input/src/abbreviations.json).
Where several exist, the shortest/most memorable is listed first.

## Symbols used in this project

### Number systems

| Symbol | Type | Meaning |
|---|---|---|
| `ℝ` | `\R` or `\real` | real numbers (ASCII: `Real`) |
| `ℂ` | `\C` or `\com` | complex numbers (ASCII: `Complex`) |

### Logic

| Symbol | Type | Meaning |
|---|---|---|
| `∀` | `\all` or `\forall` | for all |
| `∃` | `\ex` or `\exists` | there exists |
| `∧` | `\and` | and (ASCII: `/\`) |
| `≠` | `\ne` | not equal |

### Arrows

| Symbol | Type | Meaning |
|---|---|---|
| `→` | `\r` or `\to` | function type / implication (ASCII: `->`) |
| `←` | `\l` or `\<-` | reverse rewrite, as in `rw [← h]` (ASCII: `<-`) |
| `↑` | `\u` or `\coe` | coercion (cast), e.g. ℝ → ℂ |

### Sums, products, integrals

| Symbol | Type | Meaning |
|---|---|---|
| `∑` | `\sum` | finite sum `∑ i, f i` |
| `∏` | `\prod` | finite product `∏ i, f i` |
| `∫` | `\integral` | integral `∫ x, f x` (note: `\int` gives `ℤ`!) |
| `π` | `\pi` | pi (needs `open scoped Real`) |

### Matrices, vectors, algebra

| Symbol | Type | Meaning |
|---|---|---|
| `ᵀ` | `\^T` | transpose `Pᵀ` (ASCII: `Matrix.transpose P`) |
| `*ᵥ` | `*\_v` | matrix × vector (ASCII: `Matrix.mulVec M x`) |
| `⬝ᵥ` | `\tr\_v` | dot product (ASCII: `dotProduct x y`) |
| `•` | `\smul` or `\bu` | scalar multiplication `c • M` |
| `⁻¹` | `\inv` or `\-1` | inverse `x⁻¹` |

### Brackets and tactic syntax

| Symbol | Type | Meaning |
|---|---|---|
| `⟨` `⟩` | `\<` `\>` | anonymous constructor, e.g. `⟨x, h⟩` |
| `·` | `\.` or `\cdot` | focus on the next goal in a tactic proof |

### Super- and subscripts

| Symbol | Type | Notes |
|---|---|---|
| `₀` `₁` … | `\0` `\1` … or `\_0` `\_1` … | subscript digits, e.g. `P₁` |
| `ⱼ` `ᵥ` | `\_j` `\_v` | subscript letters (`\_` + letter) |
| `²` `ⁿ` | `\^2` `\^n` | superscripts (`\^` + character) |

Sub-/superscripts in names like `P₁` are just part of the identifier — they have no
mathematical meaning to Lean. `x²` is **not** `x ^ 2`; write `x ^ 2` in formulas.

### Greek letters

| Symbol | Type | Symbol | Type |
|---|---|---|---|
| `κ` | `\kappa` or `\ka` | `η` | `\eta` or `\et` |
| `ξ` | `\xi` | `ϑ` | `\vartheta` |
| `λ` | `\lambda` or `\fun` | `Λ` | `\Lambda` or `\L` |

In general: `\` + the LaTeX name. Note `λ` is also Lean's (old) keyword for anonymous functions;
prefer `fun x => …` in code.

### Only in comments/docstrings

| Symbol | Type |
|---|---|
| `½` | `\frac12` |
| `√` | `\sqrt` |
| `∂` | `\partial` |

## Other common symbols (not used here yet)

| Symbol | Type | Meaning |
|---|---|---|
| `ℕ` `ℤ` `ℚ` | `\N` `\Z` (or `\int`) `\Q` | naturals, integers, rationals |
| `∨` | `\or` | or (ASCII: `\/`) |
| `¬` | `\not` | not |
| `↔` | `\iff` | if and only if (ASCII: `<->`) |
| `≤` `≥` | `\le` `\ge` | inequalities (ASCII: `<=` `>=`) |
| `∈` | `\in` | element of |
| `⊆` | `\sub` or `\ss` | subset |
| `∘` | `\comp` or `\circ` | function composition |
| `×` | `\x` or `\times` | product type |
| `↦` | `\mapsto` | maps to |
| `‖` | `\\|\|` | norm `‖x‖` |
| `∞` | `\infty` | infinity |
