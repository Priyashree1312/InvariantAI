import Std

open Std

def valid_probability (p : Float) : Bool :=
  (0.0 ≤ p) && (p ≤ 1.0)

def main (args : List String) : IO Unit := do
  match args with
  | p_str :: _ =>
    match p_str.toNat? with
    | some n =>
      let p : Float := Float.ofNat n / 100.0

      if valid_probability p then
        IO.println s!"✔ Lean Proof: {toString p} satisfies 0 ≤ p ≤ 1"
      else
        IO.println s!"❌ Lean Violation: {toString p} out of bounds"
    | none =>
      IO.println "Invalid input"
  | _ =>
    IO.println "No input provided"
