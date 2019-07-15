open Base
open Stdio

let conv_hex_to_bin hex_string =
  match String.uppercase hex_string with
  | "0" -> "0000"
  | "1" -> "0001"
  | "2" -> "0010"
  | "3" -> "0011"
  | "4" -> "0100"
  | "5" -> "0101"
  | "6" -> "0110"
  | "7" -> "0111"
  | "8" -> "1000"
  | "9" -> "1001"
  | "A" -> "1010"
  | "B" -> "1011"
  | "C" -> "1100"
  | "D" -> "1101"
  | "E" -> "1110"
  | "F" -> "1111"
  | _ -> ""
;;

let combine_chars =
  List.fold_left ~init:"" ~f:(fun a b -> a ^ b)
;;

let hex_to_bin hex_string =
  hex_string
  |> String.to_list
  |> List.map ~f:(Char.to_string)
  |> List.map ~f:conv_hex_to_bin
  |> combine_chars
;;

let conv_bin_to_base64 bin_string =
  let dec = Int.of_string ("0b" ^ bin_string) in
  match dec with
  | 0 -> "A"
  | 1 -> "B"
  | 2 -> "C"
  | 3 -> "D"
  | 4 -> "E"
  | 5 -> "F"
  | 6 -> "G"
  | 7 -> "H"
  | 8 -> "I"
  | 9 -> "J"
  | 10 -> "K"
  | 11 -> "L"
  | 12 -> "M"
  | 13 -> "N"
  | 14 -> "O"
  | 15 -> "P"
  | 16 -> "Q"
  | 17 -> "R"
  | 18 -> "S"
  | 19 -> "T"
  | 20 -> "U"
  | 21 -> "V"
  | 22 -> "W"
  | 23 -> "X"
  | 24 -> "Y"
  | 25 -> "Z"
  | 26 -> "a"
  | 27 -> "b"
  | 28 -> "c"
  | 29 -> "d"
  | 30 -> "e"
  | 31 -> "f"
  | 32 -> "g"
  | 33 -> "h"
  | 34 -> "i"
  | 35 -> "j"
  | 36 -> "k"
  | 37 -> "l"
  | 38 -> "m"
  | 39 -> "n"
  | 40 -> "o"
  | 41 -> "p"
  | 42 -> "q"
  | 43 -> "r"
  | 44 -> "s"
  | 45 -> "t"
  | 46 -> "u"
  | 47 -> "v"
  | 48 -> "w"
  | 49 -> "x"
  | 50 -> "y"
  | 51 -> "z"
  | 52 -> "0"
  | 53 -> "1"
  | 54 -> "2"
  | 55 -> "3"
  | 56 -> "4"
  | 57 -> "5"
  | 58 -> "6"
  | 59 -> "7"
  | 60 -> "8"
  | 61 -> "9"
  | 62 -> "+"
  | 63 -> "/"
  | _ -> ""
;;

let bin_to_base64 bin_string =
  bin_string
  |> String.to_list
  |> List.map ~f:(Char.to_string)
  |> List.groupi ~break:(fun i _ _ -> i % 6 = 0)
  |> List.map ~f:(combine_chars)
  |> List.map ~f:(conv_bin_to_base64)
  |> combine_chars
;;

let hex_to_base64 hex_string =
  hex_string
  |> hex_to_bin
  |> bin_to_base64
;;

let () =
  match In_channel.input_line stdin with
  | None -> prerr_endline "Something went wrong with reading from stdin..."
  | Some hex -> print_endline (hex_to_base64 hex)
;;
