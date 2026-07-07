# Challenge 08: Compound Cipher — Substitution + Columnar Transposition

You are given a ciphertext (372 characters) with no other context.

```
GZFHG INGZT BIFIM NGJHN FGGSZ CBXHI GGRSZ HZXZX NBFZG IGIAG WGZYR QHIZG KGKGH FXYJM OOJGH NGMFM ZMHHF HMDGB GQZMI GIQQG OCHHH MMBHG MTXMM NIGXG YFGCQ IYYMG JJSXH MBQZI FCCSN ZMFQH BCMFI MHYHG CQNGG DOWQF HJXHH GHZDQ QHXZK CRHRI NHGQM HNGWO DHGXT HIHZG KFECZ GXQFK FICCY XINGN XGFNN GFQFB MIRMH HTOZG NGRIA CIGGY HCQGH YCGSH BTMXX QGHNM XCNEB IJGXO QGGHH HQQMO BQGFG ZGONG ZZMFM XMQGH SZQGJ ANNBH GIWBS GIYHX SQGNZ GAQHI BWCDM RUGFM NGJHC SFHHZ SH
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
