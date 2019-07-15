open Base
open Stdio

let fixed_xor left right =
  let hex_left = ("0x" ^ left) in
  let hex_right = ("0x" ^ right) in
  (Int.of_string hex_left) lxor (Int.of_string hex_right)
;;

let () =
  match In_channel.input_lines stdin with
  | [left; right] -> printf "%x\n" (fixed_xor left right)
  | _ -> print_endline "Incorrect usage of fixed_xor..."
;;
