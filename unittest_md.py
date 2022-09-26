import sys, unittest
from md import calcenergy

class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        from ase.lattice.cubic import FaceCenteredCubic
        from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
        from ase.md.verlet import VelocityVerlet
        from ase import units
        from asap3 import Trajectory
        from asap3 import EMT
        size = 10
        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                              symbol="Cu",
                              size=(size, size, size),
                              pbc=True)
        atoms.calc = EMT()
        MaxwellBoltzmannDistribution(atoms, temperature_K=300)
        dyn = VelocityVerlet(atoms, 5 * units.fs)
        epot, ekin, temp, etot = calcenergy(atoms)
        self.assertTrue(round(etot, 3) == 0.038)

if __name__=="__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
