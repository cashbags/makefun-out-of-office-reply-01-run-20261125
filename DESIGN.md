# Design — "Back on Tuesday, a date I chose because it sounds more believable than Friday."

## The idea

An out-of-office reply has one honest job: say when you are back. This line
does that job, then confesses in the same breath that the date was picked for
how believable it sounds, not for when the writer returns. The joke is not
attached to the message; it is the message.

## Why this line, criterion by criterion

1. **Real reply first.** "Back on Tuesday" is the most recognisable shape an
   auto-reply has. A reader knows what it is before finishing the first three
   words. It needs no signature, name, or outside context.
2. **Laugh on first read.** The twist arrives in the second clause with no
   setup: the date was chosen because it *sounds believable*. The reader gets
   the whole joke — the return date is invented — in one pass.
3. **Still a real away message.** Strip the joke and a return date remains.
   The humour lives inside the date, not bolted onto it.
4. **Fresh turn.** The field is full of houseplants, promoted auto-replies,
   pets minding inboxes, and beaches. Nobody in the 810-title field lies about
   the return date itself. "Believable" appears zero times in the field.
5. **Short, every word earns its place.** 78 characters, one sentence, one
   idea. "Tuesday" sets the frame, "believable" carries the joke, "Friday"
   lands the punch on the last word: the honest day would have been Friday,
   and Friday sounded too much like the truth to print.

## Why Tuesday and Friday

Tuesday is the most boring plausible return day, which is why it sounds
believable. Friday is the day the writer is actually coming back.

## Determinism

`main.py` writes one constant string to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(`/output` when unset). No network, no randomness, no clock, no input files,
no trailing newline. Two runs are byte-identical; hashes in BUILD-REPORT.md.