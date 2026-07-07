# Challenge 03: Vigenère Cipher — Unknown Key Length

You are given a ciphertext (550 characters) with no other context.

```
VYEPE RKAVR QIDRV GUHVW EIEJX QGRRT CIEGL GJHVT HFRQI RRRGY TVAGH CNNGL GJAVP QISJS TBEQX JIOHK JKHRR KXHGG JVCXM PXEII TPRBT GRNQW CZLGL GTAEK QYAQF GVNYS CUEQG CIESY NCYNR FKHRQ CGSJI TVSGS TVDVR VYEPE RKAVR UTAOM PSESS TVFVV UKLVK JKTUI CECUS TNAFV CZSRH CEDGL GJHVT OFVRH UCOJP AFUGS HKHRL CIBBY TKHRA KEDJE UWAIS WIAOP GRNQF AEOBR VYELG QLLQR QCOAK GISRI VYEPS CJTGL GFCRE PJTEI VTHRH KEEII TPDVV GTTVS PRNQX JVCEI YJEGX NVDVR VFTUI KIRBY VZNRA CKCUI UKHRR CMITE VFRCP QKTRH VYEVV EFUEW GLSVR IKHRW VRRFE PUTUI EFMCE UJPBM PKIAK UKENH KCYAS TKHJE TUTBA CIDGL GZRQI UKIAE VZOAX JIERA GVKFE VJENP CPAUI CUBHX VYEPE RKAVR YRSPS PWIQI PKIAL KJSUM RRNQL KJMRR
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
