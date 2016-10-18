#Reversing class r2 cheatsheet

#Notes
   -append ? to most commands to print help, other sub-commands not listed here, and in some cases examples
   -see ?$? for built-in vars (e.g. $$ equals current seek)
   
#File information
   i -> file info
   is -> symbols
   iS -> sections
      S= -> sections visual
   il -> libraries
   ii -> imports
   ir -> relocations
   iz -> strings in .rodata section

#Positioning - Current examination position in file; this address is the default for other commands
   s 0x00001000 -> "seek"/position to 0x0001000
   s-/s+ 100 -> seek backwards/forward 100 bytes, without number: undo/redo seek
   s--/s++ -> seek back/forward block size
   
#Block Size - Current examination size; this number (in bytes) is the default for other commands
   b -> print current block size
   b 0x100 -> set block size to 0x100 bytes
   b-/+ 3 -> decrease/increase block size by 3 bytes
   b eip+4 -> set to result of expression

#Analysis
   aa -> analyze all functions and basic blocks (blocks of code that together are of one sequential control flow; i.e. no branching)
   afl -> list functions
   afn -> rename function (changes it's flag too)
   afF -> fold/unfold function (shrinks it's code to a placeholder for easier viewing)
   afvn -> rename local argument or variable

#Flags - bookmarks for certain addresses of interest, e.g. functions, sections, symbols
   f -> print all flags. useful with ~ (grep output, e.g. f~main)
   f new_flag @ addr -> create new flag named new_flag at position 'addr'
   f-new_flag -> delete flag

#Comments
   CC -> list all comments
   CC "new comment" -> add new comment to current address
   
#Searching
   / hello -> search for string "hello"
   /i Hello -> search for string, ignore case
   /e /E.F/i -> search for matching regular expression.  expression is contained with the two '/' forward slashes

#Printing
   p8 -> print block-size number of hex pairs at current address.  different size and address: p8 10 @ addr
   px -> print hexdump
   pd 10 -> print disassembly of next ten instructions
   pD 10 -> print disassembly of next ten bytes
   ps -> print string
   pf -> print formatted data.  great for specifying member names and types of data structures.  see pf?? for formatting options. pf??? shows some examples.
   pf xiz ptr1 int1 str1 -> print three fields, named ptr1 (hex value, respects endianess), int1 (integer), and str1 (zero-terminated string)

#Writing - to write to files, add -w flag when opening r2
   wc -> list all write changes
   w foo -> write string 'foo' at current seek. 'wz' will add a zero for termination.
   wa -> write assembly instructions, separated by semi-colons
   
#Yanking/Pasting
   y 10 @ addr -> yank (copy) 10 bytes from address 'addr' to clipboard
   yp -> print clipboard contents
   yy -> paste contents to current seek

#Visual Mode
   hjkl/HJKL -> move around, 10 lines at a time for uppercase
   ? -> visual mode help
   o -> seek to offset (prompt)
   : -> enter r2 command
   . -> seek to program counter
   ;/;- -> add/remove comment
   p/P -> change print mode (hexdump, disassembly dump being the most used)
   Space -> Enter ascii graph view. press p/P to see different graph print modes.  use tab to switch between the basic blocks, or use t/f (true/false to follow the logic control flow)
   Tab -> change from selecting from hex to ascii and vice-versa in hexdump view
   0-9 -> goto external reference (xref) (see to the right of disassembly)
   c -> enter cursor mode, hold shift and move around to make a selection
   y/Y -> copy/paste selection

#Debugging
   db -> set/handle breakpoints.  'b' to set breakpoint in visual mode
   dr/drr -> show register values/dereference
   ds/dso/dc -> step/step over/continue (s/S to step in visual mode)
