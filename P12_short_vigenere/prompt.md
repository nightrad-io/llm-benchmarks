# Challenge 06: Short Polyalphabetic — Unknown Language, Minimal Length

You are given a ciphertext (96 characters) with no other context.

```
EYTGV AHHFB TAKYF LOGQY HYPWV YPRUF KJIOO ZFWJZ VBTHC OPKCL CBDBV LUQCG XYKZU OPKFH DPTTW YTNCK UPKLM YRLOX NLSMV L
```

## Task

Using a multi-stage approach:

**Stage 1 — Cipher Classification**
Measure the Index of Coincidence and any other discriminating statistics.
Determine the most likely cipher class (monoalphabetic substitution,
polyalphabetic, transposition, polygram, or unknown/compound).
Commit to a classification with a confidence assessment before proceeding.

**Stage 2 — Language Identification** *(if applicable)*
If Stage 1 indicates substitution or transposition, identify the underlying
plaintext language using letter-frequency analysis.
Use the method confirmed as most reliable for this cipher class.

**Stage 3 — Key Recovery and Decryption**
Using only the method you committed to in planning, attempt to recover the
key and decrypt the plaintext.

Report your results for all stages including confidence, exact statistics
measured, and — if Stage 3 is unsuccessful — an honest PARTIAL report with
the best output achieved and the reason for the limitation.
