type action =
  | Increment of int
  | Decrement of int

let add (a: int) (b: int): int = a + b

let subtract (a: int) (b: int): int = a - b

let main(p,storage : action * storage) =
  let storage =
    match p with
    | Increment n -> add storage n
    | Decrement n -> subtract storage n
  in (([] : operation list), storage)
