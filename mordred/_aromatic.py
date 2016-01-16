from ._base import Descriptor


class AromaticAtomsCount(Descriptor):
    r'''
    aromatic atoms count descriptor

    Returns:
        int: count of aromatic atoms
    '''

    def __str__(self):
        return 'nAromAtom'

    def calculate(self, mol):
        return sum(1 for a in mol.GetAtoms() if a.GetIsAromatic())


class AromaticBondsCount(Descriptor):
    r'''
    aromatic bonds count descriptor

    Returns:
        int: count of aromatic bonds
    '''

    def __str__(self):
        return 'nAromBond'

    def calculate(self, mol):
        return sum(1 for b in mol.GetBonds() if b.GetIsAromatic())
