import numpy as np
import pandas as pd
from sklearn.utils.extmath import cartesian


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


class CrossData(object):

    def __init__(self, strain_one, strain_two, determinants):
        self.strain_one = strain_one
        self.strain_two = strain_two
        self.determinants = determinants
        self.cross_matrix = cartesian((np.array([[1, 2],] * 8)))
        self.det_matrix = np.zeros((256, 5), dtype=int)
        self.populate_det_matrix()
        self.det_bin = np.zeros((256, 3), dtype=int)
        self.populate_det_bin()
        self.data = self.run_analysis() # Dictionary

    def populate_det_matrix(self):
        for j in range(5):
            det = self.determinants[j]
            seg = det.segment
            for i in range(256):
                parent = self.cross_matrix[i][seg]
                if parent == 1:
                    strain = self.strain_one
                if parent == 2:
                    strain = self.strain_two
                value = strain.pathogenicity[j]
                self.det_matrix[i][j] = value

    def populate_det_bin(self):
        for i in range(256):
            zeros = 0
            ones = 0
            twos = 0
            for j in range(5):
                det = self.det_matrix[i][j]
                if det == 0:
                    zeros += 1
                if det == 1:
                    ones += 1
                if det == 2:
                    twos += 1
            self.det_bin[i][0] = zeros
            self.det_bin[i][1] = ones
            self.det_bin[i][2] = twos

    def run_analysis(self):
        output = {}
        output["reassortants1"] = self.get_reassortants1() # List of cross_matrix indices
        output["reassortants2"] = self.get_reassortants2() # List of cross_matrix indices
        output["reassortants3"] = self.get_reassortants3() # List of cross_matrix indices
        output["representation1"] = self.get_representation1() # Dictionary
        output["representation2"] = self.get_represetnation2() # Dictionary
        return output

    def get_reassortants1(self):
        # Create bin for each occurrence of an array using det_matrix

    def get_reassortants2(self):
        # Keep track of index and number of twos using det_bin

    def get_reassortants3(self):
        # Keep track of index and number of zeros using det_bin

    def get_representation1(self):
        # Compress det_bin to number of zeros, ones, and twos

    def get_representation2(self):
        # Compress det_matrix to majority zeros, ones, and twos


det1 = Determinant(1, "PB2", 627, high='K', low='E')
det2 = Determinant(1, "PB2", 701, high='N', low='D')
det3 = Determinant(2, "PB1-F2", 66, high='S', low='N')
det4 = Determinant(6, "NA", 274, high='Y', low='H')
det5 = Determinant(8, "NS1", 92, high='E', low='D')

DETERMINANTS = [det1, det2, det3, det4, det5] # Order matters
