# Challenge 02: Monoalphabetic Substitution — Unknown Language

You are given a ciphertext (537 characters) with no other context.

```
RGBSH XTTIE JHRTZ TASHS AGLWQ ZDQNT HTZRT ICSBB JQZTB TGHTH THISO ISYSO SBSOB SLXJL SBCSJ ITGHK BGOQX BSTGH SIXSN QYOTV GTHQM QXBQX BSTGH SKGJX SBBSO SBSSL QAOSH SBISA GZJLS IQZAS MQBTZ ZTZJT HXSHT HIQZC SHLQZ LTBLS HQZMQ CZTBN SHLQH LGBJQ ZJRSR AJTHX BSZLQ HNTBZ SHTHX BTTII QZLGS HRQLS TISHQ LWTTH LJTHR THIGL TZRTL QIQBT ZMTIS ACJTH XTZTN GTINT ASZSH JASRQ XQRSN JSSIK GHQZN TLJHQ ZZTVG TDSHR TIBGJ RQOTB QISAS MQBJS RJZEB GXSRT ISLTI TCBSL JQHJA OBQNJ ZSRST HTIDS BRJHR TISSC GTISL BTLTH ISZSI LSLWQ ESZAS ZKBSH RTZRT IOGTC IQZQH XSHKB SHRTZ LQAQO TIQXS ZRTEG XCQIM ISSCG TISIS ZLGJR SLQHA GLWQS AQBLS RSNTB SHQIS ZNTHR TTHTI ATBLS RQIQL SI
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
