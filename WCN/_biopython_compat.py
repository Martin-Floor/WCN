"""Compatibility helpers for Biopython API changes."""

from __future__ import annotations

from Bio import PDB
from Bio.Data.IUPACData import protein_letters_3to1


def _normalize_resname(resname: str) -> str:
    """Normalize residue names to a 3-letter uppercase code."""
    if resname is None:
        return ""
    return str(resname).strip().upper()


def three_to_one_safe(resname: str, default: str = "X") -> str:
    """
    Convert a 3-letter residue name into one-letter code.

    Works across Biopython versions where ``three_to_one`` may have moved or
    been removed from public modules.
    """
    code = _normalize_resname(resname)
    if not code:
        return default

    # Newer Biopython versions may not expose this helper.
    try:
        return PDB.Polypeptide.three_to_one(code)
    except Exception:
        pass

    # Fallback independent of Biopython internals.
    return protein_letters_3to1.get(code.capitalize(), default)
