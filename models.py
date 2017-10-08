import pandas as pd


class Determinant(object):

    def __init__(self, segment, protein, residue, high=None, low=None):
        self.segment = segment # Integer
        self.protein = protein # String
        self.residue = residue # Integer
        self.high = high # Character
        self.low = low # Character


class Strain(object):

    def __init__(self, name, determinants):
        self.name = name # String
        self.determinants = determinants # List <Determinant Object>

        self.segments = {} # Dictionary <Segment Number [Integer] : Genomic Accession [String]>
        self.populate_segments()

        '''We only care about the segments that we have determinants on (1, 2, 6, 8)'''
        self.pathogenicity = [] # List <2/1/0> # len(pathogenicity) = 5
        self.populate_pathogenicity()

    def populate_segments(self):
        # Use pandas to populate self.segments

    def populate_pathogenicity(self):
        for determinant in self.determinants:
            seq = self.sequence(self.segments[determinant.segment])
            value = self.assess_value(seq, determinant)
            self.pathogenicity.append(value)

    def sequence(self, genomic_acc):
        # Use scraper to return the protein sequence

    def assess_value(self, seq, det):
        seq_residue = seq[det.residue] # Check if indexing is correct
        if seq_residue == det.high:
            return 2
        elif seq_residue == det.low:
            return 1
        else:
            return 0


det1 = Determinant(1, "PB2", 627, high='K', low='E')
det2 = Determinant(1, "PB2", 701, high='N', low='D')
det3 = Determinant(2, "PB1-F2", 66, high='S', low='N')
det4 = Determinant(6, "NA", 274, high='Y', low='H')
det5 = Determinant(8, "NS1", 92, high='E', low='D')

DETERMINANTS = [det1, det2, det3, det4, det5] # Order matters
