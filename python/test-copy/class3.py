#!/usr/bin/env python
#To launch: python fileName.py

# Define class here
class genParticle(object):
    def __init__(self, pt, eta, phi, mass):
        '+++ Initialise particle pt, eta, phi'
        self.pt = pt
        self.eta = eta
        self.phi = phi
        self.mass = mass
    def set_pt (self, pt):
        '+++ Set particle pt (in GeV/c)'
        self.pt = pt
    def set_eta(self, eta):
        '+++ Set particle eta (no units)'
        self.eta = eta
    def set_phi(self, phi):
        '+++ Set particle phi (in radians)'
        self.phi = phi
    def set_mass(self, mass):
        '+++ Set particle mass (in GeV/cc)'
        self.mass = mass
    def PrintValues (self):
        print "+++ Printing genParticle default values"
        print "+++ pt = %s" % (self.pt)
        print "+++ eta = %s" % (self.eta)
        print "+++ phi = %s" % (self.phi)
        print "+++ mass = %s" % (self.mass)
        
if __name__ == '__main__':
    muon = genParticle(20, 2.1, 1.57, 0.1057)
    muon.PrintValues()
